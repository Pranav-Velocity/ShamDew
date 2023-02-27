from django.db import models
from die_punch.models import *
# Create your models here.

class ClientDetails(models.Model):
    client = models.ForeignKey(CustomerDetail,on_delete=models.CASCADE)
    contact_no = models.BigIntegerField(blank=True,default=0,unique=True)
    contact_person = models.CharField(max_length=100,blank=True,default="")
    designtion = models.CharField(max_length=100,blank=True,default="")
    email = models.EmailField(max_length=100,unique=True)
    address = models.CharField(max_length=100,blank=True,default="")
    place = models.CharField(max_length=100,blank=True,default="")
    state = models.CharField(max_length=100,blank=True,default="")
    class Meta:
        db_table = "client_details"

class MarketingForm(models.Model):
    client = models.ForeignKey(ClientDetails,on_delete=models.CASCADE)
    enquiry_date = models.DateField(auto_now_add=False,blank=True,null=True)
    month = models.CharField(max_length=100,blank=True,default="")
    enquiry_received_by = models.CharField(max_length=100,blank=True,default="")
    enquiry_mode = models.CharField(max_length=100,blank=True,default="")
    quotation_ref_no = models.CharField(max_length=100,blank=True,default="")
    quotation_given_by = models.CharField(max_length=100,blank=True,default="")
    date = models.DateField(auto_now_add=False,blank=True,null=True)
    quotation_mode = models.CharField(max_length=100,blank=True,default="")
    quotation_remark = models.CharField(max_length=100,blank=True,default="")
    next_follow_up_date  = models.DateField(auto_now_add=False,blank=True,null=True)
    done_by = models.CharField(max_length=100,blank=True,default="")
    status = models.CharField(max_length=100,blank=True,default="")
    po_number  = models.CharField(max_length=100,blank=True,default="")
    po_date = models.DateField(auto_now_add=False,blank=True,null=True)
    po_received_on = models.DateField(auto_now_add=False,blank=True,null=True)
    po_mode = models.CharField(max_length=100,blank=True,default="")
    po_amount = models.BigIntegerField(blank=True,default=0)
    po_others = models.CharField(max_length=100,blank=True,default="")
    po_tax = models.FloatField(blank=True,default=0.0)
    po_total_amount = models.FloatField(blank=True,default=0.0)
    po_amount_recieved = models.FloatField(blank=True,default=0.0)
    po_balance_amount = models.FloatField(blank=True,default=0.0)
    po_payment_terms = models.CharField(max_length=100,blank=True,default="")
    po_payment_recieved_on = models.DateField(auto_now_add=False,blank=True,null=True)
    po_payment_details = models.CharField(max_length=100,blank=True,default="")
    po_payment_details_mode = models.CharField(max_length=100,blank=True,default="")
    po_account = models.CharField(max_length=100,blank=True,default="")
    po_material_to_be_dispatched_by = models.CharField(max_length=100,blank=True,default="")
    po_bill_no = models.CharField(max_length=100,blank=True,default="")
    po_bill_date = models.DateField(auto_now_add=False,blank=True,null=True)
    dispatch_material_dispatched_on  = models.DateField(auto_now_add=False,blank=True,null=True)
    dispatch_done_by = models.CharField(max_length=100,blank=True,default="")
    dispatch_courier_details = models.CharField(max_length=100,blank=True,default="")
    dispatch_destination = models.CharField(max_length=100,blank=True,default="")
    form_creation_date = models.DateTimeField(auto_now_add=True)
    form_modified_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50,null=True,blank=True)
    modified_by = models.CharField(max_length=50,null=True,blank=True)
    class Meta:
        db_table = "marketing_form"