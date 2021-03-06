# Generated by Django 3.1.1 on 2020-09-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
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
            name='Durations',
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
            name='Equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_id', models.IntegerField()),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'equipment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'modes',
                'managed': False,
            },
        ),
    ]
