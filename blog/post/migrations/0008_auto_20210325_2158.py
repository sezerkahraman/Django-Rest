# Generated by Django 2.2.3 on 2021-03-25 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20210325_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='modified_by',
            new_name='modified',
        ),
    ]