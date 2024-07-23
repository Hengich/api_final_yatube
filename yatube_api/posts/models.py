from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CheckConstraint, F, Q, UniqueConstraint

User = get_user_model()

LENGTH_LIMIT = 50


class Group(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title[:LENGTH_LIMIT]


class Post(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', blank=True)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.text[:LENGTH_LIMIT]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Текст')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    class Meta():
        constraints = (
            UniqueConstraint(
                fields=('user', 'following'),
                name='unique_user_and_following'
            ),
            CheckConstraint(
                check=~Q(user=F('following')),
                name='check_follow',
            ),
        )
