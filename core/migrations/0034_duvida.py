# Generated by Django 5.1.5 on 2025-01-29 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0033_remove_excecaohorario_motivo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Duvida",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("mensagem", models.TextField()),
                ("respondida", models.BooleanField(default=False)),
                ("resposta", models.TextField(blank=True, null=True)),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
