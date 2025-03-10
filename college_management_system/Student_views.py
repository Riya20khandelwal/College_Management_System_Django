from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from app.models import Student, Student_Notification, CustomUser, Staff_leave, Staff_feedback
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Student/home.html')

@login_required(login_url='/')
def NOTIFICATIONS(request):
    student = Student.objects.get(admin=request.user.id)

    notification = Student_Notification.objects.filter(student_id=student.id)

    context = {
        'notification': notification,
    }
    return render(request, 'Student/notification.html', context)


@login_required(login_url='/')
def STUDENT_NOTIFICATION_MARK_AS_DONE(request, status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('student_notifications')