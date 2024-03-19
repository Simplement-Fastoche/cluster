from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.

def index (request):
    context={"active_page":"index",}
    
   
    return render(request,"cluster_app/index.html",context)
    

def files (request):
    context={"active_page":"files",}
    
    return render(request,"cluster_app/files.html",context)

def inputs (request):
    context={"active_page":"inputs",}
    
    return render(request,"cluster_app/inputs.html",context)



def results (request):
    context={"active_page":"results",}
    
    return render(request,"cluster_app/results.html",context)

