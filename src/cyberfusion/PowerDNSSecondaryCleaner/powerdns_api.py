"""Classes to use PowerDNS API."""

from dataclasses import dataclass
from typing import List

import requests

TIMEOUT = 60


@dataclass
class Zone:
    """Represents PowerDNS zone."""

    id_: str

    @classmethod
    def from_powerdns_api(cls, data: dict) -> "Zone":
        """Get class from API payload."""
        return cls(id_=data["id"])


class PowerDNSAPI:
    """Represents PowerDNS API."""

    def __init__(self, api_url: str, api_key: str) -> None:
        """Set attributes."""
        self.api_url = api_url
        self.api_key = api_key

    def _execute_get_request(self, endpoint: str) -> dict:
        """Execute GET request and get response."""
        request = requests.get(
            f"{self.api_url}/api/v1/servers/localhost/{endpoint}",
            timeout=TIMEOUT,
            headers={"X-API-Key": self.api_key},
        )
        request.raise_for_status()

        return request.json()

    def _execute_delete_request(self, endpoint: str) -> None:
        """Execute DELETE request."""
        request = requests.delete(
            f"{self.api_url}/api/v1/servers/localhost/{endpoint}",
            timeout=TIMEOUT,
            headers={"X-API-Key": self.api_key},
        )
        request.raise_for_status()

    def get_zones(self) -> List[Zone]:
        """Get zones."""
        zones = self._execute_get_request("zones")

        return [Zone.from_powerdns_api(zone) for zone in zones]

    def delete_zone(self, id_: str) -> None:
        """Delete zone."""
        self._execute_delete_request(f"zones/{id_}")
