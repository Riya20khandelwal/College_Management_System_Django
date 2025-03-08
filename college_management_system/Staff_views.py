from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from app.models import Staff, Staff_Notification, CustomUser, Staff_leave, Staff_feedback
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Staff/home.html')


@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Staff.objects.get(admin=request.user.id)
    # staff_id = staff.id

    notification = Staff_Notification.objects.filter(staff_id=staff.id)

    context = {
        'notification': notification,
    }
    return render(request, 'Staff/notification.html', context)


@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request, status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('staff_notifications')


@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.get(admin=request.user.id)
    staff_leave_history = Staff_leave.objects.filter(staff_id = staff)

    context = {
        'staff_leave_history': staff_leave_history,
    }
    return render(request, 'Staff/apply_leave.html', context)


@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        staff = Staff.objects.get(admin=request.user.id)

        leave = Staff_leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request, 'Leave Successfully Send.')
        return redirect('staff_apply_leave')

    return render(request, 'Staff/apply_leave.html')


@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    staff = Staff.objects.get(admin=request.user.id)

    feedback_history = Staff_feedback.objects.filter(staff_id = staff)

    context = {
        'feedback_history': feedback_history,
    }
    return render(request, 'Staff/feedback.html', context)


@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_message = request.POST.get('feedback')

        staff = Staff.objects.get(admin=request.user.id)

        feedback = Staff_feedback(
            staff_id = staff,
            feedback = feedback_message,
            feedback_reply = '',
        )
        feedback.save()
        messages.success(request, 'Feedback Successfully Send.')
        return redirect('staff_feedback')


    return render(request, 'Staff/feedback.html')
  