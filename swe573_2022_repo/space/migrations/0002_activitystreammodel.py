# Generated by Django 4.1.3 on 2022-12-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityStreamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.JSONField()),
            ],
        ),
    ]
