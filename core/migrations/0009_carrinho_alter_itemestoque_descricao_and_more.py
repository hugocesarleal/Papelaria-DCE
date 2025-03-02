# Generated by Django 4.1 on 2024-12-20 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_remove_venda_usuario_alter_itemestoque_descricao_and_more"),
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
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="itemestoque",
            name="descricao",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="itemestoque",
            name="foto",
            field=models.ImageField(
                default="path/to/default/image.jpg", upload_to="estoque/"
            ),
        ),
        migrations.AlterField(
            model_name="itemestoque",
            name="nome",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="itemestoque",
            name="quantidade",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="itemestoque",
            name="valor",
            field=models.DecimalField(decimal_places=2, max_digits=10),
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
                        to="core.carrinho",
                    ),
                ),
                (
                    "item_estoque",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.itemestoque",
                    ),
                ),
            ],
        ),
    ]
