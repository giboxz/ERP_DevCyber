# Generated by Django 3.0 on 2022-12-05 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entradas',
            old_name='dataCriação',
            new_name='dataCriacao',
        ),
        migrations.RenameField(
            model_name='saidas',
            old_name='dataCriação',
            new_name='dataCriacao',
        ),
    ]