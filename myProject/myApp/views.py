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

def counter(request):
    text=request.POST['text']
    amt=len(text.split())
    return render(request,'counter.html',{'amount':amt})

