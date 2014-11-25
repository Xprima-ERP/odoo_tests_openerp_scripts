#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'psycopg2==2.5.4',
    'argparse==1.2.2',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='Odoo Tests',
    version='0.1.0',
    description='Test script to be used with Anybox Odoo recipe.',
    long_description=readme + '\n\n' + history,
    author='Sebastien Delisle',
    author_email='seb0del@gmail.com',
    url='https://github.com/maxc0c0s/odoo_tests',
    packages=[
        'odoo_tests',
    ],
    package_dir={'odoo_tests':
                 'odoo_tests'},
    include_package_data=True,
    install_requires=requirements,
    license="GNU GPL v3.0",
    zip_safe=False,
    keywords='odoo_tests',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        "console_scripts": [
            "test_odoo = odoo_tests.odoo_tests:main",
            "create_db = odoo_tests.odoo_tests:create_db",
            "drop_db = odoo_tests.odoo_tests:drop_db",
        ]
    }
)
