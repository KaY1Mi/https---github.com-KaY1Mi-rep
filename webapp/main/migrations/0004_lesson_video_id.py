# Generated by Django 5.0.2 on 2024-02-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_lesson_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video_id',
            field=models.CharField(default='s', max_length=50),
            preserve_default=False,
        ),
    ]