# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '2.1.0'

description = open("README.rst").read() + "\n"
description += open("CHANGES.rst").read()

setup(
    name='plone.formwidget.recaptcha',
    version=version,
    description="ReCaptcha widget for Plone.",
    long_description=description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone discussion plone.app.discussion spam captcha recaptcha',
    author='Timo Stollenwerk - Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/plone/plone.formwidget.recaptcha',
    license='GPLv2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['plone', 'plone.formwidget'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'norecaptcha>=0.3',
        'plone.app.registry',
        'plone.registry',
        'Products.CMFCore',
        'setuptools',
        'z3c.form',
        'zope.annotation',
        'zope.component',
        'zope.i18nmessageid ',
        'zope.interface',
        'zope.publisher',
        'zope.schema',
        'Zope2',
    ],
    extras_require={
        'test': [
            'interlude',
            'plone.app.testing',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
