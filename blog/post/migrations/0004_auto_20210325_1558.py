# Generated by Django 2.2.3 on 2021-03-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210324_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Resimler/post'),
        ),
    ]
