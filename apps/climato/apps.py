"""Configuration of the 'climato' application."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django_stubs_ext import StrOrPromise


class ClimatoConfig(AppConfig):
    """Class representing 'climato' application and its configuration."""

    label: str = "climato"
    name: str = "climato"
    verbose_name: StrOrPromise = _("Climato")
