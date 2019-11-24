from django.conf import path
from .models import views

urlpattern=[
    path('',views.index)
]