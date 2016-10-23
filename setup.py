#!/usr/bin/env python

from setuptools import setup, find_packages
INSTALL_REQUIRES = []


def main():
    setup(
        name="fake-micropython",
        version="0.1",
        url="https://github.com/CatherineH/fake-micropython",
        author="Catherine Holloway",
        author_email="milankie@gmail.com",
        packages=find_packages(),
        description="A package to emulate the behavior of micropython using "
                    "standard python.",
        install_requires=INSTALL_REQUIRES,
        zip_safe=True
    )

if __name__ == "__main__":
    main()