from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Patient
from .serializers import PatientSerializer,RegistrationSerializer
from rest_framework.response import Response
# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
  queryset=Patient.objects.all()
  serializer_class=PatientSerializer


class UserRegistrationApiView(APIView):
  serializer_class=RegistrationSerializer

  def post(self,request):
    serializer=self.serializer_class(data=request.data)

    if serializer.is_valid():
      user = serializer.save()
      print(user)
      return Response("User Registration Successfull")
    
    return Response(serializer.errors)