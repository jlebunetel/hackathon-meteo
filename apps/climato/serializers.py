"""Serializers definitions for the 'climato' application."""

from climato.models import Mesure, Poste
from rest_framework import serializers


class CriteriaSerializer(serializers.Serializer):
    criteria = serializers.CharField(max_length=2048)


class MesureSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer definition for 'Mesure' model."""

    class Meta:
        """Metadata options class."""

        model = Mesure

        fields = "__all__"

        extra_kwargs = {
            "url": {
                "view_name": "climato_api:mesures-detail",
                "lookup_field": "pk",
            },
            "poste": {
                "view_name": "climato_api:postes-detail",
                "lookup_field": "pk",
            },
        }


class PosteSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer definition for 'Poste' model."""

    class Meta:
        """Metadata options class."""

        model = Poste

        fields = "__all__"

        extra_kwargs = {
            "url": {
                "view_name": "climato_api:postes-detail",
                "lookup_field": "pk",
            },
        }
