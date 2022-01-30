# Generated by Django 4.0.1 on 2022-01-30 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.models
import utils.files


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=posts.models.filename_generator, validators=[utils.files.document_fileextension_validator])),
                ('tags', models.CharField(blank=True, choices=[('AN', 'Announcement'), ('RS', 'Result'), ('QB', 'Question Bank'), ('NT', 'Notes')], default='AN', max_length=2)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, related_name='posts', to='auth.Group')),
            ],
        ),
    ]