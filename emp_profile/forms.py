from django import forms
from .models import EmployeeProfile


# Create your views here.
class EmployeeProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',

            })
    )
    date_of_joining = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',

        })
    )

    # date_of_retirement = forms.DateField(
    #     widget=forms.DateInput(attrs={
    #         'type': 'date',
    #     })
    # )

    class Meta:
        model = EmployeeProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_joining', 'address',
                  'city', 'state', 'zip_code', 'email', 'marital_status', 'salutation', 'highest_qualification']

