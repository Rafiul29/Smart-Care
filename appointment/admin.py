from typing import Any
from django.contrib import admin
from .models import Appointment

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
  list_display=['patient','doctor','appointment_types','appointment_status','symptom','time','cancle']

  def doctor(self,obj):
    return self.doctor.user.first_name
  

  def patient(self,obj):
    return self.patient.user.first_name
  
  def save_model(self, request,obj,form,chnage) -> None:
    obj.save()
    if obj.appointment_status=="Running" and obj. appointment_types=='Online':
      email_subject='Your online Appointment Running'
      email_body=render_to_string('appointment_email.html',{'user':obj.patient.user,'doctor':obj.doctor})
      email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
      email.attach_alternative(email_body, "text/html")
      email.send()

admin.site.register(Appointment,AppointmentAdmin)