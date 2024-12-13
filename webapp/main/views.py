from django.shortcuts import render
from .models import Course
# Главная страница
def home(request):
    return render(request, 'index.html')

# Курс по Figma
def figma_course(request):
    return render(request, 'FigmaFree.html')
def ae_course(request):
    return render(request, 'AeFree.html')
def Ph_course(request):
    return render(request, 'PhotoShopFree.html')
def tilda_course(request):
    return render(request, 'Tilda.html')

# Каталог курсов
def all_courses(request):
    return render(request, 'Courses.html')

# Статьи
def articles(request):
    return render(request, 'Article.html')


from django.shortcuts import render
from .models import FAQ

def faq_view(request):
    # Получаем все вопросы и ответы
    faqs = FAQ.objects.all()  # Получаем все FAQ
    return render(request, 'index.html', {'faqs': faqs})


from django.shortcuts import render
from .models import Article

from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'Article.html', {'articles': articles})


from .models import Article

from django.shortcuts import render
from .models import Article

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'Colors.html', {'article': article})


def lesson_1(request):
    return render(request, 'Lesson_1.html')  # Укажите путь к вашему шаблону для первого урока
def lesson_ae(request):
    return render(request, 'LessonAE.html')  # Укажите путь к вашему шаблону для первого урока
def lesson_ps(request):
    return render(request, 'LessonPS.html')  # Укажите путь к вашему шаблону для первого урока
def lesson_t(request):
    return render(request, 'LessonT.html')  # Укажите путь к вашему шаблону для первого урока
from django.shortcuts import render
from .models import Article  # Импортируй свою модель

from django.shortcuts import render
from .models import Article  # Импортируем модель

from django.shortcuts import render
from .models import Lesson  # Импортируй свою модель

from django.shortcuts import render
from .models import Lesson

from django.shortcuts import render
from django.http import Http404
from .models import Lesson

def lesson_2(request):
    try:
        lesson = Lesson.objects.get(id=3)  # Получаем урок по ID
    except Lesson.DoesNotExist:
        raise Http404("Урок не найден")  # Если урока с таким ID нет, выбрасываем ошибку 404

    return render(request, 'Lesson_2.html', {'lesson': lesson})



from django.shortcuts import render

def figma_course(request):
    lessons = [
        {
            'number': 1,
            'title': 'Работа с Фигма',
            'image': 'images/svg/Figma/Figma.svg',
            'progress': [1, 0.25, 0.1, 0.05]
        },
        {
            'number': 2,
            'title': 'Работа с Auto Layout',
            'image': 'images/svg/Figma/AutoLayout.svg',
            'progress': [1, 1, 0.25, 0.1]
        },
        {
            'number': 3,
            'title': 'Ui Kit, компоненты, варианты',
            'image': 'images/svg/Figma/component.svg',
            'progress': [1, 1, 1, 0.25]
        },
        {
            'number': 4,
            'title': 'Самостоятельная работа',
            'image': 'images/svg/Figma/work.svg',
            'progress': [1, 1, 1, 1]
        }
    ]

    advantages = [
    {
        'bg_color': 'primary-1',
        'icon_color': 2,
        'secondary_icon_color': 4,
        'title': 'Быстрая обратная связь',
        'description': 'Мы даем самые быстрые и подробные ответы нашим студентам. Вы можете получать до двух видеоразборов домашних заданий в день. В рамках одного проекта студенты получают 50+ ответов от куратора.'
    },
    {
        'bg_color': 'primary-2',
        'icon_color': 1,
        'secondary_icon_color': 3,
        'title': 'Полноценное наставничество',
        'description': 'Учеба у нас приравнивается к стажировке, потому что вы пройдете полноценный рабочий процесс, который соответствует работе над проектами в студиях и компаниях.'
    },
    {
        'bg_color': 'primary-3',
        'icon_color': 2,
        'secondary_icon_color': 4,
        'title': 'Возможность трудоустройства',
        'description': 'Высокий уровень подготовки наших студентов соответствует требованиям дизайн-студий, а актуальность их знаний и наличие всех необходимых навыков помогают успешно трудоустраиваться.'
    }
]
    projects = [
    {
        'image': 'images/Main_img/case1.png',
        'title': 'Hello Ganss',
        'author': 'Рамиль Шарифуллин',
        'description': 'Интернет-магазин механических клавиатур',
        'link': 'https://www.behance.net/gallery/161061005/HELLO-GANSS-LANDING-PAGE'
    },
    {
        'image': 'images/Main_img/case2.png',
        'title': 'Homespot',
        'author': 'Алина Погодаева',
        'description': 'Приложение по подбору аренды жилья с разных уголков мира',
        'link': 'https://www.behance.net/gallery/205995937/Homespot-App'
    },
    {
        'image': 'images/Main_img/case3.png',
        'title': 'Happy Lemon',
        'author': 'Валерия Ветрова',
        'description': 'Магазин Bubble Tea',
        'link': 'https://www.behance.net/gallery/204793165/HAPPY-LEMON-LANDING-PAGE-REDESIGN'
    }
]
    context = {
        'lessons': lessons,
        'advantages': advantages,
        'projects': projects,
    }

    return render(request, 'FigmaFree.html', context)

