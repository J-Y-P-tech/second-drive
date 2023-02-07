from django.shortcuts import render


def bikes(request):
    return render(request, 'bikes/bikes.html')
