from django.db import models

from django.core.validators import FileExtensionValidator
from django.utils import timezone

LOCATION_CHOICES = (
    ('Port Blair','Port Blair'),
    ('Mayabunder', 'Mayabunder'),
    ('Nicobar','Nicobar'),
    ('Andaman &amp; Nicobar Islands-other', 'Andaman &amp; Nicobar Islands-other'),
    ('East Godavari', 'East Godavari'),
    ('Eluru', 'Eluru'),
    ('Kadapa ', 'Kadapa '),
    (' Machilipatnam ', 'Machilipatnam '),
    (' Ongole ',' Ongole '),
    (' Srikakulam ',' Srikakulam '),
    (' Vijayawada ',' Vijayawada '),
    (' Visakhapatnam ',' Visakhapatnam '),
    (' Vizianagaram ',' Vizianagaram '),
    ('Anantapur','Anantapur'),
    ('Guntakal','Guntakal'),
    ('Guntur','Guntur'),
    ('Kakinada','Kakinada'),
    ('Kurnool','Kurnool'),
    ('Nellore','Nellore'),
    ('Rajahmundry','Rajahmundry'),
    ('Tirupati','Tirupati'),
    ('Andhra Pradesh -Other','Andhra Pradesh -Other')
)

JOBROLES_CHOICES = (
    ('Accountant','Accountant'),
    ('BPO / Telecaller', 'BPO / Telecaller'),
    ('Customer Service / Tech Support','Customer Service / Tech Support'),
    ('Engineer (Core, Non-IT)','Engineer (Core, Non-IT)'),
    ('Sales / Marketing Executive','Sales / Marketing Executive'),
    ('IT - Mobile Developer','T - Mobile Developer'),
    ('IT Software-Engineer','IT Software-Engineer'),
    ('Management Trainee','Management Trainee'),
    ('Mechanic / Fitter / Production','Mechanic / Fitter / Production'),
    ('Retail / Store Executive','Retail / Store Executive'),
    ('Architect','Architect'),
    ('Content Writer','Content Writer'),
    ('Data Entry /Back Office','Data Entry /Back Office'),
    ('Doctor / Physician','Doctor / Physician'),
    ('HR / Admin','HR / Admin'),
    ('IT Hardware Engineer','IT Hardware Engineer'),
)

DEGREE_CHOICES = (
    ('B.Arch', 'B.Arch'),
    ('B.com','B.com'),
    ('B.Pharm','B.Pharm'),
    ('BBA - BBM','BBA - BBM'),
    ('BCA','BCA'),
    ('BDS','BDS'),
    ('BE - BTech','BE - BTech'),
    ('BEd','BEd'),
    ('BHM','BHM'),
    ('BSc','BSc'),
)

DEPARTMENT_CHOICES = (
    ('Aeronautical / Avionics / Aerospace', 'Aeronautical / Avionics / Aerospace'),
    ('Agricultural / Irrigation', 'Agricultural / Irrigation'),
    ('Anesthesia (DA)', 'Anesthesia (DA)'),
)

PASSIN_CHOICES = (
    ('2021','2021'),
    ('2022','2022'),
    ('2023','2023'),
)

PASSOUT_CHOICES = (
    ('2025','2025'),
    ('2024','2024'),
    ('2023','2023'),
)

COLLEGELOCATION_CHOICES = (
    ('Andaman &amp; Nicobar Islands', 'Andaman &amp; Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
)

# COLLEGENAME_CHOICES = (

# )

MARKS_CHOICES = (
    ('10th/12th/Degree - All Above 60%', '10th/12th/Degree - All Above 60%'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any', 'Any'),
)
                    
# Create your models here.
class Jobsearch(models.Model):
    job_id = models.AutoField(primary_key=True)
    jobname = models.CharField(max_length=200, blank=False)
    job = models.CharField(max_length=200, choices=JOBROLES_CHOICES, default='Port Blair')
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES, default='Accountant')
    degree = models.CharField(max_length=200, choices=DEGREE_CHOICES, default='B.Arch')
    department = models.CharField(max_length=200, choices=DEPARTMENT_CHOICES, default='Aeronautical / Avionics / Aerospace')
    passin = models.CharField(max_length=200, choices=PASSIN_CHOICES, default='2021')
    passout = models.CharField(max_length=200, choices=PASSOUT_CHOICES, default='2025')
    collegelocation = models.CharField(max_length=200, choices=COLLEGELOCATION_CHOICES, default='Andaman &amp; Nicobar Islands')
    # collegename = models.CharField(max_length=200, choices=COLLEGELOCATION_CHOICES, default='Andaman &amp; Nicobar Islands')
    marks = models.CharField(max_length=200, choices=MARKS_CHOICES, default='10th/12th/Degree - All Above 60%')
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default='Male')