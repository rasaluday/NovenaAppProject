from django.shortcuts import render
from novenaApp.models import contactModel,Appointment,SubscribeFotter,SingleBlogModel
from django.http import HttpResponse

# Create your views here.

def viewHome(request):
    resp=render(request,"novenaApp/home.html")
    return resp

def viewAbout(request):
    resp= render(request,"novenaApp/about.html")
    return resp

def viewService(request):
    resp= render(request,"novenaApp/service.html")
    return resp

def viewDepartment(request):
    resp= render(request,"novenaApp/department.html")
    return resp

def viewDepartmentSingle(request):
    resp= render(request,"novenaApp/departmentsingle.html")
    return resp

def viewDoctors(request):
    resp= render(request,"novenaApp/doctor.html")
    return resp

def viewSingleDoctors(request):
    resp= render(request,"novenaApp/singledoctor.html")
    return resp

def viewAppoinment(request):
    if request.method =="POST":
        department=request.POST.get("department")
        doctor =request.POST.get("doctor")
        appointment_date=request.POST.get("appointment_date")
        appointment_time=request.POST.get("appointment_time")
        full_name=request.POST.get("full_name")
        phone_number=request.POST.get("phone_number")
        message=request.POST.get("message")

        Appointment.objects.create(
            department=department,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            full_name=full_name,
            phone_number=phone_number,
            message=message
        )

        return render(request,"novenaApp/appoinment_success.html")
    return render(request,"novenaApp/appoinment.html")



def viewblock_sidebar(request):
    resp= render(request,"novenaApp/blocksidebar.html")
    return resp

def viewblock_single(request):
    resp = render(request,"novenaApp/block_single.html")
    return resp

def viewcontact(request):
    if request.method == "POST":
        contact= contactModel.objects.create(
            name = request.POST.get("name", ''),
            email= request.POST.get("email", ''),
            subject= request.POST.get("subject", ''),
            phoneNo= request.POST.get("phone", ''),
            message= request.POST.get("message", ''),
        )
        return render(request,'novenaApp/contactSuccess.html',{'name':contact.name})
        
    return render(request,"novenaApp/contact.html")

def viewAppoinment(request):
    if request.method =="POST":
        department=request.POST.get("department")
        doctor =request.POST.get("doctor")
        appointment_date=request.POST.get("appointment_date")
        appointment_time=request.POST.get("appointment_time")
        full_name=request.POST.get("full_name")
        phone_number=request.POST.get("phone_number")
        message=request.POST.get("message")

        Appointment.objects.create(
            department=department,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            full_name=full_name,
            phone_number=phone_number,
            message=message
        )

        return render(request,"novenaApp/appoinment_success.html")
    return render(request,"novenaApp/appoinment.html")


def viewSubscribe(request):
    if request.method == "POST":
        subscribe= SubscribeFotter.objects.create(
            email= request.POST.get("email", "")
        )
        return render(request,"novenaApp/subscribefooter.html")
    


def viewSingleBlock(request):
    if request.method == "POST":
        message= SingleBlogModel.objects.create(
            name = request.POST.get("name", ''),
            email= request.POST.get("email", ""),
            message=request.POST.get("comment", ""),
        )
        return HttpResponse("<h1>Message send succesfully</h1>")
    
    return render(request,"novenaApp/block_single.html")
    
        
      