# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '2.0a3'

description = open("README.rst").read() + "\n"
description += open("CHANGES.rst").read()

setup(
    name='plone.formwidget.recaptcha',
    version=version,
    description="ReCaptcha widget for Plone.",
    long_description=description,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone discussion plone.app.discussion spam captcha recaptcha',
    author='Timo Stollenwerk - Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='http://pypi.python.org/pypi/plone.formwidget.recaptcha',
    license='GPL',
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
