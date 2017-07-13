# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from setuptools import setup

def readme():
    with open('./README.rst') as f:
        return f.read()

setup(name='axe-selenium-python',
    version='0.0.2',
    description='Python library to integrate axe and selenium for web \
                accessibility testing.',
    long_description=readme(),
    url='http://github.com/kimberlythegeek/axe_selenium_python',
    author='Kimberly Pennington',
    author_email='kpennington@mozilla.com',
    packages=['axe_selenium_python'],
    install_requires=[
        'pytest-selenium>=1.10.0',
        'pytest>=3.0'
    ],
    license='Mozilla Public License 2.0 (MPL 2.0)',
    keywords='axe-core selenium pytest-selenium accessibility automation mozilla')
