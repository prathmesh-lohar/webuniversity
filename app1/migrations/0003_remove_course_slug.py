# Generated by Django 4.2.4 on 2023-08-21 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_course_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
    ]