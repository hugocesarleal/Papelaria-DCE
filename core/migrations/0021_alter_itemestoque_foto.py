# Generated by Django 5.1.5 on 2025-01-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_alter_itemestoque_foto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemestoque",
            name="foto",
            field=models.ImageField(
                default="path/to/default/image.jpg", upload_to="img/estoque/"
            ),
        ),
    ]
