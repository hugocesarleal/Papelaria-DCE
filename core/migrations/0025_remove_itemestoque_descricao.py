# Generated by Django 5.1.5 on 2025-01-27 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_customuser_primeiro_acesso"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="itemestoque",
            name="descricao",
        ),
    ]
