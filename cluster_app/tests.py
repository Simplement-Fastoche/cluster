from django.test import TestCase
from django.urls import path
from .import views
# Create your tests here.

urlpatterns=[
    path('', views.index,name='index'),
    path('files/',views.files,name="files"),
    path('inputs/',views.inputs,name="inputs"),
    path('results/',views.results,name="results")
      
]