from django.shortcuts import render

from posts.models import Post


def index(request):
    """
    Функция render() не только связывает view-функцию и шаблон, но и
    позволяет передать в этот шаблон данные, сгенерированные во view-функции.
    """
    posts = Post.objects.order_by('-pub_date')[:5]
    data = {
        'title': 'Главная страница',
        'text': 'Это главная страница проекта StarBlog',
        'posts': posts,
    }
    return render(request, 'posts/index.html', data)


def group(request, any):
    data = {
        'title': 'Группы',
    }
    return render(request, 'posts/groups.html', data)
