from django.urls import path
from . import views

urlpatterns = [
    # Authentification
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/new_register', views.new_register, name='new_register'),
    path('dashboard/view_registers', views.view_registers, name='view_registers'),
    path('dashboard/edit_registers/', views.edit_registers, name='edit_registers'),
    path('dashboard/edit_registers/<int:register_pk>', views.edit_register_detail, name='edit_register_detail'),
    path('dashboard/help/', views.help, name='help'),
    path('inbox/', views.inbox, name='inbox'),
]