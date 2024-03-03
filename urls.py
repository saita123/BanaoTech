from django.urls import path 
from . import views


urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('doctor/',views.registerdoc_view,name='doctor'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
     path('patientdashboard/',views.pat_dashboard_view,name='patientdashboard')
]