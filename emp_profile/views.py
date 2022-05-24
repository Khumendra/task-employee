from django.shortcuts import render, redirect
from .forms import EmployeeProfileForm
from django.http import HttpResponse
from .models import EmployeeProfile, EmployeePlans
# calculating age
from datetime import date
from datetime import datetime


def calculate_age(date_of_birth):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age


def calculate_date_of_retirement():
    dob_list = list(EmployeeProfile.objects.values('date_of_birth'))
    # dob_list = dob_list
    print("DOB", dob_list)

    for x in dob_list:
        dob = str(x['date_of_birth'])
        print(x['date_of_birth'])
        date_object = datetime.strptime(dob, '%Y-%m-%d').date()
        print('Date Object', date_object)

        print('Date Object Year:', date_object.year)
        year = date_object.year

        print('Date Object month:', date_object.month)
        month = date_object.month

        print('Date Object day:', date_object.day)
        day = date_object.day

        retirement_date = dob.replace(str(date_object.year), str(date_object.year + 58))
        print("Retirement Date:", retirement_date)
        # EmployeePlans(date_of_retirement=retirement_date).save()

    return retirement_date


#
# print(calculate_age(date(1995, 4, 4)), "years")


# Create your views here.
def index(request):
    form = EmployeeProfileForm()
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST)
        date_of_birth = request.POST.get('date_of_birth')
        date_of_joining = request.POST.get('date_of_joining')
        # date_of_retirement = request.POST.get('date_of_retirement')

        print("DOB", date_of_birth)
        dob = date_of_birth
        date_object = datetime.strptime(dob, '%Y-%m-%d').date()
        print('Date Object', date_object)

        print('Date Object Year:', date_object.year)
        year = date_object.year

        print('Date Object month:', date_object.month)
        month = date_object.month

        print('Date Object day:', date_object.day)
        day = date_object.day

        age = calculate_age(date(year, month, day))
        print("AGE:", age)
        # print("FORM:", form)
        if (age >= 21 and age < 58):
            try:
                print("Try Form:", form)
                form.is_valid()
                form.save()
                return redirect('emp_profile:display')
            except Exception as e:
                return HttpResponse(f'{e} <h1> Invalid Form</h1>')
        else:
            return HttpResponse('Age.')

    return render(request, 'index.html', context={'form': form})


def display(request):
    employees = EmployeeProfile.objects.all().order_by('date_of_joining')
    print(calculate_date_of_retirement())
    retirements_of_employees = calculate_date_of_retirement()
    context = {'employees': employees, 'retirements_of_employees': retirements_of_employees}

    return render(request, 'display.html', context=context)
