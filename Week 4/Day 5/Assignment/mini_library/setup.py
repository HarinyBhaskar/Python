from setuptools import setup, find_packages

setup(
    name="mini-library",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mylib=mini_library.cli:main",
        ],
    },
    python_requires=">=3.6",
)
