from powerdns_secondary_cleaner.powerdns_api import PowerDNSAPI, Zone


def test_get_zones(
    primary_api_url: str, primary_api_key: str, primary_zones_mock_absent: list
) -> None:
    assert PowerDNSAPI(
        api_url=primary_api_url, api_key=primary_api_key
    ).get_zones() == [Zone(id_=primary_zones_mock_absent[0]["id"])]
