from django.urls import path, include
from . import views


app_name = 'mobile'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', include(('mobile.contacts.urls', 'contacts'), namespace='contacts')),
]