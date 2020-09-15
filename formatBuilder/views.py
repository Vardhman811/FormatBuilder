from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        return HttpResponse('html')

def heading(request):
        if request.method == "POST":
        #tell me about your self
                
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

def education(request):
        if request.method == "POST":
                #tell me about your education
                        
                schoolname = request.POST.get('schoolname')
                loaction = request.POST.get('loaction')
                spercent = request.POST.get('spercent')
                syear = request.POST.get('syear')

                ugcourse = request.POST.get('ugcourse')
                ugcollege = request.POST.get('ugcollege')
                ugpass = request.POST.get('ugpass')
                ugpercent = request.POST.get('ugpercent')

                pgcourse = request.POST.get('pgcourse')
                pgcollege = request.POST.get('pgcollege')
                pgpass = request.POST.get('pgpass')
                pgpercent = request.POST.get('pgpercent')

                othercourse = request.POST.get('othercourse')
                othercollege = request.POST.get('othercollege')
                otherpass = request.POST.get('otherpass')
                otherpercent = request.POST.get('otherpercent')
                
                print(schoolname," ",loaction," ",spercent," ",syear," ",ugcourse," ",ugcollege," ",ugpass," ",ugpercent," ",pgcourse," ",pgcollege," ",pgpass," ",pgpercent," ",othercourse," ",othercollege," ",otherpass," ",otherpercent)
               
        return render(request,'education.html')

def work(request): 
        
        if request.method == "POST":
                #tell me about your work
                num = request.POST.get('num')
                print(num)
                
                jobtitle1 = request.POST.get('jobtitle1')
                employer1 = request.POST.get('employer1')
                city1 = request.POST.get('city1')
                startyear1 = request.POST.get('startyear1')
                endyear1 = request.POST.get('endyear1')
                discription1 = request.POST.get('discription1')
                
                jobtitle2 = request.POST.get('jobtitle2')
                employer2 = request.POST.get('employer2')
                city2 = request.POST.get('city2')
                startyear2 = request.POST.get('startyear2')
                endyear2 = request.POST.get('endyear2')
                discription2 = request.POST.get('discription2')
                
                jobtitle3 = request.POST.get('jobtitle3')
                employer3 = request.POST.get('employer3')
                city3 = request.POST.get('city3')
                startyear3 = request.POST.get('startyear3')
                endyear3 = request.POST.get('endyear3')
                discription3 = request.POST.get('discription3')
                
                jobtitle4 = request.POST.get('jobtitle4')
                employer4 = request.POST.get('employer4')
                city4 = request.POST.get('city4')
                startyear4 = request.POST.get('startyear4')
                endyear4 = request.POST.get('endyear4')
                discription4 = request.POST.get('discription4') 
                print(jobtitle1," ",employer2," ",city3," ",startyear4," ",endyear1," ",discription1)          
                                       
        return render(request,'work.html')

def skill(request):
        if request.method == "POST":
                #tell me about your self
                skill1 = request.POST.get('skill1')
                skill2 = request.POST.get('skill2')
                skill3 = request.POST.get('skill3')
                skill4 = request.POST.get('skill4')
                skill5 = request.POST.get('skill5')
                skill6 = request.POST.get('skill6')
                skill7 = request.POST.get('skill7')
                skill8 = request.POST.get('skill8')
                skill9 = request.POST.get('skill9')
                skill10 = request.POST.get('skill10')
                print(skill1," ",skill6)
        return render(request,'skill.html')
