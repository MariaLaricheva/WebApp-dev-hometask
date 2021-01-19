from django.shortcuts import render
from django.views.generic.base import View

from .models import Games, Companies


class CompanyView(View):
    def get(self, request):
        company = Companies.objects.all()
        return render(request, "company/company_list.html", {"company_list": company})


class CompanyDetailView(View):
    def get(self, request, pk):
        company = Companies.objects.get(id=pk)
        return render(request, "company/company_detail.html", {"company": company})


class GameDetailView(View):
    def get(self, request, pk):
        game = Games.objects.get(id=pk)
        return render(request, "company/game_detail.html", {"game": game})
