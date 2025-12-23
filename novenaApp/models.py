from django.db import models

# Create your models here.

class contactModel(models.Model):
    name=models.CharField(max_length=100, blank=False ,null=False)
    email=models.EmailField(max_length=254,unique=True,blank=False,null=False)
    subject= models.CharField(max_length=100,blank=False,null=False)
    phoneNo= models.CharField(max_length=12,blank=False,null=False)
    message= models.TextField(blank=False,null=False)

    def __str__(self):
        return self.name
    

#bookappoinment

class Appointment(models.Model):
    DEPARTMENT_CHOICES = [
        ('cardiology','Cardiology'),
        ('neurology','Neurology'),
        ('orthopedics','Orthopedics'),
        ('pediatrics','Pediatrics'),
        ('gynecology','Gynecology'),
    ]

    DOCTOR_CHOICES =[
        ('dr_amit','Dr. Amit Sharma'),
        ('dr_rahul','Dr. Rahul Verma'),
        ('dr_neha','Dr. Neha Singh'),
        ('dr_pooja','Dr. Pooja Gupta'),
    ]

    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)

    doctor= models.CharField(max_length=50, choices=DOCTOR_CHOICES)

    appointment_date= models.DateField()
    appointment_time= models.TimeField()

    full_name= models.CharField(max_length=100)
    phone_number= models.CharField(max_length=15)
    message=models.TextField(blank=True,null=True)

    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name} - {self.appointment_date}"

