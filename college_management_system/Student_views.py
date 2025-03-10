from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from app.models import Staff, Staff_Notification, CustomUser, Staff_leave, Staff_feedback
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Student/home.html')