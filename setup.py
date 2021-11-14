from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Python package for Arcaptcha'
LONG_DESCRIPTION = 'Validate and display captcha for Arcaptcha'

# Setting up
setup(
  # the name must match the folder name 'verysimplemodule'
  name="arcaptcha",
  version=VERSION,
  author="EVOKE",
  author_email="evoke.lektrique@gmail.com",
  description=DESCRIPTION,
  long_description=LONG_DESCRIPTION,
  packages=find_packages(),
  install_requires=["requests"],
  keywords=['captcha', 'api'],
)
