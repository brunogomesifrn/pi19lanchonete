# Generated by Django 2.2.1 on 2019-11-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='etapa',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Etapa'),
        ),
    ]
