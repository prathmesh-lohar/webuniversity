# Generated by Django 4.2.4 on 2023-08-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_alter_blog_meta_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumb',
            field=models.ImageField(default='ex.png', help_text='640*426', upload_to='blog/thumb'),
            preserve_default=False,
        ),
    ]
