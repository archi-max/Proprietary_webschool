# Generated by Django 4.0.1 on 2022-01-30 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='data',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='notebook',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='notebook',
            name='notebook_id',
            field=models.CharField(default='a', max_length=25),
            preserve_default=False,
        ),
    ]