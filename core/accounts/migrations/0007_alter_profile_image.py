# Generated by Django 3.2.23 on 2023-12-17 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='avatars/default.jpg', null=True, upload_to='avatars/'),
        ),
    ]
