# Generated by Django 3.0.6 on 2020-05-07 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200505_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='agree',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='disagree',
            field=models.IntegerField(default=0),
        ),
    ]
