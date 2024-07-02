from django.contrib import admin
from .models import Appointment
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
  list_display=['patient','doctor','appointment_types','appointment_status','symptom','time','cancle']

  def doctor(self,obj):
    return self.doctor.user.first_name
  

  def patient(self,obj):
    return self.patient.user.first_name

admin.site.register(Appointment,AppointmentAdmin)