
from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'clients'


class Duration(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    equipment_id = models.IntegerField()
    start = models.DateTimeField()
    stop = models.DateTimeField()
    mode_id = models.IntegerField()
    minutes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'durations'


class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'equipment'


class Mode(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modes'

    def __str__(self):
        return self.name
