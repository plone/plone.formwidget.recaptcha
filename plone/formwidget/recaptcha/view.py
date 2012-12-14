from Products.Five import BrowserView

from zope import schema

from zope.annotation import factory
from zope.component import adapts, queryMultiAdapter, queryUtility
from zope.interface import Interface, implements
from zope.publisher.interfaces.browser import IBrowserRequest

from recaptcha.client.captcha import displayhtml, submit

from plone.registry.interfaces import IRegistry

from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings

class IRecaptchaInfo(Interface):
    error = schema.TextLine()
    verified = schema.Bool()

class RecaptchaInfoAnnotation(object):
    implements(IRecaptchaInfo)
    adapts(IBrowserRequest)
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
        portal_state = queryMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        if portal_state is not None:
            lang = portal_state.language()[:2]
        else:
            lang = 'en'
        options = """
        <script>
        var RecaptchaOptions = {
            lang: '%s'
        };
        </script>
        """ % lang

        if not self.settings.public_key:
            raise ValueError, 'No recaptcha public key configured. Go to path/to/site/@@recaptcha-settings to configure.'
        use_ssl = self.request['SERVER_URL'].startswith('https://')
        error = IRecaptchaInfo(self.request).error
        return options + displayhtml(self.settings.public_key, use_ssl=use_ssl, error=error)

    def ajax_widget(self):
        portal_state = queryMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        if portal_state is not None:
            lang = portal_state.language()[:2]
        else:
            lang = 'en'

        if not self.settings.public_key:
            raise ValueError, 'No recaptcha public key configured. Go to path/to/site/@@recaptcha-settings to configure.'
        
        rc_html = """
        <div id="recaptcha_div" data-key="%(PublicKey)s" 
             data-theme="blackglass" data-lang="%(Lang)s"></div>""" % {
                'PublicKey' : self.settings.public_key,
                'Lang': lang
              }
        return rc_html

    def audio_url(self):
        return None

    def verify(self, input=None):
        info = IRecaptchaInfo(self.request)
        if info.verified:
            return True

        if not self.settings.private_key:
            raise ValueError, 'No recaptcha private key configured. Go to path/to/site/@@recaptcha-settings to configure.'
        challenge_field = self.request.get('recaptcha_challenge_field')
        response_field = self.request.get('recaptcha_response_field')
        remote_addr = self.request.get('HTTP_X_FORWARDED_FOR', '').split(',')[0]
        if not remote_addr:
            remote_addr = self.request.get('REMOTE_ADDR')
        res = submit(challenge_field, response_field, self.settings.private_key, remote_addr)
        if res.error_code:
            info.error = res.error_code

        info.verified = res.is_valid
        return res.is_valid

    @property
    def external(self):
        return True
