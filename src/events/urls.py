from django.urls import path
from rest_framework.routers import DefaultRouter

from .api.views import EventModelViewSet, events, e
from .views import home, map_view, landing

router = DefaultRouter(trailing_slash=False)

router.register('events', EventModelViewSet, base_name='events')

urlpatterns = [
    path('', landing, name='landing'),
    path('cal-view/', home, name='calendar_view'),
    path('evts', events, name='evts'),
    path('event', e, name='e'),
    path('map-view/', map_view, name='map_view'),
]
urlpatterns += router.urls