# Generated by Django 4.2.1 on 2023-06-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_matricula_situacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='situacao',
            field=models.CharField(choices=[('A', 'Aprovado'), ('R', 'Reprovado')], default='A', max_length=1, verbose_name='Situação'),
            preserve_default=False,
        ),
    ]
