# Generated by Django 5.0.1 on 2024-05-19 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_profile_user_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='user_title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]