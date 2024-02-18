from django.shortcuts import HttpResponse, render


def index(request):
    """
    Функция render() не только связывает view-функцию и шаблон, но и
    позволяет передать в этот шаблон данные, сгенерированные во view-функции.
    """
    data = {
        'title': 'Главная страница',
        'text': 'Это главная страница проекта StarBlog',
    }
    return render(request, 'posts/index.html', data)


def group(request, any):
    data = {
        'title': 'Группы',
    }
    return render(request, 'posts/groups.html', data)
