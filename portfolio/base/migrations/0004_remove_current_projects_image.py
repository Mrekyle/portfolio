# Generated by Django 4.2.9 on 2024-07-20 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_current_projects_image_url_alter_offerings_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='current_projects',
            name='image',
        ),
    ]
