Introduction
============

plone.formwidget.recaptcha is a z3c.form ReCaptcha widget for use with Plone.
It is a z3c.form re-implementation of the `collective.recaptcha`_ package written by
David Glick.

.. _collective.recaptcha: http://plone.org/products/collective.recaptcha


Buildout Installation
---------------------

Add the following code to your buildout.cfg to install plone.formwidget.recaptcha::

    [buildout]
    ...
    eggs =
        ...
        plone.formwidget.recaptcha
        ...

    ...
    [instance]
    ...
    zcml =
        ...
        plone.formwidget.recaptcha
    ...


ReCaptcha setup
---------------

Before the service will work, you must obtain a public and private key from
https://developers.google.com/recaptcha/, and configure them at http://path/to/site/@@recaptcha-settings


Upgrade to API v2
-----------------

Upgrading to plone.formwidget.recaptcha 2.* (reCaptcha API V2) you need double check your keys
because global Keys are not supported in the V2 API, so you need to create a new key
if you wish to use the V2 API.


