# python3-cyberfusion-powerdns-secondary-cleaner

Use powerdns-secondary-cleaner to delete zones on secondary PowerDNS server that were deleted on primary PowerDNS server.

 The PowerDNS API is used for both the primary and secondary, so the program can run anywhere. Be it on the primary, secondary or elsewhere.

# Install

## PyPI

Run the following command to install the package from PyPI:

    pip3 install python3-cyberfusion-powerdns-secondary-cleaner

## Debian

Run the following commands to build a Debian package:

    mk-build-deps -i -t 'apt -o Debug::pkgProblemResolver=yes --no-install-recommends -y'
    dpkg-buildpackage -us -uc

# Configure

No configuration is supported.

# Usage

Syntax:

    powerdns-secondary-cleaner --primary-api-url=<primary-api-url> --primary-api-key=<primary-api-key> --secondary-api-url=<secondary-api-url> --secondary-api-key=<secondary-api-key> [--dry-run]

Example when running on primary:

    powerdns-secondary-cleaner --primary-api-url=http://localhost:8081 --primary-api-key=example --secondary-api-url=http://secondary.test:8081 --secondary-api-key=example

Example when running on secondary:

    powerdns-secondary-cleaner --secondary-api-url=http://localhost:8081 --secondary-api-key=example --primary-api-url=http://primary.test:8081 --primary-api-key=example

Only show which zones would be deleted on secondary:

    powerdns-secondary-cleaner ... --dry-run
