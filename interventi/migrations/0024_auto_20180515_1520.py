# Generated by Django 2.0.5 on 2018-05-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0023_intervento_video_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervento',
            name='committente_active',
            field=models.BooleanField(default=False, help_text='If is checked show the committente', verbose_name='Attiva committente'),
        ),
        migrations.AddField(
            model_name='intervento',
            name='fine_lavori_active',
            field=models.BooleanField(default=False, help_text='If is checked show the fine lavori', verbose_name='Attiva fine lavori'),
        ),
        migrations.AddField(
            model_name='intervento',
            name='inizio_lavori_active',
            field=models.BooleanField(default=False, help_text='If is checked show the inizio lavori', verbose_name='Attiva inizio lavori'),
        ),
    ]
