# Generated by Django 4.1 on 2022-08-21 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimerMVT', '0002_delete_mvt_remove_familia_anio'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='edad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
