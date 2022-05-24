from django.urls import path, include
from . import views

app_name = 'emp_profile'

urlpatterns = [
    path('', views.index, name='home'),
    path('display/', views.display, name='display'),
    # path('date_of_retirement/', views.calculate_date_of_retirement, name='date_of_retirement'),
]
