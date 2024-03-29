# Generated by Django 4.2.6 on 2023-10-14 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=350)),
                ('Last_name', models.CharField(max_length=350)),
                ('Email', models.EmailField(max_length=350)),
                ('Message', models.TextField(max_length=500)),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicule', models.CharField(max_length=50)),
                ('Admin_Demande', models.CharField(max_length=50)),
                ('Statut_Demande', models.CharField(max_length=350)),
                ('Description', models.TextField(max_length=500)),
                ('marque', models.CharField(max_length=25)),
                ('modele', models.CharField(max_length=25)),
                ('puissance', models.CharField(max_length=25)),
                ('energie', models.CharField(max_length=25)),
                ('matricule', models.CharField(max_length=25)),
                ('kilometrage', models.CharField(max_length=25)),
                ('panne', models.CharField(max_length=20)),
                ('Date_Panne', models.DateField()),
                ('Heure_Panne', models.TimeField()),
                ('Lieu_Panne', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Demande',
            },
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=350)),
                ('password', models.CharField(max_length=350)),
            ],
            options={
                'db_table': 'Login',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_d_utilisateur', models.CharField(max_length=350)),
                ('email', models.EmailField(max_length=350)),
                ('password_hash', models.CharField(max_length=350)),
                ('confirm_password', models.CharField(max_length=350, null=True)),
            ],
            options={
                'db_table': 'Register',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_role', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Role',
            },
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=350)),
                ('last_name', models.CharField(max_length=350)),
                ('région', models.CharField(max_length=350)),
                ('num_tel', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=350)),
                ('password', models.CharField(max_length=350)),
            ],
            options={
                'db_table': 'Utilisateur',
            },
        ),
    ]
