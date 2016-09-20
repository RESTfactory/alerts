from django.contrib import admin
from .models import AlertType, Alert, EntityType, Entity, App

admin.site.register(AlertType)
admin.site.register(Alert)
admin.site.register(EntityType)
admin.site.register(Entity)
admin.site.register(App)
