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

You need to add a field to your form, adding it to your form schema, as follows::


  from zope.interface import Interface
  from zope import schema


  class IYourForm(Interface):
    ...
    captcha = schema.TextLine(title="ReCaptcha", description=u"", required=False)



You need to set IRecaptchaWidget as widget for this field, as follows::


  from plone.formwidget.recaptcha.widget import ReCaptchaFieldWidget
  from z3c.form import form, fields

  class YourForm(form.Form):
      fields = fields.Fields(IYourForm)
      fields["captcha"].widgetFactory = ReCaptchaFieldWidget


This product registers an automatic validator for all fields in all z3c.forms that use the provided widget
so you don't need to worry about the form validation, this product will handle it for your.

You can see the `demo <https://github.com/plone/plone.formwidget.recaptcha/tree/master/src/plone/formwidget/recaptcha/demo>`_ folder inside the distribution for an example usage.



Supermodel
^^^^^^^^^^
You can add a captcha field in an XML model by adding something like this::

    <field name="captcha" type="plone.formwidget.recaptcha.ReCaptchaWidget">
      <title>Solve Captcha</title>
      <description></description>
    </field>


Upgrade to API v2
-----------------

plone.formwidget.recaptcha 2.* uses V2 of the reCaptcha API.
Users upgrading from plone.formwidget.recaptcha 1.* will therefore need to generate new keys
as global Keys are not supported in the V2 API.

Source Code
-----------

Contributors please read the document `Process for Plone core's development <http://docs.plone.org/develop/plone-coredev/index.html>`_

Sources are at the `Plone code repository hosted at Github <https://github.com/plone/plone.formwidget.recaptcha>`_.
