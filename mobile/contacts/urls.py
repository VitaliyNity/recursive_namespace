from django.urls import path
from . import views


app_name = 'contacts'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
]