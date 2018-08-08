import uuid

from django.contrib.gis.db import models
from django.db import models
from django.utils import timezone


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=300)
    description = models.CharField(max_length=300, null=True)
    venue = models.CharField(max_length=100, null=True)
    # geom = models.PointField(srid=4326, blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    section_id = models.PositiveIntegerField(default=1)
    image = models.ImageField(null=True)
    url_link=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.text


class SuggestedEvent(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True)
    venue = models.CharField(max_length=100, null=True)
    contact_person = models.CharField(max_length=30, null=True)
    contact_email = models.EmailField(null=True)
    telegram_channel = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    url_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title