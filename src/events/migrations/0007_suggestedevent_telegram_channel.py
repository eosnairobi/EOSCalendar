# Generated by Django 2.0.7 on 2018-07-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20180731_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestedevent',
            name='telegram_channel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
