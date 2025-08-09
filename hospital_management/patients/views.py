from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import patient
from .Serializers import patientSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class patientListCreateView(generics.ListCreateAPIView):
    queryset= patient.objects.all()
    serializer_class = patientSerializer
    filter_backends=[DjangoFilterBackend]
    authentication_classes = [JWTAuthentication]
    filterset_fields = ['full_name', 'gender']

