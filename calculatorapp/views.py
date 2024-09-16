from django.shortcuts import render
from django.http import HttpResponse,JsonResponse 

def index(request):
    return render(request,'calculatorapp/index.html')
def submitquery(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        mydictionary = {
            "q" : q,
            "ans" : ans,
            "Error" : False
        }
        return render(request,'calculatorapp/index.html',context=mydictionary)
    except:
        mydictionary={
            "error":True
        }
        return render(request,'calculatorapp/index.html',context=mydictionary)


        

   

# Create your views here.
