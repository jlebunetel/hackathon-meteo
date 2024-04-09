"""Register 'climato' actions with 'manage.py'."""

import logging

from climato.models import Mesure, Poste
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Avg, Count, F, Q, RowRange, Subquery, Sum, Window

logger = logging.getLogger(__name__)


def sandbox() -> None:
    critere_1 = Q(rr=10, tn__lte=5)
    critere_2 = Q(tn__lte=4)
    mesures = Mesure.objects.filter(critere_1 | critere_2)

    logger.debug(mesures)
    logger.debug(mesures.count())
    return

    conditions = []

    # pas pluie pendant 7 jours consécutifs
    conditions.append(Q(cumul_5=0))

    # puis 3 jours de pluie forte
    # conditions.append(Q(rr=0))

    q = Q()

    for condition in conditions:
        q |= condition

    poste = Poste.objects.all()[0]
    mesures = poste.mesures.annotate(
        cumul_5=Window(
            expression=Sum("rr"),
            order_by=F("aaaammjj").asc(),
            frame=RowRange(start=-5, end=0),
        )
    ).filter(q)

    logger.info(mesures.count())
    logger.debug(mesures[0].cumul_5)

    return

    for mesure in mesures:
        logger.info(mesure)


class Command(BaseCommand):
    def handle(self, *args: str, **kwargs: int) -> None:
        del args, kwargs
        try:
            sandbox()
        except Exception as error:
            raise CommandError(error) from error
