# -*- coding: utf-8 -*-
from plone.formwidget.recaptcha.interfaces import IReCaptchaLayer
from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface


_ = MessageFactory("plone.formwidget.recaptcha")


@adapter(Interface, IReCaptchaLayer)
class ReCaptchaConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IReCaptchaSettings
    configlet_id = "recaptcha"
    configlet_category_id = "Products"
    title = _("ReCaptcha Control Panel")
    group = ""
    schema_prefix = "plone.formwidget.recaptcha.interfaces.IReCaptchaSettings"
