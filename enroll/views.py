import email
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User


# Create your views here.
# this function for add new item and show all data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            rn = fm.cleaned_data['roll_number']
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']

            reg = User(name=nm, email=em, roll_number=rn)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


# this function for update and edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/updatestudent.html', {'form': fm})


# this function for delate data
def deletedata(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
