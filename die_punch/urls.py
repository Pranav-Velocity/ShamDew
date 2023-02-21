from django.urls import path
from .views import *
urlpatterns = [
    path('admin',admin,name="admin"),
    path('adduser/',adduser,name="adduser"),
    path("adddata/",add_data,name="add_data"),
    path('delete/',delete_data,name="admindelete"),
    path('addcustomer/',add_customer,name="add_customer"),
    path('customerdetail/',customerCheck,name="customerdetail"),
    path('log/',user_log,name="userlog"),


    path('user1/',index1,name="index1"),
    path('add_data1/',index1Add,name="adddata1"),

    
    path('user2/',index2,name="index2"),
]