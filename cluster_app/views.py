from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pandas as pd


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



def preview_and_describe(request):
    if request.method == 'POST':
        file = request.FILES['file']
        
        df = pd.read_csv(file,sep=";",decimal='.',encoding='latin1')
        preview_html = df.head().to_html()
        description = df.describe().to_html()
        return render(request, 'cluster_app/preview_and_describe.html', {'preview_html': preview_html, 'description_html': description})
    return render(request, 'cluster_app/preview_and_describe.html')