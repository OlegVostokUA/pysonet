from django.db import models
from django.conf import settings
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class AbstractComment(models.Model):
    """Абстрактная модель комментариев"""
    text = models.TextField(max_length=512, blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        abstract = True


class Post(models.Model):
    """ Post model
    """
    text = models.TextField(max_length=1024, blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts'
    )

    def __str__(self):
        # Post by {self.user} -
        return f'id {self.id}'

    def comments_count(self):
        return self.comments.count()


class Comment(AbstractComment, MPTTModel):
    """ Модель коментариев к постам
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.post)


