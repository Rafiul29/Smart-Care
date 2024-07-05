from django.shortcuts import render
from rest_framework import viewsets,filters,pagination

from .models import Doctor,Specialization,Designation,AvailableTime,Review

from .serializers import DoctorSerializer,SpecializationSerializer,DesignationSerializer,AvailableTimeSerializer,ReviewSerializer


from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.



class SpecializationViewSet(viewsets.ModelViewSet):
  queryset=Specialization.objects.all()
  serializer_class=SpecializationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
  queryset=Designation.objects.all()
  serializer_class=DesignationSerializer


class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
  def filter_queryset(self,request,query_set,view):
    doctor_id=request.query_params.get('doctor_id')
    if doctor_id:
      return query_set.filter(doctor=doctor_id)
    return query_set


class AvailableTimeViewSet(viewsets.ModelViewSet):

  queryset=AvailableTime.objects.all()
  serializer_class=AvailableTimeSerializer
  filter_backends=[AvailableTimeForSpecificDoctor]

class DoctorPagination(pagination.PageNumberPagination):
  page_size=1
  page_size_query_param=page_size
  max_page_size=50

class DoctorViewSet(viewsets.ModelViewSet):
  queryset=Doctor.objects.all()
  serializer_class=DoctorSerializer
  filter_backends=[filters.SearchFilter]
  pagination_class=DoctorPagination
  search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']

class ReviewViewSet(viewsets.ModelViewSet):
  permission_classes=[IsAuthenticated]
  queryset=Review.objects.all()
  serializer_class=ReviewSerializer