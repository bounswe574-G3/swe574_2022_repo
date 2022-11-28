# Generated by Django 4.0.4 on 2022-11-12 13:35

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SpaceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdSpaces', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('members', models.ManyToManyField(related_name='includedSpaces', to=settings.AUTH_USER_MODEL, verbose_name='members')),
            ],
            options={
                'verbose_name': 'Space',
                'verbose_name_plural': 'Spaces',
                'db_table': 'space',
            },
        ),
        migrations.CreateModel(
            name='StepModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steptitle', models.CharField(max_length=50)),
                ('stepcontent', ckeditor.fields.RichTextField(max_length=500)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='files')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('stepcreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step', to=settings.AUTH_USER_MODEL)),
                ('stepspace', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='space.spacemodel')),
            ],
            options={
                'verbose_name': 'Steps',
                'verbose_name_plural': 'Steps',
                'db_table': 'step_table',
            },
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('memberspace', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='space.spacemodel')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'db_table': 'message_table',
            },
        ),
    ]
