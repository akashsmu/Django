from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):
    context={
        'name':'Akash',
        'age':23,
        'nationality':'Indian'
        }
    return render(requests,'index.html',context)
