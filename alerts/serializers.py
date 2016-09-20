from rest_framework import serializers
from .models import AlertType, Alert, EntityType, Entity, App

class AlertTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlertType
        # fields = ('url', 'username', 'email', 'is_staff')

class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Alert

class EntityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EntityType

class EntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entity

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = App
