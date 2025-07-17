# -*- coding: utf-8 -*-
# Code taken from external dependency
# https://pypi.org/project/norecaptcha/, which is not
# updated to Python 3
from six.moves.urllib import parse
from six.moves.urllib.request import Request
from six.moves.urllib.request import urlopen

import six

try:
    import json
except ImportError:
    import simplejson as json

VERIFY_SERVER = "www.google.com"


logger = logging.getLogger("plone.formwidget.recaptcha.norecaptcha")


class RecaptchaResponse(object):
    def __init__(self, is_valid, error_code=None, score=None, action=None):
        self.is_valid = is_valid
        self.error_code = error_code
        self.score = score
        self.action = action

    def __repr__(self):
        return "Recaptcha response: {0} {1} score={2} action={3}".format(
            self.is_valid, self.error_code, self.score, self.action
        )

    def __str__(self):
        return self.__repr__()


def _make_verification_request(data, verify_server=VERIFY_SERVER):
    """
    Common function to make verification requests to Google's reCAPTCHA API.
    """
    params = parse.urlencode(data)
    request = Request(
        url="https://{0}/recaptcha/api/siteverify".format(verify_server),
        data=params,
        headers={
            "Content-type": "application/x-www-form-urlencoded",
            "User-agent": "noReCAPTCHA Python",
        },
    )
    if six.PY3:
        request.data = request.data.encode("utf-8")

    httpresp = urlopen(request)
    return_values = json.loads(httpresp.read())
    httpresp.close()

    return return_values


def displayhtml_v3(site_key, action="homepage"):
    """
    Returns HTML/JS for reCAPTCHA v3 integration.
    site_key -- The site key
    action -- The action name for v3 (e.g., 'homepage', 'login', etc.)
    """
    return '''
<script src="https://www.google.com/recaptcha/api.js?render={SiteKey}"></script>
<script>
grecaptcha.ready(function() {{
    grecaptcha.execute('{SiteKey}', {{action: '{Action}'}}).then(function(token) {{
        var recaptchaResponse = document.getElementById('g-recaptcha-response');
        if (recaptchaResponse) {{
            recaptchaResponse.value = token;
        }}
    }});
}});
</script>
<input type="hidden" id="g-recaptcha-response" name="g-recaptcha-response">
'''.format(SiteKey=site_key, Action=action)


def submit_v3(recaptcha_response_field, secret_key, remoteip=None, action=None, min_score=0.5, verify_server=VERIFY_SERVER):
    """
    Verifies reCAPTCHA v3 token.
    recaptcha_response_field -- The token from the client
    secret_key -- your reCAPTCHA secret key
    remoteip -- the user's ip address (optional)
    action -- expected action name (optional)
    min_score -- minimum score to consider valid (default 0.5)
    """
    if not (recaptcha_response_field and len(recaptcha_response_field)):
        return RecaptchaResponse(is_valid=False, error_code="missing-input-response")

    data = {
        "secret": secret_key,
        "response": recaptcha_response_field,
    }
    if remoteip:
        data["remoteip"] = remoteip

    return_values = _make_verification_request(data, verify_server)

    success = return_values.get("success", False)
    score = return_values.get("score")
    returned_action = return_values.get("action")
    error_codes = return_values.get("error-codes", [])

    is_valid = success and (score is not None and score >= min_score)
    if action and returned_action != action:
        is_valid = False
        error_codes.append("action-mismatch")

    return RecaptchaResponse(is_valid=is_valid, error_code=error_codes, score=score, action=returned_action)


def displayhtml(site_key, language="", theme="light", fallback=False, d_type="image", size="normal"):
    """
    Gets the HTML to display for reCAPTCHA

    site_key -- The site key
    language -- The language code for the widget.
    theme -- The color theme of the widget. `light` or `dark`
    fallback -- Old version recaptcha.
    d_type -- The type of CAPTCHA to serve. `image` or `audio`
    size -- The size of the dispalyed CAPTCHA, 'normal' or 'compact'

    For more detail, refer to:
      - https://developers.google.com/recaptcha/docs/display
    """
    return """
<script
  src="https://www.google.com/recaptcha/api.js?hl={LanguageCode}&fallback={Fallback}&"
  async="async" defer="defer"></script>
<div class="g-recaptcha"
    data-sitekey="{SiteKey}"
    data-theme="{Theme}"
    data-type="{Type}"
    data-size="{Size}">
</div>
<noscript>
  <div  style="width: 302px; height: 480px;">
    <div style="width: 302px; height: 422px; position: relative;">
      <div style="width: 302px; height: 422px; position: relative;">
        <iframe
          src="https://www.google.com/recaptcha/api/fallback?k={SiteKey}&hl={LanguageCode}"
          frameborder="0" scrolling="no"
          style="width: 302px; height:422px; border-style: none;">
        </iframe>
      </div>
      <div
        style="border-style: none; bottom: 12px; left: 25px;
               margin: 0px; padding: 0px; right: 25px;
               background: #f9f9f9; border: 1px solid #c1c1c1;
               border-radius: 3px; height: 60px; width: 300px;">
            <textarea
              id="g-recaptcha-response" name="g-recaptcha-response"
              class="g-recaptcha-response"
              style="width: 250px; height: 40px; border: 1px solid #c1c1c1;
                     margin: 10px 25px; padding: 0px; resize: none;"
              value=""></textarea>
      </div>
    </div>
  </div>
</noscript>
""".format(
        LanguageCode=language,
        SiteKey=site_key,
        Theme=theme,
        Type=d_type,
        Size=size,
        Fallback=fallback,
    )


def submit(recaptcha_response_field, secret_key, remoteip, verify_server=VERIFY_SERVER):
    """
    Submits a reCAPTCHA request for verification. Returns RecaptchaResponse
    for the request

    recaptcha_response_field -- The value from the form
    secret_key -- your reCAPTCHA secret key
    remoteip -- the user's ip address
    """
    if not (recaptcha_response_field and len(recaptcha_response_field)):
        return RecaptchaResponse(is_valid=False, error_code="incorrect-captcha-sol")

    def encode_if_necessary(s):
        if isinstance(s, six.text_type):
            return s.encode("utf-8")
        return s

    if six.PY2:
        secret_key = encode_if_necessary(secret_key)
        remoteip = encode_if_necessary(remoteip)
        recaptcha_response_field = encode_if_necessary(
            recaptcha_response_field)

    data = {
        "secret": secret_key,
        "remoteip": remoteip,
        "response": recaptcha_response_field,
    }

    return_values = _make_verification_request(data, verify_server)

    return_code = return_values["success"]
    error_codes = return_values.get("error-codes", [])

    if return_code:
        return RecaptchaResponse(is_valid=True)
    else:
        return RecaptchaResponse(is_valid=False, error_code=error_codes)
