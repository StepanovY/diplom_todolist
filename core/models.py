from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Модель 'Пользователь'. Наследуется от AbstractUser.
    """

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
