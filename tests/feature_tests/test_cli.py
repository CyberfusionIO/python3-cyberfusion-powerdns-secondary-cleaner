import docopt
import pytest
from _pytest.capture import CaptureFixture
from pytest_mock import MockerFixture
from requests_mock.mocker import Mocker

from cyberfusion.PowerDNSSecondaryCleaner import CLI


def test_cli_get_args() -> None:
    with pytest.raises(SystemExit):
        CLI.get_args()


def test_cli_absent(
    mocker: MockerFixture,
    requests_mock: Mocker,
    delete_mock: None,
    capsys: CaptureFixture,
    primary_api_url: str,
    primary_api_key: str,
    secondary_api_url: str,
    secondary_api_key: str,
    primary_zones_mock_absent: list,
    secondary_zones_mock: list,
) -> None:
    mocker.patch(
        "cyberfusion.PowerDNSSecondaryCleaner.CLI.get_args",
        return_value=docopt.docopt(
            CLI.__doc__,
            [
                "--primary-api-url",
                primary_api_url,
                "--primary-api-key",
                primary_api_key,
                "--secondary-api-url",
                secondary_api_url,
                "--secondary-api-key",
                secondary_api_key,
            ],
        ),
    )

    CLI.main()

    delete_requests = [r for r in requests_mock.request_history if r.method == "DELETE"]

    assert len(delete_requests) == 1
    assert (
        delete_requests[0].url
        == secondary_api_url
        + "/api/v1/servers/localhost/zones/"
        + secondary_zones_mock[1]["id"]
    )

    assert (
        capsys.readouterr().out
        == f"Keeping {secondary_zones_mock[0]['id']}\nDeleting {secondary_zones_mock[1]['id']}\n"
    )


def test_cli_absent_dry_run(
    mocker: MockerFixture,
    requests_mock: Mocker,
    delete_mock: None,
    capsys: CaptureFixture,
    primary_api_url: str,
    primary_api_key: str,
    secondary_api_url: str,
    secondary_api_key: str,
    primary_zones_mock_absent: list,
    secondary_zones_mock: list,
) -> None:
    mocker.patch(
        "cyberfusion.PowerDNSSecondaryCleaner.CLI.get_args",
        return_value=docopt.docopt(
            CLI.__doc__,
            [
                "--primary-api-url",
                primary_api_url,
                "--primary-api-key",
                primary_api_key,
                "--secondary-api-url",
                secondary_api_url,
                "--secondary-api-key",
                secondary_api_key,
                "--dry-run",
            ],
        ),
    )

    CLI.main()

    assert not any(r.method == "DELETE" for r in requests_mock.request_history)

    assert (
        capsys.readouterr().out
        == f"Keeping {secondary_zones_mock[0]['id']}\nWould delete {secondary_zones_mock[1]['id']}\n"
    )


def test_cli_present(
    mocker: MockerFixture,
    requests_mock: Mocker,
    capsys: CaptureFixture,
    primary_api_url: str,
    primary_api_key: str,
    secondary_api_url: str,
    secondary_api_key: str,
    primary_zones_mock_present: list,
    secondary_zones_mock: list,
) -> None:
    mocker.patch(
        "cyberfusion.PowerDNSSecondaryCleaner.CLI.get_args",
        return_value=docopt.docopt(
            CLI.__doc__,
            [
                "--primary-api-url",
                primary_api_url,
                "--primary-api-key",
                primary_api_key,
                "--secondary-api-url",
                secondary_api_url,
                "--secondary-api-key",
                secondary_api_key,
            ],
        ),
    )

    CLI.main()

    assert not any(r.method == "DELETE" for r in requests_mock.request_history)

    assert (
        capsys.readouterr().out
        == f"Keeping {secondary_zones_mock[0]['id']}\nKeeping {secondary_zones_mock[1]['id']}\n"
    )