def ae_course(request):
    lessons = [
        {
            'number': 1,
            'title': 'Работа с AfterEffects',
            'image': 'images/svg/Ae.svg',
            'progress': [1, 0.25, 0.1, 0.05]
        },
        {
            'number': 2,
            'title': 'Работа с Auto Layout',
            'image': 'images/svg/Figma/AutoLayout.svg',
            'progress': [1, 1, 0.25, 0.1]
        },
        {
            'number': 3,
            'title': 'Ui Kit, компоненты, варианты',
            'image': 'images/svg/Figma/component.svg',
            'progress': [1, 1, 1, 0.25]
        },
        {
            'number': 4,
            'title': 'Самостоятельная работа',
            'image': 'images/svg/Figma/work.svg',
            'progress': [1, 1, 1, 1]
        }
    ]

    advantages = [
    {
        'bg_color': 'primary-1',
        'icon_color': 2,
        'secondary_icon_color': 4,
        'title': 'Быстрая обратная связь',
        'description': 'Мы даем самые быстрые и подробные ответы нашим студентам. Вы можете получать до двух видеоразборов домашних заданий в день. В рамках одного проекта студенты получают 50+ ответов от куратора.'
    },
    {
        'bg_color': 'primary-2',
        'icon_color': 1,
        'secondary_icon_color': 3,
        'title': 'Полноценное наставничество',
        'description': 'Учеба у нас приравнивается к стажировке, потому что вы пройдете полноценный рабочий процесс, который соответствует работе над проектами в студиях и компаниях.'
    },
    {
        'bg_color': 'primary-3',
        'icon_color': 2,
        'secondary_icon_color': 4,
        'title': 'Возможность трудоустройства',
        'description': 'Высокий уровень подготовки наших студентов соответствует требованиям дизайн-студий, а актуальность их знаний и наличие всех необходимых навыков помогают успешно трудоустраиваться.'
    }
]
    projects = [
    {
        'image': 'images/Main_img/case1.png',
        'title': 'Hello Ganss',
        'author': 'Рамиль Шарифуллин',
        'description': 'Интернет-магазин механических клавиатур',
        'link': 'https://www.behance.net/gallery/161061005/HELLO-GANSS-LANDING-PAGE'
    },
    {
        'image': 'images/Main_img/case2.png',
        'title': 'Homespot',
        'author': 'Алина Погодаева',
        'description': 'Приложение по подбору аренды жилья с разных уголков мира',
        'link': 'https://www.behance.net/gallery/205995937/Homespot-App'
    },
    {
        'image': 'images/Main_img/case3.png',
        'title': 'Happy Lemon',
        'author': 'Валерия Ветрова',
        'description': 'Магазин Bubble Tea',
        'link': 'https://www.behance.net/gallery/204793165/HAPPY-LEMON-LANDING-PAGE-REDESIGN'
    }
]
    context = {
        'lessons': lessons,
        'advantages': advantages,
        'projects': projects,
    }

    return render(request, 'AeFree.html', context)

