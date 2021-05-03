from django.shortcuts import render,redirect
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="login" 
)


mycursor = mydb.cursor()


def vjform(request):
    if request.session['user']!=False:
        print(request.session['user'],"  hello")
        return render(request, 'vjform.html',{'mail':request.session['user']})
    else:
        return redirect('/') 

def front(request):
    if 'user' not in request.session:
        request.session['user']=False
    return render(request, 'index.html',{'mail':request.session['user']})
    
    
def select(request):
    if request.session['user']!=False:
          return render(request, 'selecttemp.html',{'mail':request.session['user']})
    else:
          return redirect('/')

def register(request):
    if request.session['user']==False:
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        print(email," ",password," ",name," ",phone)

        if request.method == 'POST':

            sql = "INSERT INTO login_details VALUES (%s, %s, %s ,%s)"
            val = (email,password,name,phone)
            mycursor.execute(sql, val)
            return redirect('/login')
        else:
            return render(request, 'register.html')
    else:
            return redirect('/')

def login(request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        #print(email," ",password)
        if request.session['user']==False:
            if request.method == 'POST':
                sql = "SELECT email,password FROM login_details WHERE email = %s"
                val = (email,)
                mycursor.execute(sql,val)
                myresult = mycursor.fetchall()
                if not myresult:
                    print("List is empty")
                    error="Enter a valid Email/Password"
                else:
                    print(myresult[0][1])
                    if(myresult[0][1]==password):
                        request.session['user'] = email
                        error=False
                        return redirect('/')
                    
                return render(request,'login.html',{'error':error})
            else:
                return render(request, 'login.html')
        else:
            return redirect('/')
        

def submit(request):
        if request.session['user']!=False:
            print(request.session['user'],"  hello")
            return render(request, 'vjform.html',{'mail':request.session['user']})
        else:
            return redirect('/')

def logout(request):
            request.session['user']=False
            return redirect('/')

def test(request):
    if request.method == 'POST':    
                fname = request.POST.get('firstname')
                lname = request.POST.get('lastname')
                profession = request.POST.get('profession')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                city = request.POST.get('city')
                state = request.POST.get('state')
                pincode = request.POST.get('zip')
                print(fname," ",lname," ",profession," ",phone," ",email," ",city," ",state," ",pincode," ")

            #tell me about your education
            
                        
                course1 = request.POST.get('course1')
                college1 = request.POST.get('college1')
                start1 = request.POST.get('start1')
                pass1 = request.POST.get('pass1')
                percent1 = request.POST.get('percent1')

                course2 = request.POST.get('course2')
                college2 = request.POST.get('college2')
                start2 = request.POST.get('start2')
                pass2 = request.POST.get('pass2')
                percent2 = request.POST.get('percent2')
                
                print(course1," ",college1," ",start1," ",pass1," ",percent1," ",course2," ",college2," ",start2," ",pass2," ",percent2," ")

                
            #tell me about your work
                work1 = request.POST.get('work1')
                company1 = request.POST.get('company1')
                workstart1 = request.POST.get('workstart1')
                workpass1 = request.POST.get('workpass1')
                workdiscription1 = request.POST.get('workdiscription1')

                work2 = request.POST.get('work2')
                company2 = request.POST.get('company2')
                workstart2 = request.POST.get('workstart2')
                workpass2 = request.POST.get('workpass2')
                workdiscription2 = request.POST.get('workdiscription2')
                
                
                print(work1," ",company1," ",workstart1," ",workpass1," ",workdiscription1," ",work1," ",company1," ",workstart1," ",workpass1," ",workdiscription1," ")   


                #tell me about your self
                skill1 = request.POST.get('skill1')
                skill2 = request.POST.get('skill2')
                skill3 = request.POST.get('skill3')
                skill4 = request.POST.get('skill4')
                skill5 = request.POST.get('skill5')
                skill6 = request.POST.get('skill6')
                skill7 = request.POST.get('skill7')
                skill8 = request.POST.get('skill8')     


                print(skill1," ",skill2," ",skill3," ",skill4," ",skill5," ",skill6," ",skill7," ",skill8," ")



                #tell me about your objective
                objective = request.POST.get('objective')
                print(objective)

                return render(request, 'vjtemp.html',{
                    'fname':fname,'lname':lname,'profession':profession,'phone':phone,'email':email,'city':city,'state':state,'pincode':pincode,
                    'course1':course1,'college1':college1,'start1':start1,'pass1':pass1,'percent1':percent1,'course2':course2,'college2':college2,'start2':start2,'pass2':pass2,'percent2':percent2,
                    'work1':work1,'company1':company1,'workstart1':workstart1,'workpass1':workpass1,'workdiscription1':workdiscription1,'work2':work2,'company2':company2,'workstart2':workstart2,'workpass2':workpass2,'workdiscription2':workdiscription2,
                    'skill1':skill1,'skill2':skill2,'skill3':skill3,'skill4':skill4,'skill5':skill5,'skill6':skill6,'skill7':skill7,'skill8':skill8,
                    'objective':objective,
                    })


def start(request):
    if request.session['user']!=False:
          return render(request, 'from1.html',{'mail':request.session['user']})
    else:
          return redirect('/')
    


def submitone(request):
    # Basic Information

    fname = request.POST['cname']
    lname = request.POST['lname']
    profession = request.POST['profession']
    mobile = request.POST['mobile']
    email = request.POST['email']
    profile = request.POST['profile']

    # Skills Tree 

    skill1 = request.POST['skill1']
    desc1 = request.POST['desc1']
    skill2 = request.POST['skill2']
    desc2 = request.POST['desc2']
    skill3 = request.POST['skill3']
    desc3 = request.POST['desc3']

    # Technical Knowledge

    tech1 = request.POST['tech1']
    tech2 = request.POST['tech2']
    tech3 = request.POST['tech3']
    tech4 = request.POST['tech4']
    tech5 = request.POST['tech5']
    tech6 = request.POST['tech6']
    tech7 = request.POST['tech7']
    tech8 = request.POST['tech8']
    tech9 = request.POST['tech9']

    # Experience

    company1 = request.POST['company1']
    position1 = request.POST['position1']
    years1 = request.POST['years1']
    posdesc1 = request.POST['posdesc1']
    company2 = request.POST['company2']
    position2 = request.POST['position2']
    years2 = request.POST['years2']
    posdesc2 = request.POST['posdesc2']
    company3 = request.POST['company3']
    position3 = request.POST['position3']
    years3 = request.POST['years3']
    posdesc3 = request.POST['posdesc3']

    # Education

    university = request.POST['university']
    degree = request.POST['degree']
    gpa = request.POST['gpa']

    return render(request, 'resume1.html',
                  {
                      'fname': fname, 'lname': lname, 'profession': profession, 'mobile': mobile, 'email': email,
                      'profile': profile,

                      'skill1': skill1, 'desc1': desc1, 'skill2': skill2, 'desc2': desc2, 'skill3': skill3,
                      'desc3': desc3,

                      'tech1': tech1, 'tech2': tech2, 'tech3': tech3, 'tech4': tech4, 'tech5': tech5, 'tech6': tech6,
                      'tech7': tech7, 'tech8': tech8, 'tech9': tech9,

                      'company1': company1, 'position1': position1, 'years1': years1, 'posdesc1': posdesc1,
                      'company2': company2, 'position2': position2, 'years2': years2, 'posdesc2': posdesc2,
                      'company3': company3, 'position3': position3, 'years3': years3, 'posdesc3': posdesc3,

                      'university': university, 'degree': degree, 'gpa': gpa

                  })


def starttwo(request):
    if request.session['user']!=False:
          return render(request, 'Newresumeform.html',{'mail':request.session['user']})
    else:
          return redirect('/')
    


def submittow(request):
    name = request.POST["name"]
    profession = request.POST["profession"]
    email = request.POST["email"]
    mobileno = request.POST["mobile"]
    address = request.POST["address"]
    linkedin = request.POST["linkedin"]
    skill1 = request.POST["skill1"]
    skill2 = request.POST["skill2"]
    skill3 = request.POST["skill3"]
    skill4 = request.POST["skill4"]
    skill5 = request.POST["skill5"]
    degree1 = request.POST["degree1"]
    degree2 = request.POST["degree2"]
    certificate = request.POST["certificate"]
    award = request.POST["award"]
    resumeobjective = request.POST["objective"]
    orgname1 = request.POST["org1"]
    position1 = request.POST["position1"]
    sd1 = request.POST["sd1"]
    ed1 = request.POST["ed1"]
    exp1desc = request.POST["exp1des"]

    orgname2 = request.POST["org2"]
    position2 = request.POST["position2"]
    sd2 = request.POST["sd2"]
    ed2 = request.POST["ed2"]
    exp2desc = request.POST["exp2des"]

    orgname3 = request.POST["org3"]
    position3 = request.POST["position3"]
    sd3 = request.POST["sd3"]
    ed3 = request.POST["ed3"]
    exp3desc = request.POST["exp3des"]

    return render(request, "Newresume.html",
                  {"name": name, "profession": profession, "email": email, "mobileno": address, "linkedin": linkedin,
                   "skill1": skill1, "skill2": skill2, "skill3": skill3, "skill4": skill4, "skill5": skill5,
                   "degree1": degree1, "degree2": degree2, "certificate": certificate, "award": award,
                   "resumeobjective": resumeobjective, "position1": position1, "orgname1": orgname1, "sd1": sd1,
                   'ed1': ed1, "exp1desc": exp1desc, "position2": position2, "orgname2": orgname2, "sd2": sd2,
                   'ed2': ed2, "exp2desc": exp2desc, "position3": position3, "orgname3": orgname3, "sd3": sd1,
                   'ed3': ed3, "exp3desc": exp3desc})

