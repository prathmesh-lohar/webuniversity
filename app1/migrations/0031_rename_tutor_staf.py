# Generated by Django 4.2.4 on 2023-08-30 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_rename_staf_tutor_download_file_profile_pic_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tutor',
            new_name='staf',
        ),
    ]