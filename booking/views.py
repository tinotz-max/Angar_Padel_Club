from rest_framework import viewsets, permissions
from .models import Court, Booking
from .serializers import CourtSerializer, BookingSerializer

class CourtViewSet(viewsets.ModelViewSet):
    """
    API endpoint para listar, crear, editar o eliminar canchas.
    """
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
    permission_classes = [permissions.AllowAny] # Permite lectura libre para el frontend

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar las reservas (ABML completo).
    """
    queryset = Booking.objects.all().order_by('-start_time')
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny] # En producción usaríamos IsAuthenticated

    # Opcional: Filtrar para ver solo las reservas del usuario actual si se requiere
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Court, Booking
from django.utils.dateparse import parse_datetime
import datetime

def index_view(request):
    if request.method == 'POST':
        court_id = request.POST.get('court_id')
        user_id = request.POST.get('user_id')
        start_time_str = request.POST.get('start_time')
        
        # Procesar los objetos requeridos
        court = Court.objects.get(id=court_id)
        # Busca el usuario ingresado, si falla toma el admin logueado
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = User.objects.first()
            
        start_time = parse_datetime(start_time_str)
        # CALCULO AUTOMÁTICO: Suma exactamente 1 hora (60 minutos)
        end_time = start_time + datetime.timedelta(hours=1)
        
        # Guardar registro real en base de datos
        Booking.objects.create(
            user=user,
            court=court,
            start_time=start_time,
            end_time=end_time,
            status='confirmed'
        )
        return redirect('index') # Recarga la página por scroll limpia

    # Peticiones GET comunes
    courts = Court.objects.all()
    bookings = Booking.objects.all().order_by('-start_time')
    return render(request, 'booking/index.html', {'courts': courts, 'bookings': bookings})