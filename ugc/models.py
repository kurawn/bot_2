from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID користувача в телеграмі',
        unique=True,
    )
    name = models.TextField(
        verbose_name='Ім`я користувача',
    )

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'


class DeepLinking(models.Model):
    referral_id = models.CharField(
        max_length=8,
        verbose_name='referral id',
    )
    user_id = models.CharField(
        max_length=8,
        verbose_name='user id',
        unique=True,
    )
    user_name = models.TextField(
        verbose_name='user name',
    )

    class Meta:
        verbose_name = 'Идентификатори'
        verbose_name_plural = 'Идентификатор'
