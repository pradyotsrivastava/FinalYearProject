# Generated by Django 3.2 on 2022-04-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.PositiveBigIntegerField(blank=True, null=True, unique=True, verbose_name='Contact Number'),
        ),
    ]