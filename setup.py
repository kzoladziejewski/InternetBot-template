"""
This file is for generate python pkg
"""

import setuptools
import pathlib

with open(pathlib.Path(__file__).cwd().joinpath("VERSION")) as version_file:
    version = version_file.read()

with open(pathlib.Path(__file__).cwd().joinpath("README.md")) as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name = "bot",
    version=version_file,
    author="Kacper Zoladziejewski",
    author_email="kzoladziejewski@kacpur.pl",
    packages=setuptools.find_packages(),
    python_required='>=3.7'

)