"""Из модуля auth импортируем функцию get_user_model"""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    """Модель для хранения постов."""
    title = models.CharField(max_length=64, verbose_name='Заголовок',
                             null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор')
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='posts',
        verbose_name='Группа')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text


class Group(models.Model):
    """Модель для выбора сообщества."""
    title = models.CharField(max_length=255, verbose_name='Название группы')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание сообщества')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title
