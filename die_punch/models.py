from django import db
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    username = None
    mobile = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_user_role_1 = models.BooleanField(default=False)
    is_user_role_2 = models.BooleanField(default=False)
    is_user_role_3 = models.BooleanField(default=False)
    permissions = models.CharField(max_length = 225,null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    class Meta:
        db_table = 'user'

class Form(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50,null=True,blank=True)
    lastname = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(max_length=100,null=True,blank=True)
    age = models.CharField(max_length=10,null=True,blank=True)
    mobile = models.CharField(max_length=10,null=True,blank=True)
    salary = models.CharField(max_length=10,null=True,blank=True)
    price = models.CharField(max_length = 10,null=True,blank=True)
    networth = models.CharField(max_length=10,null=True,blank=True)
    votercard = models.CharField(max_length=20,null=True,blank=True)
    certificate = models.CharField(max_length=10,null=True,blank=True)
    class Meta:
        db_table = "form"
    def __str__(self):
        return f'{self.user}'

class CustomerDetail(models.Model):
    customerName = models.CharField(max_length=100,null=True,blank=True)
    customerMobile = models.CharField(max_length=20,null=True,blank=True)
    customerEmail = models.CharField(max_length=50,null=True,blank=True)
    customerCompanyName = models.CharField(max_length=200,null=True,blank=True)
    customerCompanyAddress = models.CharField(max_length=200,null=True,blank=True)
    customerCompanyCity = models.CharField(max_length=50,null=True,blank=True)
    customerCompanyState = models.CharField(max_length=50,null=True,blank=True)
    customerCompanyPincode = models.CharField(max_length=10,null=True,blank=True)
    class Meta:
        db_table = 'customerdetail'

  
class Moc(models.Model):
    name = models.CharField(max_length=255)

class ToolType(models.Model):
    name = models.CharField(max_length=255)

class Shape(models.Model):
    name = models.CharField(max_length=255)

class TabletSize(models.Model):
    name = models.CharField(max_length=255)

class U1(models.Model):
    name = models.CharField(max_length=255)

class U2(models.Model):
    name = models.CharField(max_length=255)

class L1(models.Model):
    name = models.CharField(max_length=255)

class L2(models.Model):
    name = models.CharField(max_length=255)

class D(models.Model):
    name = models.CharField(max_length=255)

class Set(models.Model):
    name = models.CharField(max_length=255)

class PlatingType(models.Model):
    name = models.CharField(max_length=255)

class RawMaterial(models.Model):
    name = models.CharField(max_length=255)

class PunchBlank(models.Model):
    name = models.CharField(max_length=255)

class DieBlank(models.Model):
    name = models.CharField(max_length=255)

class Blank(models.Model):
    name = models.CharField(max_length=255)

class Process(models.Model):
    name = models.CharField(max_length=255)

class BodyTipMachining(models.Model):
    name = models.CharField(max_length=255)

class HeadMachining(models.Model):
    name = models.CharField(max_length=255)

class KeywayTaperFinish(models.Model):
    name = models.CharField(max_length=255)

class HT(models.Model):
    name = models.CharField(max_length=255)

class Grinding(models.Model):
    name = models.CharField(max_length=255)

class HardChrome(models.Model):
    name = models.CharField(max_length=255)

class QualityCheck(models.Model):
    name = models.CharField(max_length=255)

class PackingDispach(models.Model):
    name = models.CharField(max_length=255)

class DispachMode(models.Model):
    name = models.CharField(max_length=255)

class ProductionData(models.Model):
    orderDate = models.CharField(max_length=50,null=True,blank=True)
    orderNumber = models.CharField(max_length=50,null=True,blank=True)
    clientName  = models.ForeignKey(CustomerDetail,on_delete=models.CASCADE)
    # client_id = models.ForeignKey(CustomerDetail,on_delete=models.CASCADE)
    value = models.CharField(max_length=50,null=True,blank=True)
    moc = models.ForeignKey(Moc,on_delete=models.CASCADE)
    toolType = models.ForeignKey(ToolType,on_delete=models.CASCADE)
    shape = models.ForeignKey(Shape,on_delete=models.CASCADE)
    tabletSize = models.ForeignKey(TabletSize,on_delete=models.CASCADE)
    u1 = models.ForeignKey(U1,on_delete=models.CASCADE)
    u2 = models.ForeignKey(U2,on_delete=models.CASCADE)
    l1 = models.ForeignKey(L1,on_delete=models.CASCADE)
    l2 = models.ForeignKey(L2,on_delete=models.CASCADE)
    d = models.ForeignKey(D,on_delete=models.CASCADE)
    set = models.ForeignKey(Set,on_delete=models.CASCADE)
    platingType = models.ForeignKey(PlatingType,on_delete=models.CASCADE)
    rawMaterial = models.ForeignKey(RawMaterial,on_delete=models.CASCADE)
    priority = models.CharField(max_length=50,null=True,blank=True)
    order_remarks = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)
    dwgNumber = models.CharField(max_length=50,null=True,blank=True)
    drgDate = models.CharField(max_length=50,null=True,blank=True)
    approvalDate = models.CharField(max_length=50,null=True,blank=True)
    master = models.CharField(max_length=50,null=True,blank=True)
    masterOut = models.CharField(max_length=50,null=True,blank=True)
    masterIn = models.CharField(max_length=50,null=True,blank=True)
    punchBlankUsed = models.ForeignKey(PunchBlank,on_delete=models.CASCADE)
    dieBlankUsed = models.ForeignKey(DieBlank,on_delete=models.CASCADE)
    hitDate = models.CharField(max_length=50,null=True,blank=True)
    estimatedDelivery = models.CharField(max_length=50,null=True,blank=True)
    planningOut = models.CharField(max_length=50,null=True,blank=True)
    planningIn = models.CharField(max_length=50,null=True,blank=True)
    
    blank = models.ForeignKey(Blank,on_delete=models.CASCADE)
    process = models.ForeignKey(Process,on_delete=models.CASCADE)
    bodyTipMachining = models.ForeignKey(BodyTipMachining,on_delete=models.CASCADE)
    headMachining = models.ForeignKey(HeadMachining,on_delete=models.CASCADE)
    keywayTaperFinish = models.ForeignKey(KeywayTaperFinish,on_delete=models.CASCADE)
    ht = models.ForeignKey(HT,on_delete=models.CASCADE)
    grinding = models.ForeignKey(Grinding,on_delete=models.CASCADE)
    hardChrome = models.ForeignKey(HardChrome,on_delete=models.CASCADE)
    qualityCheck = models.ForeignKey(QualityCheck,on_delete=models.CASCADE)
    packingDispach = models.ForeignKey(PackingDispach,on_delete=models.CASCADE)
    
    actualDelivery = models.CharField(max_length=50,null=True,blank=True)
    dispachMode = models.ForeignKey(DispachMode,on_delete=models.CASCADE)
    couriesNumber = models.CharField(max_length=50,null=True,blank=True)

    remark = models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        db_table = 'prodform'





  
