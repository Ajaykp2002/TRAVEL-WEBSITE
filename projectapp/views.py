from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from . models import Team
# Create your views here.
def add(request):
    obj=place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj1})

#def Addition(request):
   # x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
 #   res=x+y
  #  res1=x-y
 #   res2=x*y
 #   res3=x/y
#    return render(request,"home.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})
#def contact(request):
 #   return render(request,"home.html")
#def details(request):
    #return render(request,"home.html")
#def thank(request):
    #retu
# rn render(request,"home.html")