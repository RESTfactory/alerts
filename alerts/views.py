from rest_framework import viewsets
from .models import AlertType, Alert, EntityType, Entity, App
from .serializers import AlertTypeSerializer, AlertSerializer, EntityTypeSerializer, EntitySerializer, AppSerializer

class AlertTypeViewSet(viewsets.ModelViewSet):
    queryset = AlertType.objects.all()
    serializer_class = AlertTypeSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class EntityTypeViewSet(viewsets.ModelViewSet):
    queryset = EntityType.objects.all()
    serializer_class = EntityTypeSerializer

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
