from plone import api
from plone.formwidget.recaptcha.i18n import _
from plone.formwidget.recaptcha.interfaces import IReCaptchaWidget
from z3c.form import validator
from z3c.form.interfaces import NOT_CHANGED
from zope.globalrequest import getRequest
from zope.interface import Invalid
from zope.schema import ValidationError

import logging
import zope.schema.interfaces


logger = logging.getLogger(__name__)


class WrongCaptchaCode(ValidationError):
    __doc__ = _("The code you entered was wrong, please enter the new one.")


class RecaptchaFormValidator(validator.SimpleFieldValidator):
    """validator for z3c.form based forms.
    it will be registered for all fields that are using
    the recaptcha widget provided by this addon
    """

    def validate(self, value):
        if not value:
            value = self.request.get("g-recaptcha-response")

        if value is NOT_CHANGED:
            return

        captcha_view = api.content.get_view(
            name="recaptcha", context=self.context, request=getRequest()
        )
        if not captcha_view.verify():
            logger.error("Captcha validation error")
            raise Invalid(_("Captcha validation is incorrect. Try again please."))
        else:
            logger.info("Captcha validation OK")
        return True


validator.WidgetValidatorDiscriminators(
    RecaptchaFormValidator,
    field=zope.schema.interfaces.IField,
    widget=IReCaptchaWidget,
)
