from django.shortcuts import redirect, render
from app.models import Staff, Staff_Notification, CustomUser, Staff_leave
from django.contrib import messages


def HOME(request):
    return render(request, 'Staff/home.html')


def NOTIFICATIONS(request):
    staff = Staff.objects.get(admin=request.user.id)
    # staff_id = staff.id

    notification = Staff_Notification.objects.filter(staff_id=staff.id)

    context = {
        'notification': notification,
    }
    return render(request, 'Staff/notification.html', context)


def STAFF_NOTIFICATION_MARK_AS_DONE(request, status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('staff_notifications')


def STAFF_APPLY_LEAVE(request):
    return render(request, 'Staff/apply_leave.html')


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