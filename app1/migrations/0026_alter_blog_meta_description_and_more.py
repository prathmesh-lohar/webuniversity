# Generated by Django 4.2.4 on 2023-08-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_blog_summary_alter_blog_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='meta_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='meta_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]