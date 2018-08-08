from datetime import datetime

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Event, SuggestedEvent
from .serializers import EventModelSerializer


class EventModelViewSet(viewsets.ModelViewSet):
    serializer_class = EventModelSerializer
    queryset = Event.objects.all()
    authentication_classes = []


@api_view(['GET'])
def events(request):
    events = Event.objects.all()
    response = []
    for event in events:
        std = str(event.start_date)
        end = str(event.end_date)
        response.append({'id': event.id, 'text': event.text, 'description': event.description, 'image': event.image.url, 'venue': event.venue,
                         'start_date': std[:19], 'end_date': end[:19], 'section_id': event.section_id, 'url':event.url_link})

    return Response(response)


@api_view(['POST'])
def e(request):
    data = request.data
    print(data)

    # Save Suggested Event
    """
        {'!nativeeditor_status': ['inserted'], 'id': ['1532872755923'], 
        'rec_pattern': [''], 'text': ['New event'], 'event_pid': [''], 
        'start_date': ['2018-01-26 00:00'], 'rec_type': [''], 'event_length': [''], 'end_date': ['2018-01-27 00:00']}
    """
    start_date = data.get('start_date')
    print(datetime(start_date))

    return Response('success')


@api_view(['GET'])
def map_data(request):
    events = Event.objects.all().order_by()
    response = []
    for event in events:
        std = str(event.start_date)
        end = str(event.end_date)
        response.append({'id': event.id, 'text': event.text, 'description': event.description, 'image': event.image,
                         'start_date': std[:19], 'end_date': end[:19], 'section_id': event.section_id})

    return Response(response)
