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

In order to use ReCaptcha on your Plone site, you need
an account on `recaptcha.net`_. Go to
`recaptcha.net/whyrecaptcha.html`_ to create an
account and to receive your private and public key.

If you don't want to rely on an external service for
captcha, you might want to consider using
plone.formwidget.captcha instead.

After creating an account, go to the ReCaptcha control panel
(your-site/@@recaptcha-settings) and fill in your personal
ReCaptcha keys.

.. _recaptcha.net: http://recaptcha.net
.. _recaptcha.net/whyrecaptcha.html: http://recaptcha.net/whyrecaptcha.html

