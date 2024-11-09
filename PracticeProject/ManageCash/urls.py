from django.urls import path
from .views import *

urlpatterns = [
    path('', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('profile-management/', profile_management, name='profile_management'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-cash/', add_cash, name='add_cash'),
    path('add-expense/', add_expense, name='add_expense'),
]
