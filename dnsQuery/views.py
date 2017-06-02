from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("Hobby Project<br><br>Author<br>-Valar")
