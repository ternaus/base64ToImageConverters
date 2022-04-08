from pathlib import Path

import setuptools

PACKAGE_NAME = "image_to_base_64"
VERSION = "0.0.1"
AUTHOR = "Vladimir Iglovikov"
DESCRIPTION = "Image to base64 and back."
GITHUB_URL = "https://github.com/ternaus/base64ToImageConverters"

parent_dir = Path(__file__).parent.absolute()

with (parent_dir / "README.md").open() as f:
    long_description = f.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    package_dir={"base64_image_converters": "."},
    extras_require={"tests": ["pytest"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
