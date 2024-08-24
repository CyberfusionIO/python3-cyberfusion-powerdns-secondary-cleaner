import re

import pytest
from requests_mock.mocker import Mocker


@pytest.fixture
def primary_api_url() -> str:
    return "http://primary.test:8081"


@pytest.fixture
def primary_api_key() -> str:
    return "primary"


@pytest.fixture
def secondary_api_url() -> str:
    return "http://secondary.test:8081"


@pytest.fixture
def secondary_api_key() -> str:
    return "secondary"


@pytest.fixture
def delete_mock(requests_mock: Mocker, secondary_api_url: str) -> None:
    requests_mock.delete(
        re.compile(f"^{secondary_api_url}/api/v1/servers/localhost/zones/"),
        status_code=204,
    )


@pytest.fixture
def primary_zones_mock_absent(requests_mock: Mocker, primary_api_url: str) -> list:
    """Mock zones on primary where 1 zone is absent that is present on the secondary."""
    data = [
        {
            "account": "",
            "dnssec": False,
            "edited_serial": 2023062911,
            "id": "example1.test.",
            "kind": "Master",
            "last_check": 0,
            "masters": [],
            "name": "example1.test.",
            "notified_serial": 2023062910,
            "serial": 2023062910,
            "url": "/api/v1/servers/localhost/zones/example1.test.",
        }
    ]

    requests_mock.get(f"{primary_api_url}/api/v1/servers/localhost/zones", json=data)

    return data


@pytest.fixture
def primary_zones_mock_present(requests_mock: Mocker, primary_api_url: str) -> list:
    """Mock zones on primary where all zones are present that are present on the secondary."""
    data = [
        {
            "account": "",
            "dnssec": False,
            "edited_serial": 2023062911,
            "id": "example1.test.",
            "kind": "Master",
            "last_check": 0,
            "masters": [],
            "name": "example1.test.",
            "notified_serial": 2023062910,
            "serial": 2023062910,
            "url": "/api/v1/servers/localhost/zones/example1.test.",
        },
        {
            "account": "",
            "dnssec": False,
            "edited_serial": 2023062911,
            "id": "example2.test.",
            "kind": "Master",
            "last_check": 0,
            "masters": [],
            "name": "example2.test.",
            "notified_serial": 2023062910,
            "serial": 2023062910,
            "url": "/api/v1/servers/localhost/zones/example2.test.",
        },
    ]

    requests_mock.get(f"{primary_api_url}/api/v1/servers/localhost/zones", json=data)

    return data


@pytest.fixture
def secondary_zones_mock(requests_mock: Mocker, secondary_api_url: str) -> list:
    data = [
        {
            "account": "",
            "dnssec": False,
            "edited_serial": 2023062911,
            "id": "example1.test.",
            "kind": "Slave",
            "last_check": 1688298261,
            "masters": ["2001:0db8:a:b::1"],
            "name": "example1.test.",
            "notified_serial": 0,
            "serial": 2023062911,
            "url": "/api/v1/servers/localhost/zones/example1.test.",
        },
        {
            "account": "",
            "dnssec": False,
            "edited_serial": 2023062911,
            "id": "example2.test.",
            "kind": "Slave",
            "last_check": 1688298261,
            "masters": ["2001:0db8:a:b::1"],
            "name": "example2.test.",
            "notified_serial": 0,
            "serial": 2023062911,
            "url": "/api/v1/servers/localhost/zones/example2.test.",
        },
    ]

    requests_mock.get(f"{secondary_api_url}/api/v1/servers/localhost/zones", json=data)

    return data
