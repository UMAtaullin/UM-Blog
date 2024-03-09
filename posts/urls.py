from django.urls import path

from . import views

app_name = 'posts'   # pylint: disable=invalid-name

urlpatterns = [
    path('', views.index, name='home'),
    path('group/<slug:any>/', views.group_posts, name='group_posts'),
]
