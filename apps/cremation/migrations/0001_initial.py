# Generated by Django 3.2 on 2022-04-24 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedCharges',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('material_cost', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('vehicle_no', models.CharField(max_length=255)),
                ('driver_name', models.CharField(max_length=255)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='IN', unique=True, verbose_name='Contact Number')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.city')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Priest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='IN', unique=True, verbose_name='Contact Number')),
                ('address', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.city')),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cremation.religion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cremation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], default='M', max_length=1)),
                ('address', models.CharField(max_length=255)),
                ('demise_date', models.DateField()),
                ('demise_time', models.TimeField()),
                ('is_priest', models.BooleanField(default=False)),
                ('is_vehicle', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('demise_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.city')),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cremation.religion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
