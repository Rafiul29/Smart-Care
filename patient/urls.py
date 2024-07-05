from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('list', views.PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/',views.UserRegistrationApiView.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activate,name='active')
]