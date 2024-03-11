from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from posts.models import Group, Post, User


def index(request):
    """
    Функция render() не только связывает view-функцию и шаблон, но и
    позволяет передать в этот шаблон данные, сгенерированные во view-функции.
    """
    post_list = Post.objects.order_by('-pub_date')

    paginator = Paginator(post_list, 2)
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    posts = paginator.get_page(page_number)

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


def profile(request, username):

    author = get_object_or_404(User, username=username)

    data = {
        'title': 'Профиль пользователя',
        'author': author,
        'posts': Post.objects.filter(id=author.id)
    }

    return render(request, 'posts/profile.html', data)


def post_detail(request, post_id):

    data = {
        'post': get_object_or_404(Post, id=post_id)
    }

    return render(request, 'posts/post_detail.html', data)