class UserLog(models.Model):
    formid= models.ForeignKey(ProductionData,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    modified_date = models.DateTimeField(auto_now=True)
    orderDate = models.CharField(max_length=50,null=True,blank=True)
    orderNumber = models.CharField(max_length=50,null=True,blank=True)
    clientName  = models.CharField(max_length=50,null=True,blank=True)
    value = models.CharField(max_length=50,null=True,blank=True)
    moc = models.CharField(max_length=50,null=True,blank=True)
    toolType = models.CharField(max_length=50,null=True,blank=True)
    shape = models.CharField(max_length=50,null=True,blank=True)
    tabletSize = models.CharField(max_length=50,null=True,blank=True)
    u1 = models.CharField(max_length=50,null=True,blank=True)
    u2 = models.CharField(max_length=50,null=True,blank=True)
    l1 = models.CharField(max_length=50,null=True,blank=True)
    l2 = models.CharField(max_length=50,null=True,blank=True)
    d = models.CharField(max_length=10,null=True,blank=True)
    sett = models.CharField(max_length=50,null=True,blank=True)
    platingType = models.CharField(max_length=50,null=True,blank=True)
    rawMaterial = models.CharField(max_length=50,null=True,blank=True)
    priority = models.CharField(max_length=50,null=True,blank=True)
    order_remarks = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=50,null=True,blank=True)
    dwgNumber = models.CharField(max_length=50,null=True,blank=True)
    drgDate = models.CharField(max_length=50,null=True,blank=True)
    approvalDate = models.CharField(max_length=50,null=True,blank=True)
    master = models.CharField(max_length=50,null=True,blank=True)
    masterOut = models.CharField(max_length=50,null=True,blank=True)
    masterIn = models.CharField(max_length=50,null=True,blank=True)
    punchBlankUsed = models.CharField(max_length=10,null=True,blank=True)
    dieBlankUsed = models.CharField(max_length=10,null=True,blank=True)
    hitDate = models.CharField(max_length=50,null=True,blank=True)
    estimatedDelivery = models.CharField(max_length=50,null=True,blank=True)
    planningOut = models.CharField(max_length=50,null=True,blank=True)
    planningIn = models.CharField(max_length=50,null=True,blank=True)
    blank = models.CharField(max_length=10,null=True,blank=True)
    process = models.CharField(max_length=10,null=True,blank=True)
    bodyTipMachining = models.CharField(max_length=10,null=True,blank=True)
    headMachining = models.CharField(max_length=10,null=True,blank=True)
    keywayTaperFinish = models.CharField(max_length=10,null=True,blank=True)
    ht = models.CharField(max_length=10,null=True,blank=True)
    grinding = models.CharField(max_length=10,null=True,blank=True)
    hardChrome = models.CharField(max_length=10,null=True,blank=True)
    qualityCheck = models.CharField(max_length=10,null=True,blank=True)
    packingDispach = models.CharField(max_length=10,null=True,blank=True)
    actualDelivery = models.CharField(max_length=50,null=True,blank=True)
    dispachMode = models.CharField(max_length=50,null=True,blank=True)
    couriesNumber = models.CharField(max_length=50,null=True,blank=True)
    remark = models.CharField(max_length=100,null=True,blank=True)

    new_orderDate = models.CharField(max_length=50,null=True,blank=True)
    new_orderNumber = models.CharField(max_length=50,null=True,blank=True)
    new_clientName  = models.CharField(max_length=50,null=True,blank=True)
    new_value = models.CharField(max_length=50,null=True,blank=True)
    new_moc = models.CharField(max_length=50,null=True,blank=True)
    new_toolType = models.CharField(max_length=50,null=True,blank=True)
    new_shape = models.CharField(max_length=50,null=True,blank=True)
    new_tabletSize = models.CharField(max_length=50,null=True,blank=True)
    new_u1 = models.CharField(max_length=50,null=True,blank=True)
    new_u2 = models.CharField(max_length=50,null=True,blank=True)
    new_l1 = models.CharField(max_length=50,null=True,blank=True)
    new_l2 = models.CharField(max_length=50,null=True,blank=True)
    new_d = models.CharField(max_length=10,null=True,blank=True)
    new_sett = models.CharField(max_length=50,null=True,blank=True)
    new_platingType = models.CharField(max_length=50,null=True,blank=True)
    new_rawMaterial = models.CharField(max_length=50,null=True,blank=True)
    new_priority = models.CharField(max_length=50,null=True,blank=True)
    new_order_remarks = models.CharField(max_length=50,null=True,blank=True)
    new_status = models.CharField(max_length=50,null=True,blank=True)
    new_dwgNumber = models.CharField(max_length=50,null=True,blank=True)
    new_drgDate = models.CharField(max_length=50,null=True,blank=True)
    new_approvalDate = models.CharField(max_length=50,null=True,blank=True)
    new_master = models.CharField(max_length=50,null=True,blank=True)
    new_masterOut = models.CharField(max_length=50,null=True,blank=True)
    new_masterIn = models.CharField(max_length=50,null=True,blank=True)
    new_punchBlankUsed = models.CharField(max_length=10,null=True,blank=True)
    new_dieBlankUsed = models.CharField(max_length=10,null=True,blank=True)
    new_hitDate = models.CharField(max_length=50,null=True,blank=True)
    new_estimatedDelivery = models.CharField(max_length=50,null=True,blank=True)
    new_planningOut = models.CharField(max_length=50,null=True,blank=True)
    new_planningIn = models.CharField(max_length=50,null=True,blank=True)
    new_blank = models.CharField(max_length=10,null=True,blank=True)
    new_process = models.CharField(max_length=10,null=True,blank=True)
    new_bodyTipMachining = models.CharField(max_length=10,null=True,blank=True)
    new_headMachining = models.CharField(max_length=10,null=True,blank=True)
    new_keywayTaperFinish = models.CharField(max_length=10,null=True,blank=True)
    new_ht = models.CharField(max_length=10,null=True,blank=True)
    new_grinding = models.CharField(max_length=10,null=True,blank=True)
    new_hardChrome = models.CharField(max_length=10,null=True,blank=True)
    new_qualityCheck = models.CharField(max_length=10,null=True,blank=True)
    new_packingDispach = models.CharField(max_length=10,null=True,blank=True)

    new_actualDelivery = models.CharField(max_length=50,null=True,blank=True)
    new_dispachMode = models.CharField(max_length=50,null=True,blank=True)
    new_couriesNumber = models.CharField(max_length=50,null=True,blank=True)
    new_remark = models.CharField(max_length=100,null=True,blank=True)
    Type = models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        db_table="userlog"

