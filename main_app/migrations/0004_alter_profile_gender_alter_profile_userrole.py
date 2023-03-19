# Generated by Django 4.1.7 on 2023-03-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_profile_certification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userRole',
            field=models.CharField(choices=[('I', 'Instructor'), ('S', 'Student')], default=False, max_length=50),
        ),
    ]
