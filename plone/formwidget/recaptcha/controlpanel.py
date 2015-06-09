# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings
from plone.formwidget.recaptcha.interfaces import _


class ReCaptchaSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IReCaptchaSettings
    label = _(u"ReCaptcha settings")
    description = _(
        u'In order to use ReCaptcha on your Plone site, you need an account '
        u'on http://recaptcha.net. Go to '
        u'http://recaptcha.net/whyrecaptcha.html to create an  account and to '
        u'receive your private and public key. If you don\'t want to rely on '
        u'an external service for captcha, you might want to consider using '
        u'plone.formwidget.captcha instead.'
    )

    def updateFields(self):
        super(ReCaptchaSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(ReCaptchaSettingsEditForm, self).updateWidgets()


class ReCaptchaSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = ReCaptchaSettingsEditForm
