from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import meet

# Create your views here.
def demo(request):
    obj=place.objects.all()#fetch all objects from the table place
    obj1=meet.objects.all()

    return render(request,"index.html",{'result':obj,'res':obj1})
#def addition(request):
    #x = int(request.GET['num1'])
    #y = int(request.GET['num2'])
    #res = x + y
   # sub = x - y
    #mul = x * y
    #div = x / y

   # return render(request,"addition.html",{'result':res,'subs':sub,'muls':mul,'divs':div})

#def about(request):
    #return render(request,"about.html")
#def contact(request):
    #return HttpResponse("this is contact")
#def detail(request):
    #return render(request,"detail.html")
#def  thanks(request):
   # return HttpResponse("Thank You")