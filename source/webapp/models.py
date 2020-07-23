from django.db import models

STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')]

class Tasks(models.Model):
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=15, choices= STATUS_CHOICES, default='new', verbose_name='Модерация')
    task_deadline = models.DateField(default=None, null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

class Meta:
    verbose_name = "Задача"
    verbose_name_plural = "Задачи"