def Ph_course(request):
    lessons = [
        {
            'number': 1,
            'title': 'Работа с Photoshop',
            'image': 'images/svg/Ps.svg',
            'progress': [1, 0.25, 0.1, 0.05]
        },
        {
            'number': 2,
            'title': 'Работа с Auto Layout',
            'image': 'images/svg/Figma/AutoLayout.svg',
            'progress': [1, 1, 0.25, 0.1]
        },
        {
            'number': 3,
            'title': 'Ui Kit, компоненты, варианты',
            'image': 'images/svg/Figma/component.svg',
            'progress': [1, 1, 1, 0.25]
        },
        {
            'number': 4,
            'title': 'Самостоятельная работа',
            'image': 'images/svg/Figma/work.svg',
            'progress': [1, 1, 1, 1]
        }
    ]

    advantages = [
    {
        'bg_color': 'primary-1',
        'icon_color': 2,
        'secondary_icon_color': 4,
        'title': 'Быстрая обратная связь',
        'description': 'Мы даем самые быстрые и подробные ответы нашим студентам. Вы можете получать до двух видеоразборов домашних заданий в день. В рамках одного проекта студенты получают 50+ ответов от куратора.'
    },
    {
        'bg_color': 'primary-2',
        'icon_color': 1,
        'secondary_icon_color': 3,
        'title': 'Полноценное наставничество',
        'description': 'Учеба у нас приравнивается к стажировке, потому что вы пройдете полноценный рабочий процесс, который соответствует работе над проектами в студиях и компаниях.'
    },
    {
        'bg_color': 'primary-3',
        'icon_color': 2,
        'secondary_icon_color': 4,
        'title': 'Возможность трудоустройства',
        'description': 'Высокий уровень подготовки наших студентов соответствует требованиям дизайн-студий, а актуальность их знаний и наличие всех необходимых навыков помогают успешно трудоустраиваться.'
    }
]
    projects = [
    {
        'image': 'images/Main_img/case1.png',
        'title': 'Hello Ganss',
        'author': 'Рамиль Шарифуллин',
        'description': 'Интернет-магазин механических клавиатур',
        'link': 'https://www.behance.net/gallery/161061005/HELLO-GANSS-LANDING-PAGE'
    },
    {
        'image': 'images/Main_img/case2.png',
        'title': 'Homespot',
        'author': 'Алина Погодаева',
        'description': 'Приложение по подбору аренды жилья с разных уголков мира',
        'link': 'https://www.behance.net/gallery/205995937/Homespot-App'
    },
    {
        'image': 'images/Main_img/case3.png',
        'title': 'Happy Lemon',
        'author': 'Валерия Ветрова',
        'description': 'Магазин Bubble Tea',
        'link': 'https://www.behance.net/gallery/204793165/HAPPY-LEMON-LANDING-PAGE-REDESIGN'
    }
]
    context = {
        'lessons': lessons,
        'advantages': advantages,
        'projects': projects,
    }

    return render(request, 'PhotoShopFree.html', context)


def tilda_course(request):
    lessons = [
        {
            'number': 1,
            'title': 'Работа с Tilda',
            'image': 'images/svg/tilda.svg',
            'progress': [1, 0.25, 0.1, 0.05]
        },
        {
            'number': 2,
            'title': 'Работа с Auto Layout',
            'image': 'images/svg/Figma/AutoLayout.svg',
            'progress': [1, 1, 0.25, 0.1]
        },
        {
            'number': 3,
            'title': 'Ui Kit, компоненты, варианты',
            'image': 'images/svg/Figma/component.svg',
            'progress': [1, 1, 1, 0.25]
        },
        {
            'number': 4,
            'title': 'Самостоятельная работа',
            'image': 'images/svg/Figma/work.svg',
            'progress': [1, 1, 1, 1]
        }
    ]

    advantages = [
    {
        'bg_color': 'primary-1',
        'icon_color': 2,
        'secondary_icon_color': 4,
        'title': 'Быстрая обратная связь',
        'description': 'Мы даем самые быстрые и подробные ответы нашим студентам. Вы можете получать до двух видеоразборов домашних заданий в день. В рамках одного проекта студенты получают 50+ ответов от куратора.'
    },
    {
        'bg_color': 'primary-2',
        'icon_color': 1,
        'secondary_icon_color': 3,
        'title': 'Полноценное наставничество',
        'description': 'Учеба у нас приравнивается к стажировке, потому что вы пройдете полноценный рабочий процесс, который соответствует работе над проектами в студиях и компаниях.'
    },
    {
        'bg_color': 'primary-3',
        'icon_color': 2,
        'secondary_icon_color': 4,
        'title': 'Возможность трудоустройства',
        'description': 'Высокий уровень подготовки наших студентов соответствует требованиям дизайн-студий, а актуальность их знаний и наличие всех необходимых навыков помогают успешно трудоустраиваться.'
    }
]
    projects = [
    {
        'image': 'images/Main_img/case1.png',
        'title': 'Hello Ganss',
        'author': 'Рамиль Шарифуллин',
        'description': 'Интернет-магазин механических клавиатур',
        'link': 'https://www.behance.net/gallery/161061005/HELLO-GANSS-LANDING-PAGE'
    },
    {
        'image': 'images/Main_img/case2.png',
        'title': 'Homespot',
        'author': 'Алина Погодаева',
        'description': 'Приложение по подбору аренды жилья с разных уголков мира',
        'link': 'https://www.behance.net/gallery/205995937/Homespot-App'
    },
    {
        'image': 'images/Main_img/case3.png',
        'title': 'Happy Lemon',
        'author': 'Валерия Ветрова',
        'description': 'Магазин Bubble Tea',
        'link': 'https://www.behance.net/gallery/204793165/HAPPY-LEMON-LANDING-PAGE-REDESIGN'
    }
]
    context = {
        'lessons': lessons,
        'advantages': advantages,
        'projects': projects,
    }

    return render(request, 'Tilda.html', context)


def color(request):
    return render(request, 'Colors.html' )
def color1(request):
    return render(request, 'Colors1.html' )
def color2(request):
    return render(request, 'Colors2.html' )
def color3(request):
    return render(request, 'Colors3.html' )
def color4(request):
    return render(request, 'Colors4.html' )


