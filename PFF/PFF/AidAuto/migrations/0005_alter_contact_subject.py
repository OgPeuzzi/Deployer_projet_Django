# Generated by Django 4.2.6 on 2023-10-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AidAuto', '0004_utilisateur_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Subject',
            field=models.CharField(default='', max_length=20),
        ),
    ]
