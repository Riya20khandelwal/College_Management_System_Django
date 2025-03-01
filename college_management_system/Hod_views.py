from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Hod/home.html')

@login_required(login_url='/')
def ADD_STUDENT(request):
    return render(request, 'Hod/add_student.html')