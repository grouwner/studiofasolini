# Generated by Django 2.0.5 on 2018-05-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0017_remove_photo_project_titolo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervento',
            name='photo_active',
            field=models.BooleanField(default=False, help_text='If is checked show the Photo Album', verbose_name='Attiva Photo Album'),
        ),
    ]
