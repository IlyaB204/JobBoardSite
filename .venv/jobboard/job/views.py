from django.shortcuts import render
from .models import Vacancy

def upload_vacancy_view(request):
    return render(request, 'job/vacancy.html')


