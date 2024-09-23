# -*- coding: utf-8 -*-
from plone.formwidget.recaptcha.i18n import _
from z3c.form import interfaces
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


display_themes = SimpleVocabulary(
    [
        SimpleTerm(value=u"light", title=_(u"light")),
        SimpleTerm(value=u"dark", title=_(u"dark")),
    ]
)
display_types = SimpleVocabulary(
    [
        SimpleTerm(value=u"image", title=_(u"image")),
        SimpleTerm(value=u"audio", title=_(u"audio")),
    ]
)
display_sizes = SimpleVocabulary(
    [
        SimpleTerm(value=u"normal", title=_(u"normal")),
        SimpleTerm(value=u"compact", title=_(u"compact")),
    ]
)


class IReCaptchaLayer(Interface):
    """Browser layer for plone.formwdiget.recaptcha"""


class IReCaptchaWidget(interfaces.IWidget):
    """Marker interface for the ReCaptcha widget"""


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
        title=_("Site Key"), description=_(u""), required=True, default=u""
    )

    private_key = schema.TextLine(
        title=_("Secret Key"), description=_(u""), required=True, default=u""
    )

