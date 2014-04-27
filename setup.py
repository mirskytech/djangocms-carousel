#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from djangocms_column import __version__


INSTALL_REQUIRES = [

]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='djangocms-slider',
    version=__version__,
    description='Slider Plugin for django CMS',
    author='Andrew Mirsky',
    author_email='andrew@mirsky.net',
    url='https://github.com/divio/djangocms-slider',
    packages=['djangocms_slider', 'djangocms_slider.migrations'],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False
)