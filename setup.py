# coding: utf-8

"""
    Manticore Search Client

    Contact: info@manticoresearch.com
"""


from setuptools import setup, find_packages
from os import path

NAME = "manticoresearch"
VERSION = "1.0.4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
long_description = ""
with open(path.join(path.dirname(__file__), "README.md")) as f:
    for line in f:
      if '## Documentation for API Endpoints' in line:
        break
      long_description +=line
setup(
    name=NAME,
    version=VERSION,
    description="Python client for Manticore Search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Manticore Software Ltd.",
    author_email="info@manticoresearch.com",
    url="",
    keywords=[ "full-text search","manticoresearch","search"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
	    project_urls={
        "Documentation": "https://github.com/manticoresoftware/manticoresearch-python/tree/master/docs",
        "Source Code": "https://github.com/manticoresoftware/manticoresearch-python",
        "Issue Tracker": "https://github.com/manticoresoftware/manticoresearch-python/issues",
    },
	classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search"
    ],
    license="Apache 2.0",
)
