"""A setuptools based setup module."""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="powerdns-secondary-cleaner",
    version="1.0.2",
    description="Use powerdns-secondary-cleaner to delete zones on secondary PowerDNS server that were deleted on primary PowerDNS server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Cyberfusion",
    author_email="support@cyberfusion.io",
    url="https://github.com/CyberfusionIO/powerdns-secondary-cleaner",
    platforms=["linux"],
    packages=find_packages(
        include=[
            "powerdns_secondary_cleaner",
            "powerdns_secondary_cleaner.*",
        ]
    ),
    data_files=[],
    entry_points={
        "console_scripts": [
            "powerdns-secondary-cleaner=powerdns_secondary_cleaner.CLI:main"
        ]
    },
    install_requires=["docopt==0.6.2", "schema==0.7.7", "requests==2.32.3"],
)
