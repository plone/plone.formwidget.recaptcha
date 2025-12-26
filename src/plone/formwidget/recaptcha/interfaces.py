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

    display_theme = schema.Choice(
        title=_("Theme"),
        description=_("The color theme of the widget."),
        required=True,
        default="light",
        vocabulary=display_themes,
    )

    display_type = schema.Choice(
        title=_("Type"),
        description=_("The type of CAPTCHA to serve."),
        required=True,
        default="image",
        vocabulary=display_types,
    )

    display_size = schema.Choice(
        title=_("Size"),
        description=_("The size of the widget."),
        required=True,
        default="normal",
        vocabulary=display_sizes,
    )

    api_version = schema.Choice(
        title=_("API Version"),
        description=_("Select the reCAPTCHA API version to use (v2 or v3)."),
        required=True,
        default="v2",
        vocabulary=SimpleVocabulary(
            [
                SimpleTerm(value="v2", title=_("v2")),
                SimpleTerm(value="v3", title=_("v3")),
            ]
        ),
    )

    v3_score_threshold = schema.Float(
        title=_("Score Threshold (v3)"),
        description=_("Minimum score for v3 validation (0.0 - 1.0). Recommended: 0.5"),
        required=False,
        default=0.5,
    )
