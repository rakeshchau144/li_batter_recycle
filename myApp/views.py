from django.shortcuts import render
from . models import Employee


def home(request):  
    return render(request,'home.html')

def Index(request): 
    mydata = Employee.objects.all().values()
    if request.method == 'POST':   
        email = request.POST.get('email')
        passe = request.POST.get('password')
        print(email, passe)
        print(mydata)
        Employee.objects.create(Email=email, paass = passe)
  
        # print(context)
        print(type(mydata))
       
    return render(request,'Index.html', {'data':mydata})
