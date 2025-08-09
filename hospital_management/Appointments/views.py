from rest_framework import generics, permissions
from django.core.exceptions import PermissionDenied
from Appointments.models import Appointment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsDoctorOrPatientOwner 
from django.core.mail import send_mail
from .models import Appointment
from .Serializers import AppointmentSerializer


# Create your views here.
class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['date']


    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'doctor'):
            return Appointment.objects.filter(doctor = user.doctor)
        elif hasattr(user, 'patient'):
            return Appointment.objects.filter(patient = user.patient )
        return Appointment.objects.none()
    
    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user,'patient'):
            patient = user.patient
            doctor =self.request.data.get('doctor')
            appointment = serializer.save(patient =patient, doctor_id = doctor)
             
             # email notification
            send_mail(
               subject = 'Appointment confirmation', 
               message=   f' Hi {patient.full_name}, your appointment with Dr.{appointment.doctor.name} is scheduled on {appointment.date}.',
               from_email= '@gmail.com',
               recipient_list=[patient.email],
                fail_silently=False,
            )
        else:
            raise PermissionDenied("Only patients can book appointment.")

        