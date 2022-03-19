from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="dotted-ml",
    description="Translate text to and from DML with ease.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/RGBCube/dml",
    version="1.0.0",
    author="RGBCube",
    py_modules=["dml"],
    license="MIT"
)
