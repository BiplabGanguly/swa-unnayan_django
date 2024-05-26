# Generated by Django 5.0.6 on 2024-05-25 20:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0002_institutebranch'),
        ('user', '0006_alter_user_data_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.CharField(choices=[('faculty', 'faculty'), ('student', 'student')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Institute.institutebranch')),
            ],
        ),
    ]
