from Acquisition import aq_inner

from z3c.form import validator

from z3c.form.interfaces import IValidator

from zope.component import getMultiAdapter, provideAdapter

from zope.schema import ValidationError

from plone.formwidget.recaptcha import ReCaptchaMessageFactory as _

class WrongCaptchaCode(ValidationError):
    __doc__ = _("""The code you entered was wrong, please enter the new one.""")

class ReCaptchaValidator(validator.SimpleFieldValidator):

    def validate(self, value):
        super(ReCaptchaValidator, self).validate(value)
        captcha = getMultiAdapter((aq_inner(self.context), self.request), name='captcha')

        if not captcha.verify():
            raise WrongCaptchaCode
        else:
            return True
