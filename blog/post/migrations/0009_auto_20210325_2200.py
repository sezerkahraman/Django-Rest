# Generated by Django 2.2.3 on 2021-03-25 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20210325_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified', to=settings.AUTH_USER_MODEL),
        ),
    ]