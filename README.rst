Introduction
============

plone.formwidget.recaptcha is a ``z3c.form`` ReCaptcha widget for use with Plone.

It is a z3c.form re-implementation of the `collective.recaptcha`_ package original written by David Glick.

.. _collective.recaptcha: http://plone.org/products/collective.recaptcha


Buildout Installation
---------------------

Add the following code to your buildout.cfg to install plone.formwidget.recaptcha::

    [buildout]
    ...

    [instance]
    ...
    eggs =
        ...
        plone.formwidget.recaptcha
        ...


ReCaptcha setup
---------------

There is a control panel at ``http://path/to/site/@@recaptcha-settings`` to configure the Addon.
Google provides a set of test keys, that can be used to try out the recaptcha form
and documentation at https://developers.google.com/recaptcha/docs/faq.

``Site key: 6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI``

``Secret key: 6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe``

To actually use the service, you must obtain a site key and secret key from
`developers.google.com/recaptcha <https://developers.google.com/recaptcha/>`_

Usage
-----
See the `demo <https://github.com/plone/plone.formwidget.recaptcha/tree/master/src/plone/formwidget/recaptcha/demo>`_ folder inside the distribution for an example usage.

Upgrade to API v2
-----------------

plone.formwidget.recaptcha 2.* uses V2 of the reCaptcha API.
Users upgrading from plone.formwidget.recaptcha 1.* will therefore need to generate new keys
as global Keys are not supported in the V2 API.

Source Code
-----------

Contributors please read the document `Process for Plone core's development <http://docs.plone.org/develop/plone-coredev/index.html>`_

Sources are at the `Plone code repository hosted at Github <https://github.com/plone/plone.formwidget.recaptcha>`_.
