from django.urls import path
from . import views
from .views import preview_and_describe


urlpatterns=[
    path('',views.index,name="index"),
    path('inputs/',views.inputs,name="inputs"),
    path('results/',views.results,name="results"),
    path('preview_and_describe/', preview_and_describe, name='preview_and_describe'),
]