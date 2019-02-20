Changelog
=========

2.1.0 (2019-02-20)
------------------

- Update TravisCI Setup and test with Plone 5.1 and 5.2 on Python 2.7.
  Also test on Python 3.6+3.7 (allowed to fail, and fails for now).
  [jensens]

- Remove obsolete action icons configuration.
  [thet]

- update controlpanel text
  [lucid-0]

- Remove obsolete ``recaptcha_ajax.js`` - all scripts are integrated via the ``norecaptcha`` package.
  Add upgrade step for that.
  [thet]


2.0.0 (2018-09-05)
------------------

- Add a dummy widget display view which renders empty.
  A widget needs a display view, otherwise form result rendering may fail.
  [thet]


2.0a3 (2016-12-21)
------------------

- Support for use the widget with plone.supermodel
  [jpgimenez]

- Support for widget display settings as described in
  https://developers.google.com/recaptcha/docs/display
  [jensens]


2.0a2 (2015-06-17)
------------------

- Fix: problem with MANIFEST.in and old package structure made 2.0a1 a
  brown bag release. All non-python files (i.e. zcml) were missing.
  [jensens]


2.0a1 (2015-06-17)
------------------

* some pep8/plone conventions code style cleanup.
  [jensens]

* recaptcha API 2 (aka norecaptcha)
  [mamico]

1.0b3 - 2010-11-18
------------------

* Register browser components for a product browser layer so they don't
  leak to sites without this product installed.  Run the upgrade step
  if upgrading on a site that already has this product installed.
  [davisagli]

* Move to plone.app.discussion-captcha feature declaration to meta.zcml.
  [timo]

* Adapt recaptcha view instead of captcha view for validation.
  [ramon]


1.0b2 - 2010-06-02
------------------

* Updated package metadata and marked this as a Plone add-on.
  [timo]

* Declare that plone.formwidget.captcha provides a Captcha field that can be
  used by plone.app.discussion to add a Captcha field to comment forms.
  [timo]


1.0b1 - 2009-12-07
------------------

* z3c.autoinclude.plugin added
  [timo]


1.0a1 - 2009-08-28
------------------

* Initial release
  [timo]
