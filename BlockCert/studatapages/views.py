from django.shortcuts import render , redirect
from django.contrib.auth import login  , logout
from django.contrib import messages
from .models import login
from django.http import HttpResponse , HttpResponseRedirect


# Create your views here.

def pages(request):
  return HttpResponse('misruni ,,,, login.must ,,,,,,stupro/ ,,,,,,, certificate')

def home(request):
   return render(request , 'home.html')

def log(request):
  if request.method == 'POST':
    user = request.POST.get('logid')
    passw = request.POST.get('logpass')

    try:
      userobj = login.empAuth_objects.get(ID = user , password = passw)
      if userobj is not None:
        return render(request , 'stupro.html' , )
      else:
        return redirect('/')
        #messages.error(request, 'ID OR Password incorrect!') 
        #messages.warning(request, "User with same email already exist")

    except Exception as identifier:
      return render(request , 'login.html')
  else:
    return render(request , 'login.html')


def stuprofile(request):
  return render (request ,'stupro.html')

def ensure(request):
    if request.method == 'POST':
        user = request.POST.get('logid')
        passw = request.POST.get('logpass')

        try:
            userobj = login.empAuth_objects.get(ID=user, password=passw)
            # Check user's GPA
           
            if userobj.finance >=7000:
              if userobj.chours < 138:
                return HttpResponse('you are still student ')
              if userobj.gpa < 2.5:
                return HttpResponse('your GPA less than 2.5')
              return redirect('certificate/')
            else:
                #  handle case where GPA is below 2.0
                return HttpResponse('Financial hold')
                # messages.error(request, 'ID OR Password incorrect!')
                # messages.warning(request, "User with same email already exist")
        except Exception as identifier:
            return render(request, 'confirmation.html')
    else:
        return render(request, 'confirmation.html')

def signout(request):
    logout(request)
    return redirect('/')

def certificate(request):
  return render (request ,'certificate.html')
# def login(request):
#     if request.method =='post':
#         username= request.post.get('username')
#         password =request.post.get('password')
#         user =authenticate(request , username = username , password = password)
#         if user is not None:
#             login(request , user)
#             return redirect ('jj')
       
#          print (username,password)try:
#              user =login.empAuth_objects.get(id= username , password = password)
#              if user is not None:
#                  return render(request , 'stupro.html')
#              else:
#                  print("erorr")
#                  return redirect(request , 'login.html')
#          except Exception as identifier:
#              return redirect(request , 'login.html')

#     return render(request , 'log.html')







