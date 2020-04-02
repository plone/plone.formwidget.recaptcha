# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone.formwidget.recaptcha.widget import ReCaptchaFieldWidget
from plone.z3cform.layout import wrap_form
from z3c.form import button
from z3c.form import field
from z3c.form import form
from zope import interface
from zope import schema
from zope.component import getMultiAdapter

import logging


logger = logging.getLogger(__name__)


class IReCaptchaForm(interface.Interface):
    subject = schema.TextLine(title=u"Subject", description=u"", required=True)

    captcha = schema.TextLine(title=u"ReCaptcha", description=u"", required=False)


class ReCaptcha(object):
    subject = u""
    captcha = u""

    def __init__(self, context):
        self.context = context


class BaseForm(form.Form):
    """ example captcha form """

    fields = field.Fields(IReCaptchaForm)
    fields["captcha"].widgetFactory = ReCaptchaFieldWidget

    @button.buttonAndHandler(u"Save")
    def handleApply(self, action):
        data, errors = self.extractData()
        captcha = getMultiAdapter(
            (aq_inner(self.context), self.request), name="recaptcha"
        )
        if captcha.verify():
            logger.info("ReCaptcha validation passed.")
        else:
            logger.info("The code you entered was wrong, please enter the new one.")
        return


ReCaptchaForm = wrap_form(BaseForm)
