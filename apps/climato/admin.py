"""Configuration of the 'climato' application administration site."""

import logging

from climato.models import Mesure, Poste
from django.contrib import admin

logger = logging.getLogger(__name__)


class PosteAdmin(admin.ModelAdmin):
    """Encapsulate all admin options and functionality for the model 'Poste'."""

    list_display: list[str] = ["num_poste", "nom_usuel", "lat", "lon", "alti"]


admin.site.register(Poste, PosteAdmin)


class MesureAdmin(admin.ModelAdmin):
    """Encapsulate all admin options and functionality for the model 'Mesure'."""

    list_display: list[str] = ["aaaammjj", "poste", "rr", "tn", "tx", "tm", "ffm"]

    list_filter: list[str] = ["poste"]


admin.site.register(Mesure, MesureAdmin)
