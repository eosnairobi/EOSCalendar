from django.shortcuts import render
from .forms import SuggestedEventForm
from .models import SuggestedEvent
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = SuggestedEventForm(request.POST or None, files=request.FILES)
        if form.is_valid():
            form.save()
            print('Saved')
        else:
            print(form.errors)

    elif request.method == 'GET':
        form = SuggestedEventForm()
    return render(request, 'home.html', {'form': form})


def map_view(request):
    return render(request, 'map_view.html')


def landing(request):
    return render(request, 'landing.html')
