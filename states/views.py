from django.utils import timezone
from .models import State
from django.shortcuts import render, get_object_or_404

def state_list(request):
    states = State.objects.all()
    return render(request, 'state/state_list.html', {'states':states})

def graphs(request):
    states = State.objects.all()
    return render(request, 'state/graphs.html', {'states':states})


def state_theory(request):
    states = State.objects.all()
    return render(request, 'state/state_theory.html', {'states':states})

def state_detail(request, pk):
    states = get_object_or_404(State, pk=pk)
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'state/state_detail.html', {'states': states,'mapbox_access_token': mapbox_access_token})    