# Generated by Django 2.0.5 on 2018-05-15 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0020_auto_20180515_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervento',
            name='info_active',
            field=models.BooleanField(default=False, help_text='If is checked show the Info Project', verbose_name='Attiva Info Project'),
        ),
    ]
