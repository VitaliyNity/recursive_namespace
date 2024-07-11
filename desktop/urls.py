from django.urls import path, include
from desktop import views


app_name = 'desktop'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', include(('desktop.contacts.urls', 'contacts'), namespace='contacts')),
]