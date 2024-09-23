"""Setup tests for this package."""

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.formwidget.recaptcha.testing import (
    PLONE_FORMWIDGET_RECAPTCHA_INTEGRATION_TESTING,
)

import plone.api
import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that plone.formwidget.recaptcha is properly installed."""

    layer = PLONE_FORMWIDGET_RECAPTCHA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = plone.api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if plone.formwidget.recaptcha is installed."""
        self.assertTrue(
            self.installer.is_product_installed("plone.formwidget.recaptcha")
        )

    def test_browserlayer(self):
        """Test that IReCaptchaLayer is registered."""
        from plone.browserlayer import utils
        from plone.formwidget.recaptcha.interfaces import IReCaptchaLayer

        self.assertIn(IReCaptchaLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONE_FORMWIDGET_RECAPTCHA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = plone.api.portal.get_tool("portal_quickinstaller")
        roles_before = plone.api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("plone.formwidget.recaptcha")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plone.formwidget.recaptcha is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("plone.formwidget.recaptcha")
        )

    def test_browserlayer_removed(self):
        """Test that IReCaptchaLayer is removed."""
        from plone.browserlayer import utils
        from plone.formwidget.recaptcha.interfaces import IReCaptchaLayer

        self.assertNotIn(IReCaptchaLayer, utils.registered_layers())
