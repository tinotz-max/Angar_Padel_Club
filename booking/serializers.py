from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Court, Booking

# Serializer para los usuarios (autenticación e información básica)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializer para las Canchas (Court)
class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ['id', 'name', 'status', 'court_type']

# Serializer para las Reservas (Booking) - El corazón de la API
class BookingSerializer(serializers.ModelSerializer):
    # Esto nos permite ver los datos completos de la cancha y el usuario en vez de solo el ID
    court_details = CourtSerializer(source='court', read_only=True)
    user_details = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 
            'user', 
            'user_details', 
            'court', 
            'court_details', 
            'start_time', 
            'end_time', 
            'status'
        ]
        
    # Validación técnica: Evitar que reserven en el pasado o turnos inválidos
    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError({
                "end_time": "The end time must be strictly after the start time."
            })
        return data