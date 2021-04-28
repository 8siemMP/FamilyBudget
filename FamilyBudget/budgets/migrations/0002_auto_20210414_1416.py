# Generated by Django 3.1.7 on 2021-04-14 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='budget',
            name='privileges',
        ),
        migrations.AddField(
            model_name='budget',
            name='privileges',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Privilege',
        ),
    ]
