import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "AirbnbViz: an analysis and visualization tool of Airbnb homes in Seattle"
# Long description will go up on the pypi page
long_description = """
AirbnbViz
========
AirbnbViz is an analysis and visualization tool of Airbnb homes in Seattle. It
contains four parts: 
1. listing information. This part shows information of each single Airbnb home.
2. Rating Visualization. This part shows a visualization of average rating by neighbourhood.
3. Price Visualization. This part shows a visualization of average price by neighbourhood.
4. Listing Price Prediction. This part enables users to predict listing  price by inputing pameraters.
To get started using these components in your own software, please go to the
repository README_.
.. _README: https://github.com/wangbeiqi199159/analyze-of-seattle-airbnb-hosts/blob/master/README.md
License
=======
``AirbnbViz`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.
All trademarks referenced herein are property of their respective holders.
Copyright (c) 2017 Becky Wang, University of Washington
"""

NAME = "AirbnbViz"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/wangbeiqi199159/analyze-of-seattle-airbnb-hosts"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Beiqi Wang | Jingyan Yang | Runlai Zeng"
AUTHOR_EMAIL = "beiqiw@uw.edu"
VERSION = "__version__ 1.0"
PACKAGE_DATA = {'shablona': [pjoin('data', '*')]}
REQUIRES = ["numpy", "pandas", "sklearn"]

opts = dict(name=NAME,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            install_requires=REQUIRES,
            requires=REQUIRES)


if __name__ == '__main__':
    setup(**opts)






