# Generated by Django 4.1.7 on 2023-03-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_profile_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default=False, max_length=10),
        ),
    ]
