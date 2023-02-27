from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard_admin',admin,name="admin"),
    path('adduser/',adduser,name="adduser"),
    path("adddata/",add_data,name="add_data"),
    path('deleteform/',delete_data,name="admindelete"),
    path('addcustomer/',add_customer,name="add_customer"),
    path('customerdetails/',customerCheck,name="customerdetail"),
    path('log/',user_log,name="userlog"),


    path('dashboard_creator/',index1,name="index1"),
    path('create_form/',index1Add,name="adddata1"),

    
    path('user2/',index2,name="index2"),
]