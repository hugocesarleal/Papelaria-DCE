# Generated by Django 5.1.5 on 2025-02-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0035_visita"),
    ]

    operations = [
        migrations.AddField(
            model_name="itemestoque",
            name="prioridade",
            field=models.BooleanField(default=False),
        ),
    ]
