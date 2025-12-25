from django.shortcuts import render
from novenaApp.models import contactModel,Appointment,SubscribeFotter
from django.http import HttpResponse
from novenaApp.models import SingleBlogModel
from datetime import datetime,date

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
        # Get all form data
        department=request.POST.get("department","").strip()
        doctor =request.POST.get("doctor","").strip()
        appointment_date=request.POST.get("appointment_date","").strip()
        appointment_time=request.POST.get("appointment_time","").strip()
        full_name=request.POST.get("full_name","").strip()
        phone_number=request.POST.get("phone_number","").strip()
        message=request.POST.get("message","").strip()


        # Validations error list 
        errors=[]

        # Validate department
        if not department or department == "Choose Dapartment":
            errors.append("Please select the depaertment.")
        
        # validate doctor
        if not doctor or doctor == "Select Doctor":
            errors.append("Please select the doctor")

        # validate appointment_date
        if not appointment_date:
            errors.append("Please select an appointment date")
        else:
            try:
                date_obj = datetime.strptime(appointment_date, "%Y-%m-%d").date()
                #Check if data is not in the past
                if date_obj < date.today():
                    errors.append("appoinment date con not in the past.")
            except ValueError:
                errors.append("Invalide date format.")

        # validation apponment time 
        if not appointment_time or appointment_time == "Select Appoinment time":
            errors.append("Please select an appoinment time")

        # validate full name
        if not full_name:
            errors.append("Please enter your full name")
        elif len(full_name) < 3:
            errors.append("name must be at least 3 character long")

        # validate phone number
        if not phone_number:
            errors.append("Please enter your phone number.")
        elif not phone_number.replace("+","").replace("-","").replace(" ","").isdigit():
            errors.append("Phone number must contain only digits.")
        elif len(phone_number.replace("+","").replace("-","").replace(" ","")) < 10:
            errors.append("Phone number must be at least 10 digits")

        # If there are error ,return to form with error
        if errors:
            return render(request,"novenaApp/appoinment.html",{
                'errors': errors,
                'department':department,
                'doctor':doctor,
                'appointment_date':appointment_date,
                'appointment_time':appointment_time,
                'full_name':full_name,
                'phone_number':phone_number,
                'message':message

            })
        
        #Check for duplicate appoinment
        existing_appoinment= Appointment.objects.filter(
            phone_number=phone_number,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).exists()

        if existing_appoinment:
            return render(request,"novenaApp/appoinment.html",{
                'errors':['You already have an appoinmrnt scheduled at this time and date'],
                'department':department,
                'doctor':doctor,
                'appointment_date':appointment_date,
                'appointment_time':appointment_time,
                'full_name':full_name,
                'phone_number':phone_number,
                'message':message
            })
        
        #Create appoinment

        try:
            Appointment.objects.create(
                department=department,
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                full_name=full_name,
                phone_number=phone_number,
                message=message
            )

            return render(request,"novenaApp/appoinment_success.html",{
                'name':full_name
            })
        except Exception as e:
            return render(request,"novenaApp/appoinment.html",{
                'errors': [f'Error creating appoinmrnt: {str(e)}'],
                'department':department,
                'doctor':doctor,
                'appointment_date':appointment_date,
                'appointment_time':appointment_time,
                'full_name':full_name,
                'phone_number':phone_number,
                'message':message
            })
            
    return render(request,"novenaApp/appoinment.html")


def viewSubscribe(request):
    if request.method == "POST":
        subscribe= SubscribeFotter.objects.create(
            email= request.POST.get("email", "")
        )
        return render(request,"novenaApp/subscribefooter.html")
    


def viewSingleBlock(request):
    if request.method == "POST":
        email= request.POST.get("email", "")

        #Check if email exists
        if SingleBlogModel.objects.filter(email=email).exists():
            return render(request,"novenaApp/block_single.html", {
                'errors': 'You have already commented with this email.'
            })
        
        # Create the command only if email doen not exists
        message=SingleBlogModel.objects.create(
            name = request.POST.get("name",""),
            email=email,
            message=request.POST.get("message", "")
        )
        return render(request,"novenaApp/block_singleSuccesfull.html")
    return render(request,"novenaApp/block_single.html")
    
        
      