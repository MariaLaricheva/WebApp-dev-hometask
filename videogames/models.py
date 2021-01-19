from django.db import models

# Create your models here.

from datetime import date

from django.urls import reverse


class Games(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game_detail", kwargs={"slug": self.url})

    def get_company_list(self):
        return models("game_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


class Companies(models.Model):
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    name = models.ManyToManyField(Games, verbose_name="игра", related_name="company_game")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("company_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
