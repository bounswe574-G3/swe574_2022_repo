# Generated by Django 4.1.3 on 2022-12-06 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to=settings.AUTH_USER_MODEL)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='space.spacemodel')),
                ('takers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=300)),
                ('option1', models.CharField(max_length=50)),
                ('option2', models.CharField(max_length=50)),
                ('option3', models.CharField(max_length=50)),
                ('option4', models.CharField(max_length=50)),
                ('answer', models.CharField(blank=True, max_length=100, null=True)),
                ('help_link', models.URLField(blank=True, default=None, null=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.quizmodel')),
            ],
        ),
    ]
