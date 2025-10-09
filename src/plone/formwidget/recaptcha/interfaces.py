# -*- coding: utf-8 -*-
from plone.formwidget.recaptcha.i18n import _
from z3c.form import interfaces
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


display_themes = SimpleVocabulary(
    [
        SimpleTerm(value="light", title=_("light")),
        SimpleTerm(value="dark", title=_("dark")),
    ]
)
display_types = SimpleVocabulary(
    [
        SimpleTerm(value="image", title=_("image")),
        SimpleTerm(value="audio", title=_("audio")),
    ]
)
display_sizes = SimpleVocabulary(
    [
        SimpleTerm(value="normal", title=_("normal")),
        SimpleTerm(value="compact", title=_("compact")),
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
        title=_("Public Key"), description=_(""), required=True, default=""
    )

    private_key = schema.TextLine(
        title=_("Private Key"), description=_(""), required=True, default=""
    )

    v3_score_threshold = schema.Float(
        title=_(
            "Score threshold",
        ),
        description=_(
            "reCAPTCHA v3 returns a score (1.0 is very likely a good interaction, 0.0 is very likely a bot)"
            "Enter here the value below which the values will be considered spam.",
        ),
        default=0.5,
        required=True,
        readonly=False,
    )
