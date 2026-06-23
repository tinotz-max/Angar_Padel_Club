from django.contrib import admin
from django.urls import path, include
from booking.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('booking.urls')),
    path('', index_view, name='index'),
]