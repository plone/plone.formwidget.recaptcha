# -*- coding: utf-8 -*-
from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings
from plone.formwidget.recaptcha.norecaptcha import displayhtml
from plone.formwidget.recaptcha.norecaptcha import displayhtml_v3
from plone.formwidget.recaptcha.norecaptcha import submit
from plone.formwidget.recaptcha.norecaptcha import submit_v3
from plone.registry.interfaces import IRegistry
from Products.Five import BrowserView
from zope import schema
from zope.annotation import factory
from zope.component import adapter
from zope.component import queryUtility
from zope.component.hooks import getSite
from zope.interface import implementer
from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserRequest


class IRecaptchaInfo(Interface):
    error = schema.TextLine()
    verified = schema.Bool()


@adapter(IBrowserRequest)
@implementer(IRecaptchaInfo)
class RecaptchaInfoAnnotation(object):
    def __init__(self):
        self.error = None
        self.verified = False


RecaptchaInfo = factory(RecaptchaInfoAnnotation)


class RecaptchaView(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        registry = queryUtility(IRegistry)
        self.settings = registry.forInterface(IReCaptchaSettings)
        self.api_version = getattr(self.settings, "api_version", "v2")

    def image_tag(self):

        # Common error message template
        def get_config_error_message(version_suffix=""):
            return 'No recaptcha{0} public key configured. Go to <a href="{1}/@@recaptcha-settings" target=_blank>Recaptcha Settings</a> to configure.'.format(
                version_suffix, getSite().absolute_url()
            )

        if self.api_version == "v3":
            if not self.settings.public_key:
                return get_config_error_message(" v3")

            action = self.request.get("recaptcha_action", "homepage")
            return displayhtml_v3(self.settings.public_key, action=action)

        else:
            if not self.settings.public_key:
                return get_config_error_message()

            lang = self.request.get("LANGUAGE", "en")
            return displayhtml(
                self.settings.public_key,
                language=lang,
                theme=self.settings.display_theme,
                d_type=self.settings.display_type,
                size=self.settings.display_size,
            )

    def audio_url(self):
        return None

    def verify(self, input=None):

        # Do not validate recaptcha on form inline validation.
        # This automatically makes the next request (form submit) already
        # invalid. This usually happens if the captcha is not the last field
        # on a form.
        if self.request.URL.endswith("z3cform_validate_field"):
            return

        info = IRecaptchaInfo(self.request)
        if info.verified:
            return True

        if not self.settings.private_key:
            raise ValueError(
                "No recaptcha private key configured. Go to "
                "path/to/site/@@recaptcha-settings to configure."
            )
        response_field = self.request.get("g-recaptcha-response")
        remote_addr = self.request.get("HTTP_X_FORWARDED_FOR", "").split(",")[0]
        if not remote_addr:
            remote_addr = self.request.get("REMOTE_ADDR")
        res = (
            submit(response_field, self.settings.private_key, remote_addr)
            if self.api_version == "v2"
            else submit_v3(
                response_field,
                self.settings.private_key,
                remoteip=remote_addr,
                action=self.request.get("recaptcha_action", "homepage"),
                min_score=self.settings.v3_score_threshold,
            )
        )
        if res.error_code:
            info.error = res.error_code

        info.verified = res.is_valid
        return res.is_valid

    @property
    def external(self):
        return True
