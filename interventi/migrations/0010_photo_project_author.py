# Generated by Django 2.0.5 on 2018-05-15 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0009_photo_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo_project',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='interventi.Intervento'),
        ),
    ]
