from django.contrib import admin
from .models import Event, SuggestedEvent


admin.site.register(Event)
admin.site.register(SuggestedEvent)