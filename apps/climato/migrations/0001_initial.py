# Generated by Django 5.0.4 on 2024-04-08 21:13

import accounts.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Poste",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="When was this object created?",
                        verbose_name="creation date",
                    ),
                ),
                (
                    "changed_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="When was this object last modified?",
                        verbose_name="last modification date",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "num_poste",
                    models.CharField(
                        help_text="numéro Météo-France du poste sur 8 chiffres",
                        max_length=8,
                        verbose_name="numéro",
                    ),
                ),
                (
                    "nom_usuel",
                    models.CharField(
                        help_text="nom usuel du poste",
                        max_length=255,
                        verbose_name="nom",
                    ),
                ),
                (
                    "lat",
                    models.DecimalField(
                        decimal_places=6,
                        help_text="latitude, négative au sud (en degrés et millionièmes de degré)",
                        max_digits=9,
                        verbose_name="latitude",
                    ),
                ),
                (
                    "lon",
                    models.DecimalField(
                        decimal_places=6,
                        help_text="longitude, négative à l’ouest de GREENWICH (en degrés et millionièmes de degré)",
                        max_digits=9,
                        verbose_name="longitude",
                    ),
                ),
                (
                    "alti",
                    models.IntegerField(
                        help_text="altitude du pied de l'abri ou du pluviomètre si pas d'abri (en m)",
                        verbose_name="altitude",
                    ),
                ),
                (
                    "changed_by",
                    models.ForeignKey(
                        help_text="Who last modified this object?",
                        limit_choices_to={"is_active": True},
                        on_delete=models.SET(accounts.models.get_sentinel_user),
                        related_name="%(app_label)s_%(class)ss_as_changed_by",
                        related_query_name="%(app_label)s_%(class)s_as_changed_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="last editor",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="The creator of this very object.",
                        limit_choices_to={"is_active": True},
                        on_delete=models.SET(accounts.models.get_sentinel_user),
                        related_name="%(app_label)s_%(class)ss_as_owner",
                        related_query_name="%(app_label)s_%(class)s_as_owner",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="creator",
                    ),
                ),
            ],
            options={
                "verbose_name": "poste",
                "verbose_name_plural": "postes",
                "ordering": ["num_poste"],
                "abstract": False,
            },
        ),
    ]
