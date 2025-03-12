from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from app.models import Student, Student_Notification, Student_leave, Student_feedback, Attendance, Attendance_Report, Subject, StudentResult
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
  

@login_required(login_url='/')
def STUDENT_APPLY_LEAVE(request):
    student = Student.objects.get(admin=request.user.id)
    student_leave_history = Student_leave.objects.filter(student_id = student)

    context = {
        'student_leave_history': student_leave_history,
    }
    return render(request, 'Student/apply_leave.html', context)


@login_required(login_url='/')
def STUDENT_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        student = Student.objects.get(admin=request.user.id)

        leave = Student_leave(
            student_id = student,
            date = leave_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request, 'Leave Successfully Send.')
        return redirect('student_apply_leave')

    return redirect('student_apply_leave')


@login_required(login_url='/')
def STUDENT_VIEW_ATTENDANCE(request):
    student = Student.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(course=student.course_id)

    action = request.GET.get('action')
    get_subject = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)
            
            attendance_report = Attendance_Report.objects.filter(student_id=student, attendance_id__subject_id=subject_id)
            
    context = {
        'subjects':  subjects,
        'action': action,
        'get_subject': get_subject,
        'attendance_report': attendance_report,
    }
    return render(request, 'Student/view_attendance.html', context)

def VIEW_RESULT(request):
    student = Student.objects.get(admin=request.user.id)
    result = StudentResult.objects.filter(student_id=student)

    mark = None
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark

        mark = assignment_mark + exam_mark

    context = {
        'result': result, 
        'mark': mark,
    }
    return render(request, 'Student/view_result.html', context)