# Generated by Django 4.0.1 on 2022-02-08 03:29

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_avatar_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default/images/default_avatar.jpg', upload_to=user.models.avatar_filename_generator),
        ),
    ]
