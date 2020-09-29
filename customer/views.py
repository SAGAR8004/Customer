from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        bname = request.POST['bname']
        phone = request.POST['number']
        email = request.POST['email']
        dob = request.POST['birthday']
        gender = request.POST['gender']
        status = request.POST['status']
        pan = request.POST['pan']
        adhar = request.POST['adhar']

        if Customer.objects.filter(phone=phone,email=email,pan=pan,adhar=adhar).exists():
            # messages.info(request,'Already Taken')
            return redirect('home.html')
        else:
            customer=Customer(cname=cname,bname=bname,phone=phone,email=email,dob=dob,gender=gender,status=status,pan=pan,adhar=adhar)
            customer.save()
            return render(request,'success.html')
    else:
        return render('/')

            
