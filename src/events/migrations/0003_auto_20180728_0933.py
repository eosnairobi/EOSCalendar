# Generated by Django 2.0.7 on 2018-07-28 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_section_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='text',
        ),
    ]