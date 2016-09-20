from django.conf import settings
from django.db import models

class App(models.Model):
    name = models.CharField(max_length=30)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EntityType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)
    app = models.ForeignKey(App)

    def __str__(self):
        return self.name

class Entity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)
    entity_type = models.ForeignKey(EntityType)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AlertType(models.Model):
    name = models.CharField(max_length=10)
    app = models.ForeignKey(App)
    description = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class Alert(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    alert_type = models.ForeignKey(AlertType)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entity = models.ForeignKey(Entity)

    def __str__(self):
        return self.name
