from django.conf import settings
from django.db import models

class App(models.Model):
    name = models.CharField(max_length=30)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AlertType(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    app = models.ForeignKey(App)

class Alert(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    alert_type = models.ForeignKey(AlertType)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EntityType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    app = models.ForeignKey(App)

class Entity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    entity_type = models.ForeignKey(EntityType)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
