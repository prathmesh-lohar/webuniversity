# Generated by Django 4.2.4 on 2023-08-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thubnail',
            field=models.ImageField(blank=True, help_text='200*200', null=True, upload_to='blog/thumb'),
        ),
    ]