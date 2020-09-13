from django.shortcuts import render

def index(request):
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        profession = request.POST.get('profession')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('zip')
        print(fname," ",lname," ",profession," ",phone," ",email," ",city," ",state," ",pincode)
        return render(request,'resume.html')