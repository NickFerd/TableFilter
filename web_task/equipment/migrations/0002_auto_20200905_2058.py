# Generated by Django 3.1.1 on 2020-09-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'clients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_id', models.IntegerField()),
                ('equipment_id', models.IntegerField()),
                ('start', models.TextField()),
                ('stop', models.TextField()),
                ('mode_id', models.IntegerField()),
                ('minutes', models.IntegerField()),
            ],
            options={
                'db_table': 'durations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'modes',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.DeleteModel(
            name='Durations',
        ),
        migrations.DeleteModel(
            name='Modes',
        ),
    ]
