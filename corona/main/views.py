from django.shortcuts import render
from django.views.generic import View
from main import models


class IndexView(View):
    def get(self, request):
        main_carousels = models.MainCarousel.objects.all()
        
        context = {
            "main_carousels": main_carousels
        }

        return render(request, "index.html", context)
