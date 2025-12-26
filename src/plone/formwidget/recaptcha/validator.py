from Acquisition import aq_inner
from plone.formwidget.recaptcha.i18n import _
from z3c.form import validator
from zope.component import getMultiAdapter
from zope.schema import ValidationError


class WrongCaptchaCode(ValidationError):
    __doc__ = _("The code you entered was wrong, please enter the new one.")


class ReCaptchaValidator(validator.SimpleFieldValidator):
    def validate(self, value):
        super().validate(value)
        captcha = getMultiAdapter(
            (aq_inner(self.context), self.request), name="recaptcha"
        )
        if not captcha.verify():
            raise WrongCaptchaCode
        return True
