from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
def index(request):
    return render(request,'mars/index.html')

def Persons(request):
    user_list = Person.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'mars/users.html',context=user_dict)
