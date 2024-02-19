from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]


admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Посты сайта"
