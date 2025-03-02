# Generated by Django 5.1.5 on 2025-02-18 20:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("estoque", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Carrinho",
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
                ("ativo", models.BooleanField(default=True)),
                (
                    "comprovante_pix",
                    models.ImageField(
                        blank=True, null=True, upload_to="comprovantes_pix/"
                    ),
                ),
                ("data_venda", models.DateTimeField(blank=True, null=True)),
                (
                    "valor_total",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemCarrinho",
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
                ("quantidade", models.PositiveIntegerField()),
                (
                    "preco_unitario",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "carrinho",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itens",
                        to="vendas.carrinho",
                    ),
                ),
                (
                    "item_estoque",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="estoque.itemestoque",
                    ),
                ),
            ],
        ),
    ]
