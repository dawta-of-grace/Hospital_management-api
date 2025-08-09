from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Doctor
from django_filters.rest_framework import DjangoFilterBackend
from .Serializers import DoctorSerializer
from Appointments.permissions import IsDoctorOrPatientOwner 


# Create your views here.
class DoctorListCreateView(generics.ListCreateAPIView):
    queryset= Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends=[DjangoFilterBackend]
    authentication_classes = [JWTAuthentication]
    filterset_fields = [ 'name', 'specialty']



    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticatedOrReadOnly()]


