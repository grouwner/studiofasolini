# Generated by Django 2.0.5 on 2018-05-15 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0010_photo_project_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo_project',
            name='author',
        ),
        migrations.DeleteModel(
            name='photo_project',
        ),
    ]
