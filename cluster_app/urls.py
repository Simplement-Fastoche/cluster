from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name="index"),
    path('files/',views.files,name="files"),
    path('inputs/',views.inputs,name="inputs"),
    path('results/',views.results,name="results")
]