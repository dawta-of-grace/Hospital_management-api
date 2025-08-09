from rest_framework import permissions
from Doctors.models import Doctor
from patients.models import patient

class IsDoctorOrPatientOwner (permissions.BasePermission):
#only allow doctors to see their appointments or patient to see theirs.

 def has_object_permission(self,request,view,obj):
    if hasattr(request.user, 'doctor'):
        return obj.doctor.user == request.user
    elif hasattr(request.user, 'patient'):
        return obj.patient.user == request.user
    return False


def has_permission(self,request,view):
    return request.user.is_authenticated
