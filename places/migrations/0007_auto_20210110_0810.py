# Generated by Django 3.1.1 on 2021-01-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20210110_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(verbose_name='Короткое описание'),
        ),
    ]
