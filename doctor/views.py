from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor,Specialization,Designation,AvailableTime,Review

from .serializers import DoctorSerializer,SpecializationSerializer,DesignationSerializer,AvailableTimeSerializer,ReviewSerializer
# Create your views here.

class SpecializationViewSet(viewsets.ModelViewSet):
  queryset=Specialization.objects.all()
  serializer_class=SpecializationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
  queryset=Designation.objects.all()
  serializer_class=DesignationSerializer

class AvailableTimeViewSet(viewsets.ModelViewSet):
  queryset=AvailableTime.objects.all()
  serializer_class=AvailableTimeSerializer

class DoctorViewSet(viewsets.ModelViewSet):
  queryset=Doctor.objects.all()
  serializer_class=DoctorSerializer

class ReviewViewSet(viewsets.ModelViewSet):
  queryset=Review.objects.all()
  serializer_class=ReviewSerializer