Changelog
=========

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
