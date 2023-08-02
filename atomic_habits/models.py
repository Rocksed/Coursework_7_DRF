from datetime import date

from django.db import models

from users.models import User, NULLABLE


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)
    place = models.CharField(max_length=50, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=150, verbose_name='действие')
    pleasurable_habit = models.CharField(max_length=50, verbose_name='признак приятной привычки')
    linked_habit = models.CharField(max_length=50, verbose_name='cвязанная привычка')
    frequency = models.DateField(default=date.today, verbose_name='периодичность')
    reward = models.CharField(max_length=150, verbose_name='вознаграждение')
    time_to_complete = models.DateTimeField(verbose_name='время на выполнение ')
    sign_of_publicity = models.CharField(max_length=150, verbose_name='признак публичности')

    def __str__(self):
        return f'я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'