from django.db import models
from patients.models import patient
from Doctors.models import Doctor


class Appointment(models.Model):
    patient = models.ForeignKey(patient, on_delete=models.CASCADE, blank=False, null=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    reason = models.TextField(blank=False, null=False)


    def __str__(self):
        return f"Appointment: {self.patient} with {self.doctor} on {self.date} at {self.time}"