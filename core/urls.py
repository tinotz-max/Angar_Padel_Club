from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # CORRECCIÓN AQUÍ: Se usa 'booking.urls' con un PUNTO, no con barra '/'
    path('api/', include('booking.urls')), 
]