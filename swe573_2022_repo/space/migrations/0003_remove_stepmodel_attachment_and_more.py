# Generated by Django 4.1.3 on 2022-12-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_resourcemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stepmodel',
            name='attachment',
        ),
        migrations.AddField(
            model_name='stepmodel',
            name='relatedresource',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]