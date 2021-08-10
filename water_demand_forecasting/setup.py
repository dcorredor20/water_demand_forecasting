#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
]

test_requirements = []

setup(
    author="Diego",
    author_email="dcorredor20@hotmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Short-term water demand a district level [D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[Dt a[C[C[C[C[C[C[C[C district level",
    entry_points={
        "console_scripts": [
            "water_demand_forecasting=water_demand_forecasting.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="water_demand_forecasting",
    name="water_demand_forecasting",
    packages=find_packages(
        include=["water_demand_forecasting", "water_demand_forecasting.*"]
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/dcorredor20/water_demand_forecasting",
    version="0.1.0",
    zip_safe=False,
)
