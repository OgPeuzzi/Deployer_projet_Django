# Generated by Django 4.2.6 on 2023-10-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AidAuto', '0012_remove_booking_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='service',
            field=models.CharField(choices=[('', 'Sélectionner un Service'), ('test_diagnostique', 'Test diagnostique'), ('entretien_moteur', 'Entretien du moteur'), ('remplacement_pneus', 'Remplacement des pneus'), ('changement_huile', "Changement d'huile")], default='', max_length=50),
        ),
    ]
