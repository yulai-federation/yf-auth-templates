"""
App configuration
"""

# Django
from django.apps import AppConfig  # pylint: disable=import-error

from . import __version__


class YfTemplatesConfig(AppConfig):  # pylint: disable=too-few-public-methods
    """
    Template configuration
    """

    name = "yf_templates"
    label = "yf_templates"
    verbose_name = f"Yulai Federation Auth Templates v{__version__}"
