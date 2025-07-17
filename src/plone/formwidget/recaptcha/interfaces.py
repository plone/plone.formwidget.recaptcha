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
        title=_(u"Public Key"), description=_(u""), required=True, default=u""
    )

    private_key = schema.TextLine(
        title=_(u"Private Key"), description=_(u""), required=True, default=u""
    )

    display_theme = schema.Choice(
        title=_(u"Theme"),
        description=_(u"The color theme of the widget."),
        required=True,
        default=u"light",
        vocabulary=display_themes,
    )

    display_type = schema.Choice(
        title=_(u"Type"),
        description=_(u"The type of CAPTCHA to serve."),
        required=True,
        default=u"image",
        vocabulary=display_types,
    )

    display_size = schema.Choice(
        title=_(u"Size"),
        description=_(u"The size of the widget."),
        required=True,
        default=u"normal",
        vocabulary=display_sizes,
    )

    api_version = schema.Choice(
        title=_(u"API Version"),
        description=_(u"Select the reCAPTCHA API version to use (v2 or v3)."),
        required=True,
        default=u"v2",
        vocabulary=SimpleVocabulary([
            SimpleTerm(value=u"v2", title=_(u"v2")),
            SimpleTerm(value=u"v3", title=_(u"v3")),
        ]),
    )

    public_key_v3 = schema.TextLine(
        title=_(u"Public Key (v3)"),
        description=_(u"Google reCAPTCHA v3 site key."),
        required=False,
        default=u"",
    )

    private_key_v3 = schema.TextLine(
        title=_(u"Private Key (v3)"),
        description=_(u"Google reCAPTCHA v3 secret key."),
        required=False,
        default=u"",
    )

    v3_score_threshold = schema.Float(
        title=_(u"Score Threshold (v3)"),
        description=_(u"Minimum score for v3 validation (0.0 - 1.0). Recommended: 0.5"),
        required=False,
        default=0.5,
    )
