from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from app.models import Student, Student_Notification, CustomUser, Staff_leave, Student_feedback
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

@login_required(login_url='/')
def STUDENT_FEEDBACK(request):
    student = Student.objects.get(admin=request.user.id)

    feedback_history = Student_feedback.objects.filter(student_id = student)

    context = {
        'feedback_history': feedback_history,
    }
    return render(request, 'Student/feedback.html', context)


@login_required(login_url='/')
def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_message = request.POST.get('feedback')

        student = Student.objects.get(admin=request.user.id)

        feedback = Student_feedback(
            student_id = student,
            feedback = feedback_message,
        )
        feedback.save()
        messages.success(request, 'Feedback Successfully Send.')
        return redirect('student_feedback')


    return render(request, 'Student/feedback.html')
  