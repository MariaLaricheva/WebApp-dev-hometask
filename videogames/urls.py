from django.template.context_processors import static
from django.urls import path
from django.contrib import admin

from djangoProject import settings
from . import views

urlpatterns = [
    path("", views.CompanyView.as_view()),
    path("<int:pk>/", views.CompanyDetailView.as_view(), name="company"),
    path("game/<int:pk>/", views.GameDetailView.as_view(), name="game")
]