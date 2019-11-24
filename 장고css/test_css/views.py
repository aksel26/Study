from django.shortcuts import render
from .models import test_css
# Create your views here.

def index(request):
    return render(request,"test_css/index.html")