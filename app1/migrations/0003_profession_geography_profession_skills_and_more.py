# Generated by Django 4.1.4 on 2023-01-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_profession_demand'),
    ]

    operations = [
        migrations.AddField(
            model_name='profession',
            name='geography',
            field=models.TextField(default='Описание', verbose_name='География'),
        ),
        migrations.AddField(
            model_name='profession',
            name='skills',
            field=models.TextField(default='Описание', verbose_name='Необходимые навыки'),
        ),
        migrations.AddField(
            model_name='profession',
            name='vacancies',
            field=models.TextField(default='Описание', verbose_name='Последние вакансии'),
        ),
    ]
