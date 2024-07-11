from django.shortcuts import render


def profile(request):
    return render(request, 'contacts/profile.html')

def settings(request):
    return render(request, 'contacts/settings.html')