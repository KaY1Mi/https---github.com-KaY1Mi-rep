# Generated by Django 5.0.2 on 2024-02-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lesson_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.CharField(max_length=200),
        ),
    ]