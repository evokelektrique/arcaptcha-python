import json
import requests

class Captcha:
  VERIFY_URL = "https://api.arcaptcha.ir/arcaptcha/api/verify"

  def __init__(self, site_key, secret_key):

    # Validate arguments
    if not site_key or not secret_key:
      raise ValueError("Arguments cannot be empty")

    # Assign arguments
    self.site_key = site_key
    self.secret_key = secret_key

  # Send HTTP request to verification API url and return the status
  def verify(self, challenge_id):
    # Validate argument
    if not challenge_id:
      raise ValueError("challenge_id cannot be empty.")

    # Validate argument type
    if not isinstance(challenge_id, str):
      raise ValueError("challenge_id must be string.")

    payload = {
      "site_key": self.site_key,
      "secret_key": self.secret_key,
      "challenge_id": challenge_id
    }

    # Send POST request to api
    response = requests.post(self.VERIFY_URL, json=payload)

    return self.validate_response(response.content)

  # JSON resposne body validator
  def validate_response(self, response):
    parsed = json.loads(response)

    if "success" in parsed:
      return True

    return False

  # Print captcha HTML tag
  def display(self):
    return "<div class='arcaptcha' data-site-key='" + self.site_key +"'></div>"

  # Print API script tag
  def display_tag(self):
    return "<script src='https://widget.arcaptcha.ir/1/api.js' async defer></script>"
