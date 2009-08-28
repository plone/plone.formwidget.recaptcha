from Products.Five.browser import BrowserView

from zope.component import queryUtility

from plone.registry.interfaces import IRegistry

from plone.app.registry.browser import controlpanel

from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings, _

class ReCaptchaSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IReCaptchaSettings
    label = _(u"ReCaptcha settings")
    description = _(u"""In order to use ReCaptcha on your Plone site, you need
                        an account on http://recaptcha.net. Go to
                        http://recaptcha.net/whyrecaptcha.html to create an
                        account and to receive your private and public key.

                        If you don't want to rely on an external service for
                        captcha, you might consider to use
                        plone.formwidget.captcha instead.
                        """)

    def updateFields(self):
        super(ReCaptchaSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(ReCaptchaSettingsEditForm, self).updateWidgets()

class ReCaptchaSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = ReCaptchaSettingsEditForm
