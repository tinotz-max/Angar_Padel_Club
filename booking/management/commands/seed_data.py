from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from booking.models import Court, Booking
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Poblar la base de datos con canchas de prueba'

    def handle(self, *args, **kwargs):
        # 1. Crear Canchas si no existen
        court1, created1 = Court.objects.get_or_create(name='Court 01', status='available', court_type='indoor')
        court2, created2 = Court.objects.get_or_create(name='Court 02', status='available', court_type='outdoor')
        
        self.stdout.write(self.style.SUCCESS('Canchas verificadas/creadas con éxito.'))

        # 2. Crear una reserva de prueba asociada al primer usuario que encuentre
        user = User.objects.first()
        if user:
            start = timezone.now() + datetime.timedelta(days=1) # Mañana
            end = start + datetime.timedelta(hours=1, minutes=30) # Turno de 90 min
            
            Booking.objects.create(
                user=user,
                court=court1,
                start_time=start,
                end_time=end,
                status='confirmed'
            )
            self.stdout.write(self.style.SUCCESS(f'Reserva de prueba creada para el usuario: {user.username}'))
        else:
            self.stdout.write(self.style.WARNING('No se creó reserva porque no hay usuarios en la BD. Crea uno en /admin.'))