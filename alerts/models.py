from django.db import models

class AlertType(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=30)

class Alert(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    alert_type = models.ForeignKey(AlertType)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EntityType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Entity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    entity_type = models.ForeignKey(EntityType)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
