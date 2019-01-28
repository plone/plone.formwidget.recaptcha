# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings
from plone.formwidget.recaptcha.interfaces import _


class ReCaptchaSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IReCaptchaSettings
    label = _(u"ReCaptcha settings")
    description = _(
        u'In order to use ReCaptcha on your Plone site, go to '
        u'https://developers.google.com/recaptcha/ to create an account and to '
        u'receive your private and public key. Then configure them at '
        u'http://path/to/site/@@recaptcha-settings. If you don\'t want to '
        u'rely on an external service for captcha, you might want to consider '
        u'using plone.formwidget.captcha instead.'
    )

    def updateFields(self):
        super(ReCaptchaSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(ReCaptchaSettingsEditForm, self).updateWidgets()


class ReCaptchaSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = ReCaptchaSettingsEditForm
