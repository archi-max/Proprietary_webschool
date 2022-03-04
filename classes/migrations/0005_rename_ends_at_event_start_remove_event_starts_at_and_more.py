# Generated by Django 4.0.1 on 2022-03-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_remove_class_created_by_remove_class_groups_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='ends_at',
            new_name='start',
        ),
        migrations.RemoveField(
            model_name='event',
            name='starts_at',
        ),
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='background_color',
            field=models.CharField(default='#03a9f3', max_length=7),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
