# Generated by Django 2.0.5 on 2018-05-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0027_auto_20180515_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervento',
            name='progetto_del_verde_active',
            field=models.BooleanField(default=False, help_text='If is checked show progetto del verde', verbose_name='Attiva progetto del verde'),
        ),
    ]
