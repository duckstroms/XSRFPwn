#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#    XSRF Pwn       #
#-:-:-:-:-:-:-::-:-:#

# Author: duckstroms
# This module requires XSRFPwn
# https://github.com/duckstroms/XSRFPwn

import io
from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

setup(
    name='xsrfpwn',
    version=__import__('xsrfpwn').__version__,
    description='The Prime Cross Site Request Forgery (CSRF) Audit & Exploitation Toolkit',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='Pinaki Mondal',
    author_email='pwn0sec@cyberservices.com',
    license='GPLv3',
    url='https://github.com/duckstroms/XSRFPwn',
    download_url='https://github.com/duckstroms/XSRFPwn/archive/v%s.zip' % __import__('xsrfpwn').__version__,
    packages=find_packages(),
    scripts=['xsrfpwn/bin/xsrfpwn'],
    install_requires=[
        'requests',
        'bs4',
        'stringdist',
        'tld',
        'yattag'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: Security',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    keywords=['csrf', 'xsrf', 'appsec', 'vulnerability scanner', 'webapps', 'hacking'],
)
