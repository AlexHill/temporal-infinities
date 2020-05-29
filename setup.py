import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    author="Alex Hill",
    author_email="alex@hill.net.au",
    name="temporal-infinities",
    version="0.1.0",
    description="Infinities for datetime, date and timedelta.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexhill/temporal-infinities",
    py_modules=["temporal_infinities"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
