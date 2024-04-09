"""Model definitions for the 'climato' application."""

import logging
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


class Poste(models.Model):
    """Class to represent a Poste."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    num_poste = models.CharField(
        max_length=8,
        verbose_name="numéro",
        help_text="numéro Météo-France du poste sur 8 chiffres",
    )

    nom_usuel = models.CharField(
        max_length=255,
        verbose_name="nom",
        help_text="nom usuel du poste",
    )

    lat = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name="latitude",
        help_text="latitude, négative au sud (en degrés et millionièmes de degré)",
    )

    lon = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name="longitude",
        help_text="longitude, négative à l’ouest de GREENWICH (en degrés et "
        "millionièmes de degré)",
    )

    alti = models.IntegerField(
        verbose_name="altitude",
        help_text="altitude du pied de l'abri ou du pluviomètre si pas d'abri (en m)",
    )

    class Meta:
        """Metadata options class."""

        ordering: list[str] = ["num_poste"]
        verbose_name = _("poste")
        verbose_name_plural = _("postes")

    def __repr__(self) -> str:
        """Returns an unambiguous description of the model (for developers)."""
        return f"<{self.__class__.__name__} object ({self.pk})>"

    def __str__(self) -> str:
        """Returns a description of the model (for customers)."""
        return f"{self.nom_usuel} ({self.num_poste})"


class Mesure(models.Model):
    """Class to represent a Mesure."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    poste = models.ForeignKey(
        to=Poste,
        # Allow deleting the Poste
        # only if all Mesure instances are deleted first:
        on_delete=models.PROTECT,
        related_name="mesures",
        related_query_name="mesure",
        verbose_name="poste",
    )

    aaaammjj = models.DateField(
        verbose_name="date",
        help_text="date de la mesure (année mois jour)",
    )

    rr = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        verbose_name="précipitation",
        help_text="quantité de précipitation tombée en 24 heures (de 06h FU le jour J "
        "à 06h FU le jour J+1). La valeur relevée à J+1 est affectée au jour J (en mm "
        "et 1/10)",
    )

    tn = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name="température minimale",
        help_text="température minimale sous abri (en °C et 1/10)",
    )

    tx = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name="température maximale",
        help_text="température maximale sous abri (en °C et 1/10)",
    )

    tm = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        verbose_name="température moyenne",
        help_text="moyenne quotidienne des températures horaires sous abri (en °C et 1/10)",
    )

    ffm = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        verbose_name="vent moyen",
        help_text="moyenne quotidienne de la force du vent moyenné sur 10 mn, à 10 m (en m/s et 1/10)",
    )

    class Meta:
        """Metadata options class."""

        ordering: list[str] = ["-aaaammjj"]
        verbose_name = _("mesure")
        verbose_name_plural = _("mesures")

    def __repr__(self) -> str:
        """Returns an unambiguous description of the model (for developers)."""
        return f"<{self.__class__.__name__} object ({self.pk})>"

    def __str__(self) -> str:
        """Returns a description of the model (for customers)."""
        return f"{self.aaaammjj} ({self.poste})"
