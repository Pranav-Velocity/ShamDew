import datetime
from datetime import timedelta, date
from django import template
register = template.Library()
from die_punch.models import *

@register.filter()
def testing(id):
    get_form = ProductionData.objects.get(id = id)
    if get_form.blank:  
        data1 = get_form.blank.name
    else:
        data1 = 0
    if get_form.process:  
        data2 = get_form.process.name
    else:
        data2 = 0
    if get_form.bodyTipMachining:  
        data3 = get_form.bodyTipMachining.name
    else:
        data3 = 0
    if get_form.headMachining:  
        data4 = get_form.headMachining.name
    else:
        data4 = 0
    if get_form.keywayTaperFinish:  
        data5 = get_form.keywayTaperFinish.name
    else:
        data5 = 0
    if get_form.ht:  
        data6 = get_form.ht.name
    else:
        data6 = 0
    if get_form.grinding:  
        data7 = get_form.grinding.name
    else:
        data7 = 0
    if get_form.hardChrome:  
        data8 = get_form.hardChrome.name
    else:
        data8 = 0
    if get_form.qualityCheck:  
        data9 = get_form.qualityCheck.name
    else:
        data9 = 0
    if get_form.packingDispach:  
        data10 = get_form.packingDispach.name
    else:
        data10 = 0
    

    
    
    if data1 :
        data1 = float(data1)
    else:
        data1 = 0
    if data2 :
        data2 = float(data2)
    else:
        data2 = 0
    if data3 :
        data3 = float(data3)
    else:
        data3 = 0
    if data4 :
        data4 = float(data4)
    else:
        data4 = 0
    if data5 :
        data5 = float(data5)
    else:
        data5 = 0
    if data6 :
        data6 = float(data6)
    else:
        data6 = 0
    if data7 :
        data7 = float(data7)
    else:
        data7 = 0
    if data8 :
        data8 = float(data8)
    else:
        data8 = 0
    if data9 :
        data9 = float(data9)
    else:
        data9 = 0
    if data10 :
        data10 = float(data10)
    else:
        data10 = 0
    totaldata = (((data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10)/10) * 100)
    # print("total is :",totaldata)
    data_status = str(totaldata) + str("%") 
    print("Total Data :",data_status)
    return data_status