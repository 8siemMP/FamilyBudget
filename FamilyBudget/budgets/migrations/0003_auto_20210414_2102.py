# Generated by Django 3.1.7 on 2021-04-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0002_auto_20210414_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='privileges',
            field=models.JSONField(default={}),
        ),
    ]
