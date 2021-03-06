# Generated by Django 2.0.6 on 2018-08-17 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(help_text='veuillez indiquer un departement', max_length=255, unique=True)),
                ('image', models.FileField(default='Departement/images/images39.png', upload_to='Departement/images/')),
                ('description', models.TextField(help_text='Ce champ doit avoir au minimum 300 caractères')),
            ],
            options={
                'ordering': ('libelle',),
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(help_text='veuillez indiquer le titre du document', max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', models.FileField(default='Document/images/images34.jpeg', upload_to='Document/images/')),
                ('fichier', models.FileField(default='Document/fichiers/tutoriel2.pdf', upload_to='Document/fichiers/')),
            ],
            options={
                'ordering': ('titre',),
            },
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(help_text='veuillez indiquer une filiere', max_length=255, unique=True)),
                ('description', models.TextField()),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eces.Departement')),
            ],
            options={
                'ordering': ('libelle',),
            },
        ),
        migrations.AddField(
            model_name='document',
            name='filiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eces.Filiere'),
        ),
    ]
