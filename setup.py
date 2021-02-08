#!/usr/bin/env python3

from setuptools import setup


def getRequirements():
    requirements = []
    with open("requirements.txt", "r") as reqfile:
        for line in reqfile.readlines():
            requirements.append(line.strip())
    return requirements


setup(
    python_requires=">=3.8",
    name="pymdmix",
    version="4.0.0",
    description="pymdmix meta-package",
    author="ggutierrez-bio",
    author_email="",
    url="https://github.com/ggutierrez-bio/mdmix4",
    install_requires=getRequirements(),
)
