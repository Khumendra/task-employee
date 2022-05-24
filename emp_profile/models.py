from django.db import models


# Create your models here.
class EmployeeProfile(models.Model):
    # SALUTATION CHOICES
    MR = 'MR'
    MRS = 'MRS'
    MISS = 'MISS'

    SALUTATION_CHOICES = [
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MISS, 'Miss'),
    ]

    # HIGHEST QUALIFICATION CHOICES
    BTECH = "BTECH"
    MTECH = "MTECH"
    BSC = "BSC"
    MSC = "MSC"
    MBA = "MBA"
    BBA = "BBA"

    HIGHEST_QUALIFICATION_CHOICES = [
        (BTECH, 'BTech'),
        (MTECH, 'MTech'),
        (BSC, "BSc"),
        (MSC, "MSc"),
        (MBA, "MBA"),
        (BBA, "BBA")
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=6)
    email = models.EmailField()
    marital_status = models.BooleanField(default=False)
    salutation = models.CharField(max_length=4, choices=SALUTATION_CHOICES, default=MR)
    highest_qualification = models.CharField(max_length=5, choices=HIGHEST_QUALIFICATION_CHOICES)


class EmployeePlans(models.Model):
    date_of_retirement = models.DateField()
