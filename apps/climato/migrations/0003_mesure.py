# Generated by Django 5.0.4 on 2024-04-08 21:38

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climato', '0002_remove_poste_changed_at_remove_poste_changed_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesure',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('aaaammjj', models.DateField(help_text='date de la mesure (année mois jour)', verbose_name='date')),
                ('rr', models.DecimalField(decimal_places=1, help_text='quantité de précipitation tombée en 24 heures (de 06h FU le jour J à 06h FU le jour J+1). La valeur relevée à J+1 est affectée au jour J (en mm et 1/10)', max_digits=6, verbose_name='précipitation')),
                ('tn', models.DecimalField(decimal_places=1, help_text='température minimale sous abri (en °C et 1/10)', max_digits=3, verbose_name='température minimale')),
                ('tx', models.DecimalField(decimal_places=1, help_text='température maximale sous abri (en °C et 1/10)', max_digits=3, verbose_name='température maximale')),
                ('tm', models.DecimalField(decimal_places=1, help_text='moyenne quotidienne des températures horaires sous abri (en °C et 1/10)', max_digits=3, verbose_name='température moyenne')),
                ('ffm', models.DecimalField(decimal_places=1, help_text='moyenne quotidienne de la force du vent moyenné sur 10 mn, à 10 m (en m/s et 1/10)', max_digits=6, verbose_name='vent moyen')),
                ('poste', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mesures', related_query_name='mesure', to='climato.poste', verbose_name='poste')),
            ],
            options={
                'verbose_name': 'mesure',
                'verbose_name_plural': 'mesures',
                'ordering': ['-aaaammjj'],
            },
        ),
    ]
