# -*- coding: utf-8 -*-
"""Installer for the plone.formwidget.recaptcha package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="plone.formwidget.recaptcha",
    version="2.3.1.dev0",
    description="ReCaptcha widget for Plone.",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="plone discussion plone.app.discussion spam captcha recaptcha",
    author="Timo Stollenwerk - Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://github.com/collective/plone.formwidget.recaptcha",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/plone.formwidget.recaptcha",
        "Source": "https://github.com/plone/plone.formwidget.recaptcha",
        "Tracker": "https://github.com/plone/plone.formwidget.recaptcha/issues",
        # 'Documentation': 'https://plone.formwidget.recaptcha.readthedocs.io/en/latest/',
    },
    license="GPLv2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["plone", "plone.formwidget"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=2.7",
    install_requires=[
        "plone.app.registry",
        "plone.registry",
        "Products.CMFCore",
        "setuptools",
        "z3c.form",
        "zope.annotation",
        "zope.component",
        "zope.i18nmessageid ",
        "zope.interface",
        "zope.publisher",
        "zope.schema",
        "Zope2",
    ],
    extras_require={
        "test": [
            "plone.api",
            "plone.app.testing",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
