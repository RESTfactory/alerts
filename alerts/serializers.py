from rest_framework import serializers
from .models import AlertType, Alert, EntityType, Entity, App

class AlertTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertType
        fields = ('url', 'id', 'name', 'app', 'description')

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model =Alert
        fields = ('url', 'id', 'name', 'description', 'alert_type', 'created_at', 'updated_at', 'entity')

class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = ('url', 'id', 'name', 'description', 'app')

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('code', 'name', 'description', 'entity_type', 'created_at', 'updated_at')

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('url', 'id', 'name', 'created_at', 'updated_at')
