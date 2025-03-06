from django.shortcuts import redirect, render


def HOME(request):
    return render(request, 'Staff/home.html')