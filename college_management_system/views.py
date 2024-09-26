from django.shortcuts import redirect, render
from student.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
# from .settings import BASE_DIR, rr

def BASE(request):
    # print(rr,2222222222222)
    return render(request, 'base.html')

def LOGIN(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         )
        return None