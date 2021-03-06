# Generated by Django 2.0.7 on 2018-07-29 13:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180728_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestedEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('section_id', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
