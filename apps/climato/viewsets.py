"""ViewSets definitions for the 'climato' application."""

import logging
from datetime import timedelta

from climato.models import Mesure, Poste
from climato.serializers import CriteriaSerializer, MesureSerializer, PosteSerializer
from climato.utils.mm import MeteoMatch, translate
from django.db.models import Q
from django_filters.rest_framework import FilterSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

logger = logging.getLogger(__name__)


class MesureFilterSet(FilterSet):
    """FilterSet definition for 'Mesure' model."""

    class Meta:
        """Metadata options class."""

        model = Mesure

        fields = {
            "poste": ["exact"],
            "aaaammjj": ["exact", "lte", "gte", "range"],
            "rr": ["exact", "lte", "gte", "range"],
            "tn": ["exact", "lte", "gte", "range"],
            "tx": ["exact", "lte", "gte", "range"],
            "tm": ["exact", "lte", "gte", "range"],
            "ffm": ["exact", "lte", "gte", "range"],
        }


class MesureViewSet(ReadOnlyModelViewSet):  # pylint: disable=too-many-ancestors
    """ViewSet definition for 'Mesure' model."""

    queryset = Mesure.objects.all()

    serializer_class = MesureSerializer

    filterset_class = MesureFilterSet

    search_fields = ["aaaammjj"]

    @action(detail=False, methods=["post"], serializer_class=CriteriaSerializer)
    def post_criteria(self, request):
        logger.debug(request.POST)
        criteria = request.POST.get("criteria")

        mm: MeteoMatch = translate(criteria)
        queryset = Mesure.objects.filter(poste__num_poste=mm.id)

        for contrainte_temp in mm.contraintes_temp:
            logger.debug(contrainte_temp)

            critere_1 = Q(tn__lte=-4)
            queryset = queryset.filter(critere_1)

        payload: list[list[Mesure]] = []

        for match in queryset:
            end_date = match.aaaammjj
            start_date = end_date - timedelta(days=3)
            sub_queryset = Mesure.objects.filter(
                poste=match.poste, aaaammjj__range=[start_date, end_date]
            )
            serializer = MesureSerializer(
                sub_queryset, many=True, context={"request": request}
            )
            payload.append(serializer.data)

        return Response(payload)


class PosteViewSet(ReadOnlyModelViewSet):  # pylint: disable=too-many-ancestors
    """ViewSet definition for 'Poste' model."""

    queryset = Poste.objects.all()

    serializer_class = PosteSerializer

    search_fields = ["num_poste", "nom_usuel"]
