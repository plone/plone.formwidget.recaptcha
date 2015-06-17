# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName


def install_browserlayer(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        'profile-plone.formwidget.recaptcha:default',
        'browserlayer',
        run_dependencies=False,
        purge_old=False
    )
