from django.shortcuts import get_object_or_404, render

from posts.models import Group, Post


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


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:5]
    data = {
        'title': 'Группы',
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/groups.html', data)
