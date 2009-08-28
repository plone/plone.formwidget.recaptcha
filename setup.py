from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plone.formwidget.recaptcha',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Timo Stollenwerk',
      author_email='timo@zmag.de',
      url='http://svn.plone.org/svn/plone/plone.formwidget.recaptcha',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.z3cform',
          'plone.registry',
          'plone.app.registry',
          'recaptcha-client != 1.0.4',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
