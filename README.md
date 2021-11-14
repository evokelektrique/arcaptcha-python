<h1>
  <img src="https://arcaptcha.ir/logo.png" width="80" />
  Arcaptcha
  
  <!-- Badges -->
  <a href="https://github.com/evokelektrique/arcaptcha-python/blob/master/LICENSE">
    <img alt="GitHub" src="https://img.shields.io/github/license/evokelektrique/arcaptcha-python?color=blue&style=flat-square">
  </a>
  <a href="https://pypi.org/project/arcaptcha/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/arcaptcha?style=flat-square">
  </a>
</h1>

Validate and display captcha from Arcaptcha easily in Python. ([PyPI](https://pypi.org/project/arcaptcha/))

## Installation

The package can be installed easily by `pip install arcaptcha` command.

## Usage

```python
# Import the package to the project
from arcaptcha import Arcaptcha

# Create a new instance of Captcha object
captcha = Arcaptcha.Captcha(site_key = "my_site_key", secret_key = "my_secret_key")

# Verify challenge
>>> captcha.verify(challenge_id = "example_challenge_id")
True

# Display API script tag
>>> captcha.display_tag()
"<script src='https://widget.arcaptcha.ir/1/api.js' async defer></script>"

# Display captcha HTML tag
>>> captcha.display()
"<div class='arcaptcha' data-site-key='my_site_key'></div>"
```
