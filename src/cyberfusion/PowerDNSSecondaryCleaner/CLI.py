"""powerdns-secondary-cleaner.

Usage:
   powerdns-secondary-cleaner --primary-api-url=<primary-api-url> --primary-api-key=<primary-api-key> --secondary-api-url=<secondary-api-url> --secondary-api-key=<secondary-api-key> [--dry-run]

Options:
  -h --help                                 Show this screen.
  --primary-api-url=<primary-api-url>       URL of primary PowerDNS server API.
  --primary-api-key=<primary-api-key>       Key for primary PowerDNS server API.
  --secondary-api-url=<secondary-api-url>   URL of secondary PowerDNS server API.
  --secondary-api-key=<secondary-api-key>   Key for secondary PowerDNS server API.
  --dry-run                                 Only show which zones would be deleted on secondary.
"""

import docopt
from schema import Schema

from cyberfusion.PowerDNSSecondaryCleaner.powerdns_api import PowerDNSAPI


def get_args() -> docopt.Dict:
    """Get docopt args."""
    return docopt.docopt(__doc__)


def main() -> None:
    """Spawn relevant class for CLI function."""

    # Validate input

    args = get_args()
    schema = Schema(
        {
            "--primary-api-url": str,
            "--primary-api-key": str,
            "--secondary-api-url": str,
            "--secondary-api-key": str,
            "--dry-run": bool,
        }
    )
    args = schema.validate(args)

    # Run classes

    primary_api = PowerDNSAPI(args["--primary-api-url"], args["--primary-api-key"])
    primary_zones = primary_api.get_zones()

    secondary_api = PowerDNSAPI(
        args["--secondary-api-url"], args["--secondary-api-key"]
    )
    secondary_zones = secondary_api.get_zones()

    for zone in secondary_zones:
        if zone in primary_zones:
            print(f"Keeping {zone.id_}")

            continue

        if not args["--dry-run"]:
            print(f"Deleting {zone.id_}")

            secondary_api.delete_zone(zone.id_)
        else:
            print(f"Would delete {zone.id_}")
