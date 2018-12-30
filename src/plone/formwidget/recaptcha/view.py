# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from norecaptcha.captcha import displayhtml, submit
from plone.app.layout.viewlets import ViewletBase
from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings
from plone.registry.interfaces import IRegistry
from zope import schema
from zope.annotation import factory
from zope.annotation.interfaces import IAnnotations
from zope.component import adapter
from zope.component import queryUtility
from zope.interface import Interface
from zope.interface import implementer
from zope.publisher.interfaces.browser import IBrowserRequest

HAS_RECAPTCHA_FIELD_KEY = 'has_recaptcha'


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

    def image_tag(self):
        if not self.settings.public_key:
            raise ValueError(
                'No recaptcha public key configured. Go to '
                'path/to/site/@@recaptcha-settings to configure.'
            )
        lang = self.request.get('LANGUAGE', 'en')
        IAnnotations(self.request)[HAS_RECAPTCHA_FIELD_KEY] = True
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
        info = IRecaptchaInfo(self.request)
        if info.verified:
            return True

        if not self.settings.private_key:
            raise ValueError(
                'No recaptcha private key configured. Go to '
                'path/to/site/@@recaptcha-settings to configure.'
            )
        response_field = self.request.get('g-recaptcha-response')
        remote_addr = self.request.get(
            'HTTP_X_FORWARDED_FOR',
            ''
        ).split(',')[0]
        if not remote_addr:
            remote_addr = self.request.get('REMOTE_ADDR')
        res = submit(response_field, self.settings.private_key, remote_addr)
        if res.error_code:
            info.error = res.error_code

        info.verified = res.is_valid
        return res.is_valid

    @property
    def external(self):
        return True


class HeadViewlet(ViewletBase):
    def available(self):
        return IAnnotations(self.request).get(HAS_RECAPTCHA_FIELD_KEY, False)
