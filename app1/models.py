from django.db import models

class Profession(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    demand = models.TextField('Востребованность', default='Описание')
    geography = models.TextField('География', default='Описание')
    skills = models.TextField('Необходимые навыки', default='Описание')
    vacancies = models.TextField('Последние вакансии', default='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'