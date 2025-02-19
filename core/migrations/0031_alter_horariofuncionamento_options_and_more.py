# Generated by Django 5.1.5 on 2025-01-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0030_horariofuncionamento_excecaohorario"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="horariofuncionamento",
            options={"ordering": ["dia_semana", "horario_abertura"]},
        ),
        migrations.RenameField(
            model_name="excecaohorario",
            old_name="data_excecao",
            new_name="data",
        ),
        migrations.RenameField(
            model_name="excecaohorario",
            old_name="horario_alterado",
            new_name="status",
        ),
        migrations.RenameField(
            model_name="horariofuncionamento",
            old_name="hora_abertura",
            new_name="horario_abertura",
        ),
        migrations.RenameField(
            model_name="horariofuncionamento",
            old_name="hora_fechamento",
            new_name="horario_fechamento",
        ),
        migrations.AlterField(
            model_name="horariofuncionamento",
            name="dia_semana",
            field=models.CharField(
                choices=[
                    ("Segunda", "Segunda"),
                    ("Terça", "Terça"),
                    ("Quarta", "Quarta"),
                    ("Quinta", "Quinta"),
                    ("Sexta", "Sexta"),
                    ("Sábado", "Sábado"),
                    ("Domingo", "Domingo"),
                ],
                max_length=10,
            ),
        ),
    ]
