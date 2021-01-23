from django.contrib.auth import get_user_model
from django.db import models


class Chat(models.Model):
    members = models.ManyToManyField(get_user_model(), related_name='member', verbose_name="Участник")


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), verbose_name="Пользователь", on_delete=models.CASCADE)
    message = models.TextField(max_length=10000, null=False, verbose_name="Сообщение")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    is_readed = models.BooleanField(verbose_name='Прочитано', default=False)


    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return f'{self.message}'