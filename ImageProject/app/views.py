from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def register(request):
    EUFO=UserModel()
    EPFO=ProfileModel()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method == 'POST' and request.FILES:
        UFDO = UserModel(request.POST)
        PFDO = ProfileModel(request.POST, request.FILES)
        if UFDO.is_valid():
            MUFDO = UFDO.save(commit=False)
            pw = UFDO.cleaned_data.get('password')
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username = MUFDO
            MPFDO.save()
            return HttpResponse('User rgistration is Done')
        return HttpResponse('invalid Data')
    return render (request,'register.html',d)