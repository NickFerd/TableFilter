from django.contrib import admin

from .models import Clients, Modes, Equipment, Durations

admin.site.register(Clients)
admin.site.register(Modes)
admin.site.register(Equipment)


