#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()

requirements = [
    'psycopg2==2.5.4',
    'argparse==1.3.0',
]

setup(
    name='odoo_tests_openerp_scripts',
    version='0.1.1',
    description='Test openerp_scripts to be used with Anybox Odoo recipe.',
    long_description=readme,
    author='Sebastien Delisle',
    author_email='seb0del@gmail.com',
    url='https://github.com/maxc0c0s/odoo_tests_openerp_scripts',
    packages=[
        'odoo_tests',
    ],
    package_dir={'odoo_tests':
                 'odoo_tests'},
    include_package_data=True,
    install_requires=requirements,
    license="GNU GPL v3.0",
    zip_safe=False,
    keywords='odoo_tests_openerp_scripts',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Framework :: Buildout :: Extension',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        "console_scripts": [
            "test_odoo = odoo_tests.odoo_tests:main",
            "create_db = odoo_tests.odoo_tests:create_db",
            "drop_db = odoo_tests.odoo_tests:drop_db",
        ]
    }
)
