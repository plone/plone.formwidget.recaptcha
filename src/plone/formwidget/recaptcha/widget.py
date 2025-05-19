# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone.formwidget.recaptcha.interfaces import IReCaptchaWidget
from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text
from zope.component import getMultiAdapter
from zope.interface import implementer_only

import zope.component
import zope.interface
import zope.schema.interfaces
from plone import api


@implementer_only(IReCaptchaWidget)
class ReCaptchaWidget(text.TextWidget):

    def public_key(self):
        return api.portal.get_registry_record('plone.formwidget.recaptcha.interfaces.IReCaptchaSettings.public_key')


@zope.component.adapter(zope.schema.interfaces.IField, interfaces.IFormLayer)
@zope.interface.implementer(interfaces.IFieldWidget)
def ReCaptchaFieldWidget(field, request):
    """IFieldWidget factory for CaptchaWidget."""
    return widget.FieldWidget(field, ReCaptchaWidget(request))
