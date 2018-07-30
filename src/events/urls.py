from django.urls import path
from rest_framework.routers import DefaultRouter

from .api.views import EventModelViewSet, events, e
from .views import home

router = DefaultRouter(trailing_slash=False)

router.register('events', EventModelViewSet, base_name='events')

urlpatterns = [
    path('', home, name='home'),
    path('evts', events, name='evts'),
    path('event', e, name='e'),
]
urlpatterns += router.urls