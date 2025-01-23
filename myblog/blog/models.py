from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    '''Модель поста о корги'''
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Содержание')
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Автор',
        null=True,
        blank=True
    )
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField('Фото корги', upload_to='corgi_images/%Y/%m/%d/')
    tags = models.CharField('Теги', max_length=100, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date']

class Comment(models.Model):
    '''Модель комментариев'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Комментарий')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {self.post.title}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class UserProfile(models.Model):
    '''Профиль пользователя'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Аватар', upload_to='avatars/', blank=True)
    bio = models.TextField('О себе', max_length=500, blank=True)
    favorite_corgi = models.CharField('Любимая порода корги', max_length=100, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
