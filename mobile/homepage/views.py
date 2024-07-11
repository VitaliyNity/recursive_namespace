from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index_m.html')
