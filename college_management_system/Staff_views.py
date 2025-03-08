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