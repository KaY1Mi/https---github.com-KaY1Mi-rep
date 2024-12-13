from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # Путь для админки
    path('', views.home, name='home'),  # Главная страница
    path('courses/figma/', views.figma_course, name='figma_course'),  # Курс по Figma
    path('courses/', views.all_courses, name='all_courses'),  # Каталог курсов
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('articles/', views.article_list, name='articles'),  # URL с именем 'articles'
      path('lesson-1/', views.lesson_1, name='lesson_1'),
      path('lesson-ae/', views.lesson_ae, name='lesson_ae'),
      path('lesson-ps/', views.lesson_ps, name='lesson_ps'),
      path('lesson-t/', views.lesson_t, name='lesson_t'),
      path('lesson-2/', views.lesson_2, name='lesson_2'),
       path('color/', views.color, name='color'),  # URL для статьи "Цвет в UX/UI"
 path('courses/', views.all_courses, name='courses'),  # Каталог курсов
path('courses/ae/', views.ae_course, name='ae_course'),  # Курс по Figma
path('courses/Ph/', views.Ph_course, name='Ph_course'),  # Курс по Figma
path('courses/tilda/', views.tilda_course, name='tilda_course'),  # Курс по Figma
    path('articles/', views.article_list, name='article_list'),  # Определяем имя 'article_list'

    path('color1/', views.color1, name='color1'),  # URL для статьи "Цвет в UX/UI"
    path('color2/', views.color2, name='color2'),  # URL для статьи "Цвет в UX/UI"
    path('color3/', views.color3, name='color3'),  # URL для статьи "Цвет в UX/UI"
    path('color4/', views.color4, name='color4'),  # URL для статьи "Цвет в UX/UI"
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


