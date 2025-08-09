from django.urls import path
from .views import patientListCreateView


urlpatterns = [
    path('', patientListCreateView.as_view(), name='patient' )
]