# Generated by Django 5.1.6 on 2025-02-22 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userauth', '0002_alter_farmer_email_alter_farmer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('crop_id', models.AutoField(primary_key=True, serialize=False)),
                ('crop_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.farmer')),
            ],
        ),
    ]
