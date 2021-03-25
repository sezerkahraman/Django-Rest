# Generated by Django 2.2.3 on 2021-03-25 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_post_modified_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]