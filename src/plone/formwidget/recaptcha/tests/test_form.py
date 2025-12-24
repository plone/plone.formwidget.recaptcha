from plone import api
from plone.formwidget.recaptcha.testing import (
    PLONE_FORMWIDGET_RECAPTCHA_FUNCTIONAL_TESTING,
)
from zope.testbrowser.browser import Browser

import transaction
import unittest


class TestFormV2(unittest.TestCase):

    layer = PLONE_FORMWIDGET_RECAPTCHA_FUNCTIONAL_TESTING

    def setUp(self):
        self.browser = Browser()
        self.portal = self.layer["portal"]
        self.portal_url = self.portal.absolute_url()
        api.portal.set_registry_record(
            "plone.formwidget.recaptcha.interfaces.IReCaptchaSettings.public_key",
            "some-public-key",
        )
        api.portal.set_registry_record(
            "plone.formwidget.recaptcha.interfaces.IReCaptchaSettings.private_key",
            "some-private-key",
        )
        api.portal.set_registry_record(
            "plone.formwidget.recaptcha.interfaces.IReCaptchaSettings.api_version", "v2"
        )

        transaction.commit()

    def test_form_renders_captcha(self):
        """render the test form and check for keywords"""
        self.browser.open(f"{self.portal_url}/@@recaptcha_form")
        self.assertIn("https://www.google.com/recaptcha/api.js", self.browser.contents)
        self.assertIn('data-sitekey="some-public-key"', self.browser.contents)


class TestFormV3(unittest.TestCase):

    layer = PLONE_FORMWIDGET_RECAPTCHA_FUNCTIONAL_TESTING

    def setUp(self):
        self.browser = Browser()
        self.portal = self.layer["portal"]
        self.portal_url = self.portal.absolute_url()
        api.portal.set_registry_record(
            "plone.formwidget.recaptcha.interfaces.IReCaptchaSettings.public_key",
            "some-public-key",
        )
        api.portal.set_registry_record(
            "plone.formwidget.recaptcha.interfaces.IReCaptchaSettings.private_key",
            "some-private-key",
        )
        api.portal.set_registry_record(
            "plone.formwidget.recaptcha.interfaces.IReCaptchaSettings.api_version", "v3"
        )
        api.portal.set_registry_record(
            "plone.formwidget.recaptcha.interfaces.IReCaptchaSettings.v3_score_threshold",
            0.5,
        )
        transaction.commit()

    def test_form_renders_captcha(self):
        """render the test form and check for keywords"""
        self.browser.open(f"{self.portal_url}/@@recaptcha_form")
        self.assertIn("https://www.google.com/recaptcha/api.js", self.browser.contents)
        self.assertIn("grecaptcha.execute('some-public-key'", self.browser.contents)
