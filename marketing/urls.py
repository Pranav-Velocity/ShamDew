from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard/',Marketing_Dashboard,name='marketing_dashboard'),
    path('create_marketing_form/',CreateMarketingForm,name='create_marketing_form'),
    path('add_marketing_form_user_1/',add_marketing_form_user_1,name="add_marketing_form_user_1")
    
]