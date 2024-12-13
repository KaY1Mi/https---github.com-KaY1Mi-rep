from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()  # Здесь можно хранить ссылку на изображение
    # Если используете локальные изображения, можно использовать:
    # image = models.ImageField(upload_to='courses_images/')

    def __str__(self):
        return self.name

from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

from django.db import models

from django.db import models

from django.db import models

from ckeditor.fields import RichTextField

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    video_url = models.URLField()
    image = models.ImageField(upload_to='lessons/', default='media/lessons/figma1')


def get_default_image():
    return 'articles/2.png'

class Article(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=200, default='Default subtitle')
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', default=get_default_image)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
