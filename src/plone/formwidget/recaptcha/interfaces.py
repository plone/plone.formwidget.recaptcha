# -*- coding: utf-8 -*-
from z3c.form import interfaces
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface

_ = MessageFactory('plone.formwidget.recaptcha')


class IReCaptchaLayer(Interface):
    """Browser layer for plone.formwdiget.recaptcha"""


class IReCaptchaWidget(interfaces.IWidget):
    """Marker interface for the ReCaptcha widget
    """


class IReCaptchaSettings(Interface):
    """Global discussion settings.

    This describes records stored in the configuration registry and
    obtainable via plone.registry.
    """

    # Todo: Write a short hint, that other discussion related options can
    # be found elsewhere in the Plone control panel:
    #
    # - Types control panel: Allow comments on content types
    # - Search control panel: Show comments in search results

    public_key = schema.TextLine(
        title=_(u"Public Key"),
        description=_(u""),
        required=True,
        default=u""
    )

    private_key = schema.TextLine(
        title=_(u"Private Key"),
        description=_(u""),
        required=True,
        default=u""
    )
