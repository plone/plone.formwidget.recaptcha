from plone.app.registry.browser import controlpanel
from plone.formwidget.recaptcha.i18n import _
from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings


class ReCaptchaSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IReCaptchaSettings
    label = _("ReCaptcha v2 settings")
    description = _(
        "In order to use ReCaptcha v2 on your Plone site, go to"
        " https://developers.google.com/recaptcha/ to create an account and"
        " to receive your private and public key. Then configure them at"
        " https://host/path/to/site/@@recaptcha-settings. If you don't want"
        " to rely on an external service for captcha, you might want to"
        " consider using plone.formwidget.captcha instead."
    )

    def updateFields(self):
        super().updateFields()

    def updateWidgets(self):
        super().updateWidgets()


class ReCaptchaSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = ReCaptchaSettingsEditForm
