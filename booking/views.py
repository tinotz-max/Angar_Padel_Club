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