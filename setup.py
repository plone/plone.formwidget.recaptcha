from setuptools import setup, find_packages

version = '1.0b3'

setup(name='plone.formwidget.recaptcha',
      version=version,
      description="ReCaptcha widget for Plone.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(), 
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Timo Stollenwerk - Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.formwidget.recaptcha',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.z3cform',
          'plone.registry',
          'plone.app.registry',
          'recaptcha-client != 1.0.4',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
