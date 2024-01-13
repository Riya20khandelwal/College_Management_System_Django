from django.shortcuts import redirect, render
# from .settings import BASE_DIR, rr

def BASE(request):
    # print(rr,2222222222222)
    return render(request, 'base.html')