# Generated by Django 5.0.6 on 2024-05-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_userbranch'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbranch',
            name='user_permission',
            field=models.CharField(blank=True, choices=[('pending', 'pending'), ('accept', 'accept'), ('reject', 'reject')], max_length=50),
        ),
    ]
