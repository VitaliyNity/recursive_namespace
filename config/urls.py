from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobile/', include(('mobile.homepage.urls', 'mobile'), namespace='mobile')),
    path('desktop/', include(('desktop.urls', 'desktop'), namespace='desktop')),
]