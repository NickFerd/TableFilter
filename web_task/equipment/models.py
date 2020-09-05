
from django.db import models


class Clients(models.Model):
    id = models.AutoField(unique=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'clients'


class Durations(models.Model):
    id = models.AutoField(unique=True)
    client_id = models.IntegerField()
    equipment_id = models.IntegerField()
    start = models.TextField()
    stop = models.TextField()
    mode_id = models.IntegerField()
    minutes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'durations'


class Equipment(models.Model):
    id = models.AutoField()
    client_id = models.IntegerField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'equipment'


class Modes(models.Model):
    id = models.AutoField(unique=True)
    name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modes'
