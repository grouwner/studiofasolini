# Generated by Django 2.0.5 on 2018-05-15 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0016_auto_20180515_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo_project',
            name='titolo_photo',
        ),
    ]