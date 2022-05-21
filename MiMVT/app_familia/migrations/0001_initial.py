# Generated by Django 4.0.4 on 2022-05-19 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Apellido', models.CharField(max_length=30)),
                ('Edad', models.IntegerField()),
                ('Parentesco', models.CharField(max_length=30)),
                ('Direccion', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IngresoenSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomFam', models.CharField(max_length=40)),
                ('FingresoSist', models.DateField()),
                ('FamDirecto', models.BooleanField()),
            ],
        ),
    ]