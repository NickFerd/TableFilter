from django.contrib import admin

from .models import Client, Mode, Equipment, Duration

admin.site.register(Client)
admin.site.register(Mode)
admin.site.register(Equipment)


