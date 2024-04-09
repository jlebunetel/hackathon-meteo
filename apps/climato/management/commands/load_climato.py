"""Register 'climato' actions with 'manage.py'."""

import csv
import logging
from datetime import datetime

from climato.models import Mesure, Poste
from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)


def load_climato_data(csv_file_path: str) -> None:
    """Loads climato data."""
    logger.info("Load climato data")
    with open(file=csv_file_path, mode="r", encoding="utf_8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            num_poste = row["NUM_POSTE"].strip()

            try:
                poste = Poste.objects.get(num_poste=num_poste)
            except Poste.DoesNotExist:
                poste = Poste.objects.create(
                    num_poste=num_poste,
                    nom_usuel=row["NOM_USUEL"],
                    lat=row["LAT"],
                    lon=row["LON"],
                    alti=row["ALTI"],
                )
                logger.debug("New Poste: %s", poste)

            try:
                Mesure.objects.create(
                    poste=poste,
                    aaaammjj=datetime.strptime(row["AAAAMMJJ"], "%Y%m%d").date(),
                    rr=row["RR"].strip() or 0.0,
                    tn=row["TN"].strip() or 0.0,
                    tx=row["TX"].strip() or 0.0,
                    tm=row["TM"].strip() or 0.0,
                    ffm=row["FFM"].strip() or 0.0,
                )
            except CommandError as error:
                logger.error(error)
                logger.debug(row)


class Command(BaseCommand):
    """Command to load climato data."""

    help: str = "Load climato data"

    def add_arguments(self, parser):
        parser.add_argument("csv_file_path", nargs=1, type=str)

    def handle(self, *args: str, **kwargs: int) -> None:
        """Loads climato data."""
        del args
        try:
            load_climato_data(kwargs["csv_file_path"][0])
        except Exception as error:
            raise CommandError(error) from error
