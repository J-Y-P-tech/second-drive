from django.shortcuts import render
from .models import Team
from bikes.models import Bike


def home(request):
    teams = Team.objects.all()
    featured_bikes = Bike.objects.order_by('-created_date').filter(is_featured=True)
    all_bikes = Bike.objects.order_by('-created_date')
    print(f'Featured bikes count {featured_bikes.count()}')
    data = {
        'teams': teams,
        'featured_bikes': featured_bikes,
        'all_bikes': all_bikes,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
