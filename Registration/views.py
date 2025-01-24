from django.shortcuts import render

# Create your views here.
from .models import Student_data
def index(request):
    if request.method =="POST":
        Std_Name = request.POST['name']
        Std_Email = request.POST['email']
        Std_Number = request.POST['phone']

        New_Student=Student_data(Name=Std_Name,email=Std_Email,phone=Std_Number)
        New_Student.save()
    return render(request,"Resgistration/form6.html")
