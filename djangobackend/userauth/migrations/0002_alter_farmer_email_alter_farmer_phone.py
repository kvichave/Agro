# Generated by Django 5.1.6 on 2025-02-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
