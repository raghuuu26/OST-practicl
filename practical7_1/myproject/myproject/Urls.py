

from django.contrib import admin

from django.urls import path, include
urlpatterns = [
path('', include('myapp.Urls')), path('admin/', admin.site.urls),
]
