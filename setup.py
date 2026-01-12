from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gitstar",
    version="1.0.1",
    author="Imran Pollob",
    author_email="imranpollob@gmail.com",
    description="Find out the total star earned by a github user",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imranpollob/gitstar",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "gitstar=gitstar.core:main",
        ],
    },
)
