# Generated by Django 3.2 on 2022-04-24 07:01

from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('speaker', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('start_at', models.TimeField()),
                ('duration', models.DecimalField(decimal_places=2, max_digits=7)),
                ('mode', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], default='Online', max_length=10)),
                ('venue', models.CharField(max_length=255)),
                ('cover_image', models.ImageField(default='seminar.jpg', upload_to='seminar\\cover_image')),
                ('watch_on_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SeminarAttendees',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='IN', unique=True, verbose_name='Contact Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
