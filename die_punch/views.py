from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect , HttpResponseRedirect
from .models import *
from .serializers import *
from marketing.views import GetPermission
from django.db.models import Q
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
import datetime

def IndexLogin(request):
    error=""
    print("yes")
    # user_id = int()
    # if request.user.is_authenticated:
    #     user_id = request.user.id
    #     print(user_id)
    if request.method == "POST":
        uemail = request.POST.get('email')
        upass = request.POST.get('password')
        print(uemail)
        print(upass)
        authen = authenticate(username = uemail,password = upass)
        if authen:
            user_loggedin = User.objects.get(email = authen)
            if user_loggedin.is_superuser == True:
                print("logged in user is user admin")
                login(request,authen)
                return redirect('admin')
            elif user_loggedin.is_user_role_1 == True:
                print("logged in user is user 1")
                login(request,authen)
                return redirect('index1')
            elif user_loggedin.is_user_role_2 == True:
                print("logged in user is user 2")
                login(request,authen)
                return redirect('index2')
        else:
            error="yes"
    params={
        "error":error
    }
    return render(request,"indexlogin.html",params)
    # shamdew.sharpefforts.com
    # sharpeff_shamdew
    # sharpeff_shamdew_user
    # -0hEw^UBy]dP

def index1(request):
    if request.user.is_user_role_1:
        if request.method == 'POST':
            order_number = request.POST.get('abc')
            if order_number:
                data = ProductionData.objects.get(orderNumber=order_number)
                production_data_serializer = ProductionDataSerializer(data,many=False)
                return JsonResponse({"passdata":production_data_serializer.data})
            
            update_orderdate = request.POST.get('update_orderdate')
            update_ordernumber = request.POST.get('update_ordernumber')
            update_clientname = request.POST.get('update_clientname')
            update_value = request.POST.get('update_value')
            # print("value is :",value1)
            update_moc = request.POST.get('update_moc')
            update_tooltype = request.POST.get('update_tooltype')
            update_shape = request.POST.get('update_shape')
            update_tabletsize = request.POST.get('update_tabletsize')
            update_u1 = request.POST.get('update_u1')
            update_u2 = request.POST.get('update_u2')
            update_l1 = request.POST.get('update_l1')
            update_l2 = request.POST.get('update_l2')
            update_d = request.POST.get('update_d')
            update_set = request.POST.get('update_set')
            update_platingtype = request.POST.get('update_platingtype')
            update_orderremark = request.POST.get('update_orderremark')
            update_form_id = request.POST.get('update_form_id')
            update_actualdeliverydate = request.POST.get('update_actualdeliverydate')
            update_modeofdispatch = request.POST.get('update_modeofdispatch')
            update_couriernumber = request.POST.get('update_couriernumber')
            if update_orderdate or update_ordernumber or update_clientname or update_value or update_moc or update_tooltype or update_shape or update_tabletsize or update_u1 or update_u2 or update_u2 or update_l1 or update_l2 or update_d or update_set or update_platingtype or update_orderremark or update_form_id or update_actualdeliverydate or update_modeofdispatch or update_couriernumber:
                print(update_orderdate , update_ordernumber , update_clientname , update_value , update_moc , update_tooltype , update_shape , update_tabletsize , update_u1 , update_u2 , update_l1 , update_l2 , update_d , update_set , update_platingtype , update_orderremark , update_form_id , update_actualdeliverydate , update_modeofdispatch , update_couriernumber)
                update_form = ProductionData.objects.get(id=update_form_id)
                update_form.orderDate = update_orderdate
                update_form.orderNumber = update_ordernumber
                update_form.clientName = CustomerDetail.objects.get(id=update_clientname)
                update_form.value = update_value
                update_form.moc = Moc.objects.get(id=update_moc)
                update_form.toolType = ToolType.objects.get(id=update_tooltype)
                update_form.shape = Shape.objects.get(id=update_shape)
                update_form.tabletSize = TabletSize.objects.get(id=update_tabletsize)
                update_form.u1 = U1.objects.get(id=update_u1)
                update_form.u2 =U2.objects.get(id=update_u2)
                update_form.l1 = L1.objects.get(id=update_l1)
                update_form.l2= L2.objects.get(id=update_l2)
                update_form.d = D.objects.get(id=update_d)
                update_form.set = Set.objects.get(id=update_set)
                update_form.platingType = PlatingType.objects.get(id=update_platingtype)
                update_form.user_1_remarks = update_orderremark
                update_form.actualDelivery = update_actualdeliverydate
                update_form.dispachMode = DispachMode.objects.get(id=update_modeofdispatch)
                update_form.couriesNumber = update_couriernumber
                update_form.save()
                return redirect('index1')




   
        params = {
            "tabledata":ProductionData.objects.all(),
            "CustomerDetail":CustomerDetail.objects.all(),
            "Moc":Moc.objects.all(),
            "ToolType":ToolType.objects.all(),
            "Shape":Shape.objects.all(),
            "TabletSize":TabletSize.objects.all(),
            "U1":U1.objects.all(),
            "U2":U2.objects.all(),
            "L1":L1.objects.all(),
            "L2":L2.objects.all(),
            "D":D.objects.all(),
            "Set":Set.objects.all(),
            "PlatingType":PlatingType.objects.all(),
            "DispachMode":DispachMode.objects.all(),
            "permissions":GetPermission(request.user)
        }
        return render(request,"user1/dashboard_user1.html",params)

def index1Add(request):
    if request.user.is_user_role_1:
        if request.method == "POST":
            orderdate = request.POST.get('orderdate')
            ordernumber = request.POST.get('ordernumber')
            clientname = request.POST.get('clientname')
            value = request.POST.get('value')
            moc = request.POST.get('moc')
            tooltype = request.POST.get('tooltype')
            shape = request.POST.get('shape')
            tabletsize = request.POST.get('tabletsize')
            u1 = request.POST.get('u1')
            u2 = request.POST.get('u2')
            l1 = request.POST.get('l1')
            l2 = request.POST.get('l2')
            d = request.POST.get('d')
            set = request.POST.get('set')
            platingtype = request.POST.get('platingtype')
            user_1_remarks = request.POST.get('orderremark')
            # rawmaterial = request.POST.get('rawmaterial')
            # priority = request.POST.get('priority')
            
            # edd = request.POST.get('edd')
            actualdeliverydate = request.POST.get('actualdeliverydate')
            modeofdispatch = request.POST.get('modeofdispatch')
            couriernumber = request.POST.get('couriernumber')
            print(orderdate , ordernumber , clientname , value , moc , tooltype , shape , tabletsize , u1 , u2 , l1 , l2 , d , set , platingtype , user_1_remarks , user_1_remarks , actualdeliverydate , modeofdispatch ,couriernumber)
            if orderdate or clientname or value or moc or tooltype or shape or tabletsize or u1 or u2 or l1 or l2 or d or set or platingtype or actualdeliverydate or modeofdispatch or couriernumber :
                type="New Form"
                formadd = ProductionData(
                    orderDate=orderdate,
                    orderNumber=ordernumber,
                    clientName=CustomerDetail.objects.get(id=clientname),
                    value=value,
                    moc=Moc.objects.get(id = moc),
                    toolType=ToolType.objects.get(id = tooltype),
                    shape=Shape.objects.get(id = shape),
                    tabletSize=TabletSize.objects.get(id = tabletsize),
                    u1=U1.objects.get(id = u1),
                    u2=U2.objects.get(id = u2),
                    l1=L1.objects.get(id = l1),
                    l2=L2.objects.get(id = l2),
                    d=D.objects.get(id = d),
                    set=Set.objects.get(id = set),
                    platingType=PlatingType.objects.get(id = platingtype),
                    user_1_remarks=user_1_remarks,
                    actualDelivery=actualdeliverydate,
                    dispachMode=DispachMode.objects.get(id = modeofdispatch),
                    couriesNumber=couriernumber
                    )
                # log = UserLog(user_id=request.user.id,user_name=request.user.username,new_orderDate=orderdate,new_orderNumber=ordernumber ,new_clientName=clientname ,new_value=value ,new_moc=moc ,new_toolType=tooltype  ,new_shape=shape  ,new_tabletSize=tabletsize  ,new_u1=u1  ,new_u2=u2  ,new_l1=l1  ,new_l2=l2  ,new_d=d  ,new_sett=set  ,new_platingType=platingtype,new_order_remarks=orderremark,new_actualDelivery=actualdeliverydate ,new_dispachMode=modeofdispatch ,new_couriesNumber=couriernumber,Type=type)
                
                if formadd:
                    formadd.save()
                    # log.save()
                    return redirect('index1')
        
        params = {
            "CustomerDetail":CustomerDetail.objects.all(),
            "Moc":Moc.objects.all(),
            "ToolType":ToolType.objects.all(),
            "Shape":Shape.objects.all(),
            "TabletSize":TabletSize.objects.all(),
            "U1":U1.objects.all(),
            "U2":U2.objects.all(),
            "L1":L1.objects.all(),
            "L2":L2.objects.all(),
            "D":D.objects.all(),
            "Set":Set.objects.all(),
            "PlatingType":PlatingType.objects.all(),
            "DispachMode":DispachMode.objects.all(),
            "permissions":GetPermission(request.user)
        }
        return render(request,"user1/1add.html",params)




def index2(request):
    if request.user.is_user_role_2:
        if request.method == 'POST':
            get_data = request.POST.get('abc')
            if get_data:
                check = ProductionData.objects.get(orderNumber=get_data)
                punchblank = int(check.u1.name) + int(check.l1.name)
                dieblank = int(check.d.name)
                production_data_serializer = ProductionDataSerializer(check,many=False)
                return JsonResponse({"passdata":production_data_serializer.data,"punch_blank":punchblank,'die_blank':dieblank})
            update_form_id = request.POST.get('update_form_id')
            rawmaterial = request.POST.get('update_rawmaterial')
            priority = request.POST.get('update_priority')
            dwgnumber = request.POST.get('update_dwgnumber')
            drgdate = request.POST.get('update_drgdate')
            approvaldate = request.POST.get('update_approvaldate')
            master = request.POST.get('update_master')
            masterout = request.POST.get('update_masterout')
            masterin = request.POST.get('update_masterin')
            htdate = request.POST.get('update_htdate')
            estimateddelivery = request.POST.get('update_estimateddelivery')
            planningout = request.POST.get('update_planningout')
            planningin = request.POST.get('update_planningin')
            blank = request.POST.get('update_blank')
            process = request.POST.get('update_process')
            bodytipping = request.POST.get('update_bodytipping')
            headmachine = request.POST.get('update_headmachine')
            keyway = request.POST.get('update_keyway')
            ht = request.POST.get('update_ht')
            grinding = request.POST.get('update_grinding')
            hardchrome = request.POST.get('update_hardchrome')
            qualitycheck = request.POST.get('update_qualitycheck')
            packingdispach = request.POST.get('update_packingdispach')
            if update_form_id or rawmaterial or priority or dwgnumber or drgdate or approvaldate or master or masterout or masterin or htdate or estimateddelivery or planningout or planningin or blank or process or bodytipping or  headmachine or keyway or ht or grinding or hardchrome or qualitycheck or packingdispach:
                get_form = ProductionData.objects.get(id=update_form_id)
                get_form.rawMaterial = RawMaterial.objects.get(id=rawmaterial)
                get_form.priority = priority
                get_form.dwgNumber = dwgnumber
                get_form.drgDate = drgdate
                get_form.approvalDate = approvaldate
                get_form.master = master
                get_form.masterOut = masterout
                get_form.masterIn = masterin
                get_form.hitDate = htdate
                get_form.estimatedDelivery = estimateddelivery
                get_form.planningOut = planningout
                get_form.planningIn = planningin
                get_form.blank = Blank.objects.get(id = blank)
                get_form.process = Process.objects.get(id = process)
                get_form.bodyTipMachining = BodyTipMachining.objects.get(id = bodytipping)
                get_form.headMachining = HeadMachining.objects.get(id = headmachine)
                get_form.keywayTaperFinish = KeywayTaperFinish.objects.get(id = keyway)
                get_form.ht = HT.objects.get(id = ht)
                get_form.grinding = Grinding.objects.get(id = grinding)
                get_form.hardChrome = HardChrome.objects.get(id = hardchrome)
                get_form.qualityCheck = QualityCheck.objects.get(id = qualitycheck)
                get_form.packingDispach = PackingDispach.objects.get(id = packingdispach)
                get_form.save()
                return redirect('index2')
                
                
    # rawmaterial = ""
    # priority=""
    # update_punchBlankUsed = ""
    # update_dieBlankUsed = ""
    # errlogin=""
    # alerta = ""
    # a=""
    # user_name=""
    # tabledata= []
    # placeholderdata = []
    # update = ""
    # updateform = ""
    # mobile = ""
    # salary = ""
    # test = ""
    # updateplaceholder = []
    # blanklist = []
    # processlist = []
    # bodyTipMachininglist = []
    # headMachininglist = []
    # keywayTaperFinishlist = []
    # htlist = []
    # grindinglist = []
    # hardChromelist = []
    # qualityChecklist = []
    # packingDispachlist = []
    # rawmateriallist= []
    # blankdata = AutoAddManufacturing.objects.filter(blank__isnull = False).order_by('blank')
    # for i in blankdata:
    #     blanklist.append(i.blank)
    # processdata = AutoAddManufacturing.objects.filter(process__isnull = False).order_by('process')
    # for i in processdata:
    #     processlist.append(i.process)
    # bodyTipMachiningdata = AutoAddManufacturing.objects.filter(bodyTipMachining__isnull = False).order_by('bodyTipMachining')
    # for i in bodyTipMachiningdata:
    #     bodyTipMachininglist.append(i.bodyTipMachining)
    # headMachiningdata = AutoAddManufacturing.objects.filter(headMachining__isnull = False).order_by('headMachining')
    # for i in headMachiningdata:
    #     headMachininglist.append(i.headMachining)
    # keywayTaperFinishdata = AutoAddManufacturing.objects.filter(keywayTaperFinish__isnull = False).order_by('keywayTaperFinish')
    # for i in keywayTaperFinishdata:
    #     keywayTaperFinishlist.append(i.keywayTaperFinish)
    # htdata = AutoAddManufacturing.objects.filter(ht__isnull = False).order_by('ht')
    # for i in htdata:
    #     htlist.append(i.ht)
    # grindingdata = AutoAddManufacturing.objects.filter(grinding__isnull = False).order_by('grinding')
    # for i in grindingdata:
    #     grindinglist.append(i.grinding)
    # hardChromedata = AutoAddManufacturing.objects.filter(hardChrome__isnull = False).order_by('hardChrome')
    # for i in hardChromedata:
    #     hardChromelist.append(i.hardChrome)
    # qualityCheckdata = AutoAddManufacturing.objects.filter(qualityCheck__isnull = False).order_by('qualityCheck')
    # for i in qualityCheckdata:
    #     qualityChecklist.append(i.qualityCheck)
    # packingDispachdata = AutoAddManufacturing.objects.filter(packingDispach__isnull = False).order_by('packingDispach')
    # for i in packingDispachdata:
    #     packingDispachlist.append(i.packingDispach)
    # dispatchlist = []
    # dispatchdata = AutoAddDispatch.objects.filter(dispachMode__isnull = False).order_by('dispachMode')
    # for i in dispatchdata:
    #     dispatchlist.append(i.dispachMode)
    # rawmaterialdata = AutoAddMain.objects.filter(rawMaterial__isnull = False)
    # for i in rawmaterialdata:
    #     rawmateriallist.append(i.rawMaterial)
    # placeholder = {
    #     "blank" : blanklist,
    #     "process":processlist,
    #     "bodyTipMachining":bodyTipMachininglist,
    #     "headMachining":headMachininglist,
    #     "keywayTaperFinish":keywayTaperFinishlist,
    #     "ht":htlist,
    #     "grinding":grindinglist,
    #     "hardChrome":hardChromelist,
    #     "qualityCheck":qualityChecklist,
    #     "packingDispach":packingDispachlist,
    #     "dispachMode" : dispatchlist,
    #     "rawmaterial":rawmateriallist
    # }
    
    # if request.method == 'POST':
    #     test = request.POST.get('abc')
    #     print("test data is :",test)
    #     rawmaterial = request.POST.get('rawmaterial')
    #     priority = request.POST.get('priority')
    #     print(rawmaterial , priority)
    #     dwgnumber = request.POST.get('dwgnumber')
    #     drgdate = request.POST.get('drgdate')
    #     approvaldate = request.POST.get('approvaldate')
    #     master = request.POST.get('master')
    #     masterout = request.POST.get('masterout')
    #     masterin = request.POST.get('masterin')
    #     htdate = request.POST.get('htdate')
    #     estimateddelivery = request.POST.get('estimateddelivery')
    #     planningout = request.POST.get('planningout')
    #     planningin = request.POST.get('planningin')
    #     # print(dwgnumber)
    #     # print(drgdate)
    #     # print(approvaldate)
    #     # print(master)
    #     # print(masterout)
    #     # print(masterin)
    #     # print(htdate)
    #     # print(estimateddelivery)
    #     # print(planningout)
    #     # print(planningin)

    #     blank = request.POST.get('blank')
    #     process = request.POST.get('process')
    #     bodytipping = request.POST.get('bodytipping')
    #     headmachine = request.POST.get('headmachine')
    #     keyway = request.POST.get('keyway')
    #     ht = request.POST.get('ht')
    #     grinding = request.POST.get('grinding')
    #     hardchrome = request.POST.get('hardchrome')
    #     qualitycheck = request.POST.get('qualitycheck')
    #     packingdispach = request.POST.get('packingdispach')

    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
        
    #     updateform = request.POST.get('updateform')
        
    #     if username and password:
    #         query = User.objects.filter(Q(username=username))
    #         if query:
    #             for i in query:
    #                 userid=i.id
    #                 userlvl = UserLevel.objects.get(user_id=userid)
    #                 level = userlvl.level
    #                 # print("logged in userlevel is :",level)
    #                 superuser = i.is_superuser
    #                 if superuser == False and level == 2:
    #                     authen = authenticate(username=username, password=password)
    #                     if authen:
    #                         login(request, authen)
    #                     else:
    #                         errlogin = "invalid"
    #                 else:
    #                     errlogin = "invalid"
    #         else:
    #             errlogin = "invalid"
    #     # if username and password:
    #     #     query = User.objects.filter(Q(username=username))
    #     #     for i in query:
    #     #         superuser = i.is_superuser
    #     #         if superuser == False:
    #     #             authen = authenticate(username=username, password=password)
    #     #             if authen:
    #     #                 login(request, authen)
    # else:
    #     dwgnumber = ""
    #     drgdate = ""
    #     approvaldate = ""
    #     master = ""
    #     masterout = ""
    #     masterin = ""
    #     htdate = ""
    #     estimateddelivery = ""
    #     planningout = ""
    #     planningin = ""

    #     blank = ""
    #     process = ""
    #     bodytipping = ""
    #     headmachine = ""
    #     keyway = ""
    #     ht = ""
    #     grinding = ""
    #     hardchrome = ""
    #     qualitycheck = ""
    #     packingdispach = ""
    # if request.user.is_user_role_2:
        # user_id = request.user.id
        # user_name = request.user.first_name
        # # print("logedin user name is :",user_name)
        # # print("loged in user is:",user_id)
        # lvl = 2
        # if lvl == 2:
        #     a="yes"
        # else:
        #     a='no'
        
        # form = ProductionData.objects.all()
        # for xj in form:
        #     data_id= xj.id
        #     data_orderdate1  = xj.orderDate
        #     data_orderdate = datetime.datetime.strptime(data_orderdate1, "%Y-%m-%d").strftime("%d-%m-%Y")
        #     data_ordernumber    = xj.orderNumber
        #     data_clientname =xj.clientName
        #     data_value =xj.value
        #     data_moc = xj.moc
        #     data_tooltype =xj.toolType
        #     data_shape =xj.shape
        #     data_tabletsize =xj.tabletSize
        #     data_u1 =xj.u1
        #     data_u2 =xj.u2
        #     data_l1 =xj.l1
        #     data_l2 =xj.l2
        #     data_d =xj.d
        #     data_set =xj.sett
        #     data_platingtype =xj.platingType
        #     data_rawmaterial =xj.rawMaterial
        #     data_priority =xj.priority
        #     data_orderremark = xj.order_remarks
        #     data_edd = xj.estimatedDelivery
        #     data_actualdd=xj.actualDelivery
            
        #     # print("edd :",data_edd)
        #     # print("actual edd :",data_actualdd)
            # data1 = xj.blank
            # data2 = xj.process
            # data3 = xj.bodyTipMachining
            # data4 = xj.headMachining
            # data5 = xj.keywayTaperFinish
            # data6 = xj.ht
            # data7 = xj.grinding
            # data8 = xj.hardChrome
            # data9 = xj.qualityCheck
            # data10 = xj.packingDispach
            
            
            # if data1 :
            #     data1 = float(data1)
            # else:
            #     data1 = 0
            # if data2 :
            #     data2 = float(data2)
            # else:
            #     data2 = 0
            # if data3 :
            #     data3 = float(data3)
            # else:
            #     data3 = 0
            # if data4 :
            #     data4 = float(data4)
            # else:
            #     data4 = 0
            # if data5 :
            #     data5 = float(data5)
            # else:
            #     data5 = 0
            # if data6 :
            #     data6 = float(data6)
            # else:
            #     data6 = 0
            # if data7 :
            #     data7 = float(data7)
            # else:
            #     data7 = 0
            # if data8 :
            #     data8 = float(data8)
            # else:
            #     data8 = 0
            # if data9 :
            #     data9 = float(data9)
            # else:
            #     data9 = 0
            # if data10 :
            #     data10 = float(data10)
            # else:
            #     data10 = 0
            
            # totaldata = (((data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10)/10) * 100)
            # # print("total is :",totaldata)
            # data_status = str(totaldata) + str("%") 
            
        #     if data_orderdate and data_ordernumber and data_clientname and data_value and data_moc and data_tooltype and data_shape and data_tabletsize and data_u1 and data_u2 and data_l1 and data_l2 and data_d and data_set and data_platingtype  :
        #         obj = {
        #         "id":data_id,
        #         "orderdate" : data_orderdate,
        #         "ordernumber" :data_ordernumber,
        #         "clientname" :data_clientname,
        #         "value" :data_value,
        #         "moc" :data_moc,
        #         "tooltype" :data_tooltype,
        #         "shape" :data_shape,
        #         "tabletsize" :data_tabletsize,
        #         "u1" :data_u1,
        #         "u2" :data_u2,
        #         "l1" :data_l1,
        #         "l2" :data_l2,
        #         "d" :data_d,
        #         "set" :data_set,
        #         "platingtype" :data_platingtype,
        #         "rawmaterial" :data_rawmaterial,
        #         "priority" :data_priority,
        #         "remarks":data_orderremark,
        #         "status" :data_status,
        #         'edd':data_edd,
        #         'actualdeliverydate':data_actualdd
        #     }
        #     tabledata.append(obj)
        
        # if test:
        #     udata = ProductionData.objects.get(orderNumber = test)
        #     print(udata)
        #     data1 = udata.blank
        #     data2 = udata.process
        #     data3 = udata.bodyTipMachining
        #     data4 = udata.headMachining
        #     data5 = udata.keywayTaperFinish
        #     data6 = udata.ht
        #     data7 = udata.grinding
        #     data8 = udata.hardChrome
        #     data9 = udata.qualityCheck
        #     data10 = udata.packingDispach
        #     # print(data1)
        #     # print(data2)
        #     # print(data3)
        #     # print(data4)
        #     # print(data5)
        #     # print(data6)
        #     # print(data7)
        #     # print(data8)
        #     # print(data9)
        #     # print(data10)
            
        #     if data1 :
        #         data1 = float(data1)
        #     else:
        #         data1 = 0
        #     if data2 :
        #         data2 = float(data2)
        #     else:
        #         data2 = 0
        #     if data3 :
        #         data3 = float(data3)
        #     else:
        #         data3 = 0
        #     if data4 :
        #         data4 = float(data4)
        #     else:
        #         data4 = 0
        #     if data5 :
        #         data5 = float(data5)
        #     else:
        #         data5 = 0
        #     if data6 :
        #         data6 = float(data6)
        #     else:
        #         data6 = 0
        #     if data7 :
        #         data7 = float(data7)
        #     else:
        #         data7 = 0
        #     if data8 :
        #         data8 = float(data8)
        #     else:
        #         data8 = 0
        #     if data9 :
        #         data9 = float(data9)
        #     else:
        #         data9 = 0
        #     if data10 :
        #         data10 = float(data10)
        #     else:
        #         data10 = 0
            
        #     totaldata = (((data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10)/10) * 100)
        #     print("total is :",totaldata)
        #     data_status = str(totaldata) + str("%")
        #     if data_status:
        #         udata.status = data_status
        #         udata.save()
        #     if udata.u1 and udata.l1:
        #         udata.punchBlankUsed = int(udata.u1) + int(udata.l1)
        #         udata.save()
        #     if udata.d:
        #         udata.dieBlankUsed = udata.d
        #         udata.save()
            
        # # else:
        # #     print("no didnt get")
        # #     update = "no"
        # # if 'updateformid'  in request.session:
        # #     sessdata = request.session['updateformid']
        # # else:
        # #     sessdata = ""
        # if test:
        #     check = ProductionData.objects.get(orderNumber=test)
        #     request.session['id'] = check.id
        #     punchblank = int(check.u1) + int(check.l1)
        #     dieblank = int(check.d)
        #     print("lala",punchblank,dieblank)
        #     print("set",check.sett)
        #     passdata = {
        #         "set" : check.sett,
        #         "rawmaterial" : check.rawMaterial,
        #         "priority" : check.priority,
        #         "dwgnumber" : check.dwgNumber,
        #         "drgdate" : check.drgDate,
        #         "approvaldate" : check.approvalDate,
        #         "master" : check.master,
        #         "masterout" : check.masterOut,
        #         "masterin" : check.masterIn,
        #         "punchblank":punchblank,
        #         "dieblank":dieblank,
        #         "htdate" : check.hitDate,
        #         "estimateddelivery" : check.estimatedDelivery,
        #         "planningout" : check.planningOut,
        #         "planningin" : check.planningIn,
        #         "orderdate" : check.orderDate,
        #         "ordernumber" : check.orderNumber,
        #         "clientname" :check.clientName,
        #         "value" : check.value,
        #         "moc" : check.moc,
        #         "tooltype" : check.toolType,
        #         "shape" : check.shape,
        #         "tabletsize" : check.tabletSize,
        #         "u1" : check.u1,
        #         "u2" : check.u2,
        #         "l1" : check.l1,
        #         "l2" : check.l2,
        #         "d" : check.d,
                
        #         "platingtype" : check.platingType,
        #         "orderremark" : check.order_remarks,
        #         "actualdeliverydate" : check.actualDelivery,
        #         "modeofdispatch" : check.dispachMode,
        #         "couriernumber" : check.couriesNumber,               
        #         "blank" : check.blank,
        #         "process" : check.process,
        #         "bodytipping" : check.bodyTipMachining,
        #         "headmachine" : check.headMachining,
        #         "keyway" : check.keywayTaperFinish,
        #         "ht" : check.ht,
        #         "grinding" : check.grinding,
        #         "hardchrome" : check.hardChrome,
        #         "qualitycheck" : check.qualityCheck,
        #         "packingdispach" : check.packingDispach

        #     }
        #     return JsonResponse({"passdata":passdata})
        # if 'id' in request.session:
        #     sessdata = request.session['id']
        # if rawmaterial or priority or dwgnumber or drgdate or approvaldate or master or masterout or masterin or htdate or estimateddelivery or planningout or planningin or blank or process or bodytipping or headmachine or keyway or ht or grinding or hardchrome or qualitycheck or packingdispach :
        #     print("yes satisfied")
        #     print("logged in user is blah :",user_id,user_name)
        #     form = ProductionData.objects.get(id = sessdata)
        #     type="Updated"
        #     # status=form.status,dwgNumber=form.dwgNumber,drgDate=form.drgDate,approvalDate=form.approvalDate,master=form.master,masterOut=form.masterOut,masterIn=form.masterIn,punchBlankUsed=form.punchBlankUsed,dieBlankUsed=form.dieBlankUsed,hitDate=form.hitDate,estimatedDelivery=form.estimatedDelivery,planningOut=form.planningOut,planningIn=form.planningIn,blank=form.blank,process=form.process,bodyTipMachining=form.bodyTipMachining,headMachining=form.headMachining,keywayTaperFinish=form.keywayTaperFinish,ht=form.ht,grinding=form.grinding,hardChrome=form.hardChrome,qualityCheck=form.qualityCheck,packingDispach=form.packingDispach
        #     log = UserLog(formid=sessdata,user_id=user_id,user_name=user_name,rawMaterial=form.rawMaterial,priority=form.priority,dwgNumber=form.dwgNumber,drgDate=form.drgDate,approvalDate=form.approvalDate,master=form.master,masterOut=form.masterOut,masterIn=form.masterIn,hitDate=form.hitDate,estimatedDelivery=form.estimatedDelivery,planningOut=form.planningOut,planningIn=form.planningIn,blank=form.blank,process=form.process,bodyTipMachining=form.bodyTipMachining,headMachining=form.headMachining,keywayTaperFinish=form.keywayTaperFinish,ht=form.ht,grinding=form.grinding,hardChrome=form.hardChrome,qualityCheck=form.qualityCheck,packingDispach=form.packingDispach,new_rawMaterial=rawmaterial,new_priority=priority,new_dwgNumber=dwgnumber,new_drgDate=drgdate,new_approvalDate=approvaldate,new_master=master,new_masterOut=masterout,new_masterIn=masterin,new_hitDate=htdate,new_estimatedDelivery=estimateddelivery,new_planningOut=planningout,new_planningIn=planningin,new_blank=blank,new_process=process,new_bodyTipMachining=bodytipping,new_headMachining=headmachine,new_keywayTaperFinish=keyway,new_ht=ht,new_grinding=grinding,new_hardChrome=hardchrome,new_qualityCheck=qualitycheck,new_packingDispach=packingdispach,Type=type)
        #     log.save()
        #     if rawmaterial:
        #         form.rawMaterial = rawmaterial
        #         form.save()
        #     if priority:
        #         form.priority = priority
        #         form.save()
        #     if dwgnumber:
        #         print("got dwgnumber")
        #         form.dwgNumber = dwgnumber
        #         form.save()
        #     if drgdate:
        #         form.drgDate = drgdate
        #         form.save()
        #     if approvaldate:
        #         form.approvalDate = approvaldate
        #         form.save()
        #     if master:
        #         form.master = master
        #         form.save()
        #     if masterout:
        #         form.masterOut = masterout
        #         form.save()
        #     if masterin:
        #         form.masterIn = masterin
        #         form.save()
        #     if htdate:
        #         form.hitDate = htdate
        #         form.save()
        #     if estimateddelivery:
        #         form.estimatedDelivery = estimateddelivery
        #         form.save()
        #     if planningout:
        #         form.planningOut = planningout
        #         form.save()
        #     if planningin:
        #         form.planningIn = planningin
        #         form.save()
        #     if blank:
        #         print("yes blank")
        #         form.blank = blank
        #         form.save()
        #     if process:
        #         form.process = process
        #         form.save()
        #     if bodytipping:
        #         form.bodyTipMachining = bodytipping
        #         form.save()
        #     if headmachine:
        #         form.headMachining = headmachine
        #         form.save()
        #     if keyway:
        #         form.keywayTaperFinish = keyway
        #         form.save()
        #     if ht:
        #         form.ht = ht
        #         form.save()
        #     if grinding:
        #         form.grinding = grinding
        #         form.save()
        #     if hardchrome:
        #         form.hardChrome = hardchrome
        #         form.save()
        #     if qualitycheck:
        #         form.qualityCheck = qualitycheck
        #         form.save()
        #     if packingdispach:
        #         form.packingDispach = packingdispach
        #         form.save()
        #     alerta = "yes"
        #     return redirect('index2')
        # else:
        #     print("not satisfied")
    params = {
        "tabledata":ProductionData.objects.all(),
        "RawMaterial":RawMaterial.objects.all(),
        "Blank":Blank.objects.all(),
        "Process":Process.objects.all(),
        "BodyTipMachining":BodyTipMachining.objects.all(),
        "HeadMachining":HeadMachining.objects.all(),
        "KeywayTaperFinish":KeywayTaperFinish.objects.all(),
        "HT":HT.objects.all(),
        "Grinding":Grinding.objects.all(),
        "HardChrome":HardChrome.objects.all(),
        "QualityCheck":QualityCheck.objects.all(),
        "PackingDispach":PackingDispach.objects.all(),
    }
    return render(request,"user2/dashboard_user2.html",params)





@login_required
def admin(request):
    display = ""
    if request.user.is_superuser:
        if request.method == "POST":
            form_order_id = request.POST.get('abc')
            if form_order_id:
                print("Got Form Order Id :",form_order_id)
                data = ProductionData.objects.get(orderNumber=form_order_id)
                punchblank = int(data.u1.name) + int(data.l1.name)
                dieblank = int(data.d.name)
                data_serializer = ProductionDataSerializer(data,many=False)
                return JsonResponse({"passdata":data_serializer.data,"punch_blank":punchblank,'die_blank':dieblank})
            update_orderdate = request.POST.get('update_orderdate')
            update_ordernumber = request.POST.get('update_ordernumber')
            update_clientname = request.POST.get('update_clientname')
            update_value = request.POST.get('update_value')
            # print("value is :",value1)
            update_moc = request.POST.get('update_moc')
            update_tooltype = request.POST.get('update_tooltype')
            update_shape = request.POST.get('update_shape')
            update_tabletsize = request.POST.get('update_tabletsize')
            update_u1 = request.POST.get('update_u1')
            update_u2 = request.POST.get('update_u2')
            update_l1 = request.POST.get('update_l1')
            update_l2 = request.POST.get('update_l2')
            update_d = request.POST.get('update_d')
            update_set = request.POST.get('update_set')
            update_platingtype = request.POST.get('update_platingtype')
            update_orderremark = request.POST.get('update_orderremark')
            update_form_id = request.POST.get('update_form_id')
            update_actualdeliverydate = request.POST.get('update_actualdeliverydate')
            update_modeofdispatch = request.POST.get('update_modeofdispatch')
            update_couriernumber = request.POST.get('update_couriernumber')
            rawmaterial = request.POST.get('update_rawmaterial')
            priority = request.POST.get('update_priority')
            dwgnumber = request.POST.get('update_dwgnumber')
            drgdate = request.POST.get('update_drgdate')
            approvaldate = request.POST.get('update_approvaldate')
            master = request.POST.get('update_master')
            masterout = request.POST.get('update_masterout')
            masterin = request.POST.get('update_masterin')
            htdate = request.POST.get('update_htdate')
            estimateddelivery = request.POST.get('update_estimateddelivery')
            planningout = request.POST.get('update_planningout')
            planningin = request.POST.get('update_planningin')
            blank = request.POST.get('update_blank')
            process = request.POST.get('update_process')
            bodytipping = request.POST.get('update_bodytipping')
            headmachine = request.POST.get('update_headmachine')
            keyway = request.POST.get('update_keyway')
            ht = request.POST.get('update_ht')
            grinding = request.POST.get('update_grinding')
            hardchrome = request.POST.get('update_hardchrome')
            qualitycheck = request.POST.get('update_qualitycheck')
            packingdispach = request.POST.get('update_packingdispach')
            if update_orderdate or update_ordernumber or update_clientname or update_value or update_moc or update_tooltype or update_shape or update_tabletsize or update_u1 or update_u2 or update_u2 or update_l1 or update_l2 or update_d or update_set or update_platingtype or update_orderremark or update_form_id or update_actualdeliverydate or update_modeofdispatch or update_couriernumber or rawmaterial or priority or dwgnumber or drgdate or approvaldate or master or masterout or masterin or htdate or estimateddelivery or planningout or planningin or blank or process or bodytipping or  headmachine or keyway or ht or grinding or hardchrome or qualitycheck or packingdispach:
                print(update_orderdate , update_ordernumber , update_clientname , update_value , update_moc , update_tooltype , update_shape , update_tabletsize , update_u1 , update_u2 , update_l1 , update_l2 , update_d , update_set , update_platingtype , update_orderremark , update_form_id , update_actualdeliverydate , update_modeofdispatch , update_couriernumber)
                update_form = ProductionData.objects.get(id=update_form_id)
                if update_orderdate:
                    update_form.orderDate = update_orderdate
                if update_ordernumber:
                    update_form.orderNumber = update_ordernumber
                if update_clientname:
                    update_form.clientName = CustomerDetail.objects.get(id=update_clientname)
                if update_value:
                    update_form.value = update_value
                if update_moc:
                    update_form.moc = Moc.objects.get(id=update_moc)
                if update_tooltype:
                    update_form.toolType = ToolType.objects.get(id=update_tooltype)
                if update_shape:
                    update_form.shape = Shape.objects.get(id=update_shape)
                if update_tabletsize:
                    update_form.tabletSize = TabletSize.objects.get(id=update_tabletsize)
                if update_u1:
                    update_form.u1 = U1.objects.get(id=update_u1)
                if update_u2:
                    update_form.u2 =U2.objects.get(id=update_u2)
                if update_l1:
                    update_form.l1 = L1.objects.get(id=update_l1)
                if update_l2:
                    update_form.l2= L2.objects.get(id=update_l2)
                if update_d:
                    update_form.d = D.objects.get(id=update_d)
                if update_set:
                    update_form.set = Set.objects.get(id=update_set)
                if update_platingtype:
                    update_form.platingType = PlatingType.objects.get(id=update_platingtype)
                if update_orderremark:
                    update_form.user_1_remarks = update_orderremark
                if update_actualdeliverydate:
                    update_form.actualDelivery = update_actualdeliverydate
                if update_modeofdispatch:
                    update_form.dispachMode = DispachMode.objects.get(id=update_modeofdispatch)
                if update_couriernumber:
                    update_form.couriesNumber = update_couriernumber
                if rawmaterial:
                    update_form.rawMaterial = RawMaterial.objects.get(id=rawmaterial)
                if priority:
                    update_form.priority = priority
                if dwgnumber:
                    update_form.dwgNumber = dwgnumber
                if drgdate:
                    update_form.drgDate = drgdate
                if approvaldate:
                    update_form.approvalDate = approvaldate
                if master:
                    update_form.master = master
                if masterout:
                    update_form.masterOut = masterout
                if masterin:
                    update_form.masterIn = masterin
                if htdate:
                    update_form.hitDate = htdate
                if estimateddelivery:
                    update_form.estimatedDelivery = estimateddelivery
                if planningout:
                    update_form.planningOut = planningout
                if planningin:
                    update_form.planningIn = planningin
                if blank:
                    update_form.blank = Blank.objects.get(id = blank)
                if process:
                    update_form.process = Process.objects.get(id = process)
                if bodytipping:
                    update_form.bodyTipMachining = BodyTipMachining.objects.get(id = bodytipping)
                if headmachine:
                    update_form.headMachining = HeadMachining.objects.get(id = headmachine)
                if keyway:
                    update_form.keywayTaperFinish = KeywayTaperFinish.objects.get(id = keyway)
                if ht:
                    update_form.ht = HT.objects.get(id = ht)
                if grinding:
                    update_form.grinding = Grinding.objects.get(id = grinding)
                if hardchrome:
                    update_form.hardChrome = HardChrome.objects.get(id = hardchrome)
                if qualitycheck:
                    update_form.qualityCheck = QualityCheck.objects.get(id = qualitycheck)
                if packingdispach:
                    update_form.packingDispach = PackingDispach.objects.get(id = packingdispach)
                update_form.save()
                return redirect('admin')
        params = {
            "tabledata":ProductionData.objects.all(),
            "CustomerDetail":CustomerDetail.objects.all(),
            "Moc":Moc.objects.all(),
            "ToolType":ToolType.objects.all(),
            "Shape":Shape.objects.all(),
            "TabletSize":TabletSize.objects.all(),
            "U1":U1.objects.all(),
            "U2":U2.objects.all(),
            "L1":L1.objects.all(),
            "L2":L2.objects.all(),
            "D":D.objects.all(),
            "Set":Set.objects.all(),
            "PlatingType":PlatingType.objects.all(),
            "DispachMode":DispachMode.objects.all(),
            "RawMaterial":RawMaterial.objects.all(),
            "Blank":Blank.objects.all(),
            "Process":Process.objects.all(),
            "BodyTipMachining":BodyTipMachining.objects.all(),
            "HeadMachining":HeadMachining.objects.all(),
            "KeywayTaperFinish":KeywayTaperFinish.objects.all(),
            "HT":HT.objects.all(),
            "Grinding":Grinding.objects.all(),
            "HardChrome":HardChrome.objects.all(),
            "QualityCheck":QualityCheck.objects.all(),
            "PackingDispach":PackingDispach.objects.all(),

        }
        return render(request,"admin/admin.html",params)

@login_required
def add_customer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            customername = request.POST.get('customername')
            customeremail = request.POST.get('customeremail')
            customermobile = request.POST.get('customermobile')
            companyname = request.POST.get('companyname')
            companyaddress = request.POST.get('companyaddress')
            companystate = request.POST.get('state')
            companycity = request.POST.get('companycity')
            companypincode = request.POST.get('companypincode')
            if customeremail and customermobile:
                addcustomer = CustomerDetail(customerName=customername,customerEmail=customeremail,customerMobile=customermobile,customerCompanyName=companyname,customerCompanyAddress=companyaddress,customerCompanyState=companystate,customerCompanyCity=companycity,customerCompanyPincode=companypincode)
                if addcustomer:
                    addcustomer.save()
                    return redirect('add_customer')
            
    return render(request,"admin/admin_addcustomer.html")

@login_required
def customerCheck(request):
    if request.user.is_superuser:
        if request.method == "POST":
            custid=request.POST.get('custid')
            print("custid :",custid)
            if custid:
                custdata = CustomerDetail.objects.get(id=custid)
                customer_detail_serializer = CustomerDetailSerializer(custdata,many=False)
                return JsonResponse({"custdata":customer_detail_serializer.data})
            # print("data is :",request.session['custid'])
            customerID = request.POST.get('customerID')
            customername = request.POST.get('customername')
            customeremail = request.POST.get('customeremail')
            customermobile = request.POST.get('customermobile')
            companyname = request.POST.get('companyname')
            companyaddress = request.POST.get('companyaddress')
            companystate = request.POST.get('state')
            companycity = request.POST.get('companycity')
            companypincode = request.POST.get('companypincode')
            
            if customername or customeremail or customermobile or companyname or companyaddress or companystate or companycity or companypincode:
                custdata = CustomerDetail.objects.get(id=customerID)
                if customername:
                    custdata.customerName=customername                     
                if customeremail:
                    custdata.customerEmail=customeremail                   
                if customermobile:
                    custdata.customerMobile=customermobile                      
                if companyname:
                    custdata.customerCompanyName=companyname
                if companyaddress:
                    custdata.customerCompanyAddress=companyaddress
                if companystate:
                    custdata.customerCompanyState=companystate
                if companycity:
                    custdata.customerCompanyCity=companycity
                if companypincode:
                    custdata.customerCompanyPincode=companypincode
                custdata.save()
                    
                    
                
                  
        params={
            'cust':CustomerDetail.objects.all()
        }
        return render(request,"admin/customerdetails.html",params)

@login_required
def adduser(request):
    if request.user.is_superuser:
        data = "yes"
        created = ""
        user_match = ""
        if request.method == "POST":
            email = request.POST.get('email')
            addpassword = request.POST.get('addpassword')
            user_level = request.POST.get('user_level')
            print(email , addpassword , user_level)
            if email and addpassword and user_level:
                try:
                    user_exist = User.objects.get(email=email)
                    user_match = "yes"
                except User.DoesNotExist:
                    user_match = "no"
                    if user_level == "user_1":
                        usercreation = User.objects.create_user(email=email, password=addpassword,is_user_role_1=True)
                        if usercreation:
                            usercreation.save()
                    if user_level == "user_2":
                        usercreation = User.objects.create_user(email=email, password=addpassword,is_user_role_2=True)
                        if usercreation:
                            usercreation.save()
                    
                    if user_level == "user_3":
                        usercreation = User.objects.create_user(email=email, password=addpassword,is_user_role_3=True)
                        if usercreation:
                            usercreation.save()
                                
                    created = "yes" 
                    
                    
        params = {
            "user_match":user_match,
            "created":created
        }
                
        return render(request,"admin/adduser.html",params)

@login_required
def add_data(request):
    data=""
    if request.user.is_superuser:
        data = "yes"
        if request.method == "POST":
            get_data_of = request.POST.get('get_data_of')
            if get_data_of:
                print("get_data_of :",get_data_of)
                if get_data_of == "clientname":
                    customer_detail = CustomerDetail.objects.all()
                    customer_detail_serializer = CustomerDetailSerializer(customer_detail,many=True)
                    return JsonResponse({'data':customer_detail_serializer.data,'type':"clientname"})
                elif get_data_of == "moc":
                    moc = Moc.objects.all()
                    moc_serializer = MocSerializer(moc,many=True)
                    return JsonResponse({'data':moc_serializer.data,'type':"moc"})
                elif get_data_of == "tooltype":
                    tooltype = ToolType.objects.all()
                    tooltype_serializer = ToolTypeSerializer(tooltype,many=True)
                    return JsonResponse({'data':tooltype_serializer.data,'type':"tooltype"})
                elif get_data_of == "shape":
                    shape = Shape.objects.all()
                    shape_serializer = ShapeSerializer(shape,many=True)
                    return JsonResponse({'data':shape_serializer.data,'type':"shape"})
                elif get_data_of == "tabletsize":
                    tabletsize = TabletSize.objects.all()
                    tabletsize_serializer = TabletSizeSerializer(tabletsize,many=True)
                    return JsonResponse({'data':tabletsize_serializer.data,'type':"tabletsize"})
                elif get_data_of == "u1":
                    u1 = U1.objects.all()
                    u1_serializer = U1Serializer(u1,many=True)
                    return JsonResponse({'data':u1_serializer.data,'type':"u1"})
                elif get_data_of == "u2":
                    u2 = U2.objects.all()
                    u2_serializer = U2Serializer(u2,many=True)
                    return JsonResponse({'data':u2_serializer.data,'type':"u2"})
                elif get_data_of == "l1":
                    l1 = L1.objects.all()
                    l1_serializer = L1Serializer(l1,many=True)
                    return JsonResponse({'data':l1_serializer.data,'type':"l1"})
                elif get_data_of == "l2":
                    l2 = L2.objects.all()
                    l2_serializer = L2Serializer(l2,many=True)
                    return JsonResponse({'data':l2_serializer.data,'type':"l2"})
                elif get_data_of == "d":
                    d = D.objects.all()
                    d_serializer = DSerializer(d,many=True)
                    return JsonResponse({'data':d_serializer.data,'type':"d"})
                elif get_data_of == "set":
                    set = Set.objects.all()
                    set_serializer = SetSerializer(set,many=True)
                    return JsonResponse({'data':set_serializer.data,'type':"set"})
                elif get_data_of == "platingtype":
                    platingtype = PlatingType.objects.all()
                    platingtype_serializer = PlatingTypeSerializer(platingtype,many=True)
                    return JsonResponse({'data':platingtype_serializer.data,'type':"platingtype"})
                elif get_data_of == "rawmaterial":
                    rawmaterial = RawMaterial.objects.all()
                    rawmaterial_serializer = RawMaterialSerializer(rawmaterial,many=True)
                    return JsonResponse({'data':rawmaterial_serializer.data,'type':"rawmaterial"})
                elif get_data_of == "punchblank":
                    punchblank = PunchBlank.objects.all()
                    punchblank_serializer = PunchBlankSerializer(punchblank,many=True)
                    return JsonResponse({'data':punchblank_serializer.data,'type':"punchblank"})
                elif get_data_of == "dieblank":
                    dieblank = DieBlank.objects.all()
                    dieblank_serializer = DieBlankSerializer(dieblank,many=True)
                    return JsonResponse({'data':dieblank_serializer.data,'type':"dieblank"})



                elif get_data_of == "blank":
                    blank = Blank.objects.all()
                    blank_serializer = BlankSerializer(blank,many=True)
                    return JsonResponse({'data':blank_serializer.data,'type':"blank"})
                elif get_data_of == "process":
                    process = Process.objects.all()
                    process_serializer = ProcessSerializer(process,many=True)
                    return JsonResponse({'data':process_serializer.data,'type':"process"})
                elif get_data_of == "bodytipmachining":
                    bodytipmachining = BodyTipMachining.objects.all()
                    bodytipmachining_serializer = BodyTipMachiningSerializer(bodytipmachining,many=True)
                    return JsonResponse({'data':bodytipmachining_serializer.data,'type':"bodytipmachining"})
                elif get_data_of == "headmachining":
                    headmachining = HeadMachining.objects.all()
                    headmachining_serializer = HeadMachiningSerializer(headmachining,many=True)
                    return JsonResponse({'data':headmachining_serializer.data,'type':"headmachining"})
                elif get_data_of == "keywaytaperfinish":
                    keywaytaperfinish = KeywayTaperFinish.objects.all()
                    keywaytaperfinish_serializer = KeywayTaperFinishSerializer(keywaytaperfinish,many=True)
                    return JsonResponse({'data':keywaytaperfinish_serializer.data,'type':"keywaytaperfinish"})
                elif get_data_of == "ht":
                    ht = HT.objects.all()
                    ht_serializer = HTSerializer(ht,many=True)
                    return JsonResponse({'data':ht_serializer.data,'type':"ht"})
                elif get_data_of == "grinding":
                    grinding = Grinding.objects.all()
                    grinding_serializer = GrindingSerializer(grinding,many=True)
                    return JsonResponse({'data':grinding_serializer.data,'type':"grinding"})
                elif get_data_of == "hardchrome":
                    hardchrome = HardChrome.objects.all()
                    hardchrome_serializer = HardChromeSerializer(hardchrome,many=True)
                    return JsonResponse({'data':hardchrome_serializer.data,'type':"hardchrome"})
                elif get_data_of == "qualitycheck":
                    qualitycheck = QualityCheck.objects.all()
                    qualitycheck_serializer = QualityCheckSerializer(qualitycheck,many=True)
                    return JsonResponse({'data':qualitycheck_serializer.data,'type':"qualitycheck"})
                elif get_data_of == "packingdispatch":
                    packingdispatch = PackingDispach.objects.all()
                    packingdispatch_serializer = PackingDispachSerializer(packingdispatch,many=True)
                    return JsonResponse({'data':packingdispatch_serializer.data,'type':"packingdispatch"})
                
                elif get_data_of == "dispatchmode":
                    dispatchmode = DispachMode.objects.all()
                    dispatchmode_serializer = DispachModeSerializer(dispatchmode,many=True)
                    return JsonResponse({'data':dispatchmode_serializer.data,'type':"dispatchmode"})
                
                
            clientname = request.POST.get('clientname')
            if clientname:
                customer_detail = CustomerDetail(customerCompanyName=clientname)
                customer_detail.save()
            moc = request.POST.get('moc')
            if moc:
                add_moc = Moc(name=moc)
                add_moc.save()
            tooltype = request.POST.get('tooltype')
            if tooltype:
                add_tooltype = ToolType(name=tooltype)
                add_tooltype.save()
            shape = request.POST.get('shape')
            if shape:
                add_shape = Shape(name=shape)
                add_shape.save()
            tabletsize = request.POST.get('tabletsize')
            if tabletsize:
                add_tabletsize = TabletSize(name=tabletsize)
                add_tabletsize.save()
            u1 = request.POST.get('u1')
            if u1:
                add_u1 = U1(name=u1)
                add_u1.save()
            u2 = request.POST.get('u2')
            if u2:
                add_u2 = U2(name=u2)
                add_u2.save()
            l1 = request.POST.get('l1')
            if l1:
                add_l1 = L1(name=l1)
                add_l1.save()
            l2 = request.POST.get('l2')
            if l2:
                add_l2 = L2(name=l2)
                add_l2.save()
            d = request.POST.get('d')
            if d:
                add_d = D(name=d)
                add_d.save()
            set = request.POST.get('set')
            if set:
                add_set = Set(name=set)
                add_set.save()
            platingtype = request.POST.get('platingtype')
            if platingtype:
                add_platingtype = PlatingType(name=platingtype)
                add_platingtype.save()
            rawmaterial = request.POST.get('rawmaterial')
            if rawmaterial:
                add_rawmaterial = RawMaterial(name=rawmaterial)
                add_rawmaterial.save()
            punchblank = request.POST.get('punchblank')
            if punchblank:
                add_punchblank = PunchBlank(name=punchblank)
                add_punchblank.save()
            dieblank = request.POST.get('dieblank')
            if dieblank:
                add_dieblank = DieBlank(name=dieblank)
                add_dieblank.save()

            blank = request.POST.get('blank')   
            if blank:
                add_blank = Blank(name=blank)
                add_blank.save()
            process = request.POST.get('process')
            if process:
                add_process = Process(name=process)
                add_process.save()
            bodytipmachining = request.POST.get('bodytipmachining')
            if bodytipmachining:
                add_bodytipmachining = BodyTipMachining(name=bodytipmachining)
                add_bodytipmachining.save()
            headmachining = request.POST.get('headmachining')
            if headmachining:
                add_headmachining = HeadMachining(name=headmachining)
                add_headmachining.save()
            keywaytaperfinish = request.POST.get('keywaytaperfinish')
            if keywaytaperfinish:
                add_keywaytaperfinish = KeywayTaperFinish(name=keywaytaperfinish)
                add_keywaytaperfinish.save()
            ht = request.POST.get('ht')
            if ht:
                add_ht = HT(name=ht)
                add_ht.save()
            grinding = request.POST.get('grinding')
            if grinding:
                add_grinding = Grinding(name=grinding)
                add_grinding.save()
            hardchrome = request.POST.get('hardchrome')
            if hardchrome:
                add_hardchrome = HardChrome(name=hardchrome)
                add_hardchrome.save()
            qualitycheck = request.POST.get('qualitycheck')
            if qualitycheck:
                add_qualitycheck = QualityCheck(name=qualitycheck)
                add_qualitycheck.save()
            packingdispatch = request.POST.get('packingdispatch')
            if packingdispatch:
                add_packingdispatch = PackingDispach(name=packingdispatch)
                add_packingdispatch.save()
            # 
            dispatchmode = request.POST.get('dispatchmode')
            if dispatchmode:
                add_dispatchmode = DispachMode(name=dispatchmode)
                add_dispatchmode.save()

        
        params = {
            "data":data
        }
                
        return render(request,"admin/admin_adddata.html",params)

@login_required
def delete_data(request):
    data=""
    tabledata = []
    if request.user.is_superuser:
        if request.method == "POST":
            deleteform = request.POST.get('deleteform')
            if deleteform:
                deletedata = ProductionData.objects.get(id = deleteform)
                if deletedata:
                    deletedata.delete()
                    type="Deleted"
                    log = UserLog(formid=deleteform,user_id=request.user.id,user_name=request.user.username,Type=type)
                    log.save()
                    return redirect('admindelete')
        
            # form = ProductionData.objects.all()
            # for x in form:
            #     data_id= x.id
            #     data_orderdate1  = x.orderDate
            #     data_orderdate = datetime.datetime.strptime(data_orderdate1, "%Y-%m-%d").strftime("%d-%m-%Y")
            #     data_ordernumber    = x.orderNumber
            #     data_clientname =x.clientName
            #     data_value =x.value
            #     data_moc = x.moc
            #     data_tooltype =x.toolType
            #     data_shape =x.shape
            #     data_tabletsize =x.tabletSize
            #     data_u1 =x.u1
            #     data_u2 =x.u2
            #     data_l1 =x.l1
            #     data_l2 =x.l2
            #     data_d =x.d
            #     data_set =x.set
            #     data_platingtype =x.platingType
            #     data_rawmaterial =x.rawMaterial
            #     data_priority =x.priority
            #     data_dwgNumber = x.dwgNumber
            #     data_drgDate = x.drgDate
            #     data_approvalDate = x.approvalDate
            #     data_master = x.master
            #     data_masterOut = x.masterOut
            #     data_masterIn = x.masterIn
            #     if data_u1 and data_u2:
            #         data_punchBlankUsed = int(data_u1.name)+ int(data_l1.name)
            #     else:
            #         data_punchBlankUsed =0
            #     # print(data_punchBlankUsed)
            #     data_dieBlankUsed = data_d
            #     data_hitDate = x.hitDate
            #     data_estimatedDelivery = x.estimatedDelivery
            #     data_planningOut=x.planningOut
            #     data_planningIn=x.planningIn
            #     data_blank=x.blank
            #     data_process=x.process
            #     data_bodyTipMachining=x.bodyTipMachining
            #     data_headMachining=x.headMachining
            #     data_keywayTaperFinish=x.keywayTaperFinish
            #     data_ht=x.ht
            #     data_grinding=x.grinding
            #     data_hardChrome=x.hardChrome
            #     data_qualityCheck=x.qualityCheck
            #     data_packingDispach=x.packingDispach
            #     data_estimatedDelivery=x.estimatedDelivery
            #     data_actualDelivery=x.actualDelivery
            #     data_dispachMode=x.dispachMode
            #     data_couriesNumber=x.couriesNumber
            #     data_remark=x.remark
            #     data1 = x.blank
            #     data2 = x.process
            #     data3 = x.bodyTipMachining
            #     data4 = x.headMachining
            #     data5 = x.keywayTaperFinish
            #     data6 = x.ht
            #     data7 = x.grinding
            #     data8 = x.hardChrome
            #     data9 = x.qualityCheck
            #     data10 = x.packingDispach
            #     if data1 :
            #         data1 = float(data1)
            #     else:
            #         data1 = 0
            #     if data2 :
            #         data2 = float(data2)
            #     else:
            #         data2 = 0
            #     if data3 :
            #         data3 = float(data3)
            #     else:
            #         data3 = 0
            #     if data4 :
            #         data4 = float(data4)
            #     else:
            #         data4 = 0
            #     if data5 :
            #         data5 = float(data5)
            #     else:
            #         data5 = 0
            #     if data6 :
            #         data6 = float(data6)
            #     else:
            #         data6 = 0
            #     if data7 :
            #         data7 = float(data7)
            #     else:
            #         data7 = 0
            #     if data8 :
            #         data8 = float(data8)
            #     else:
            #         data8 = 0
            #     if data9 :
            #         data9 = float(data9)
            #     else:
            #         data9 = 0
            #     if data10 :
            #         data10 = float(data10)
            #     else:
            #         data10 = 0
                
            #     totaldata = (((data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10)/10) * 100)
            #     # print(totaldata%2)
            #     data_status = str(totaldata) + str("%")

            #     # print("status is :",data_id,data_status)
            #     if data_orderdate or data_ordernumber or data_clientname or data_value or data_moc or data_tooltype or data_shape or data_tabletsize or data_u1 or data_u2 or data_l1 or data_l2 or data_d or data_set or data_platingtype or data_rawmaterial or data_priority or data_status:
            #         obj = {
            #             "id":data_id,
            #             "orderdate" : data_orderdate,
            #             "ordernumber" :data_ordernumber,
            #             "clientname" :data_clientname,
            #             "value" :data_value,
            #             "moc" :data_moc,
            #             "tooltype" :data_tooltype,
            #             "shape" :data_shape,
            #             "tabletsize" :data_tabletsize,
            #             "u1" :data_u1,
            #             "u2" :data_u2,
            #             "l1" :data_l1,
            #             "l2" :data_l2,
            #             "d" :data_d,
            #             "set" :data_set,
            #             "platingtype" :data_platingtype,
            #             "rawmaterial" :data_rawmaterial,
            #             "priority" :data_priority,
            #             "status" :data_status,
            #             "dwgNumber" :  data_dwgNumber,
            #             "drgDate" :  data_drgDate,
            #             "approvalDate" :  data_approvalDate,
            #             "master" :  data_master,
            #             "masterOut" :  data_masterOut,
            #             "masterIn" :  data_masterIn,
            #             "punchBlankUsed" :  data_punchBlankUsed,
            #             "dieBlankUsed" :  data_dieBlankUsed,
            #             "hitDate" :  data_hitDate,
            #             "estimatedDelivery" :  data_estimatedDelivery,
            #             "planningOut": data_planningOut,
            #             "planningIn": data_planningIn,
            #             "blank": data_blank,
            #             "process": data_process,
            #             "bodyTipMachining": data_bodyTipMachining,
            #             "headMachining": data_headMachining,
            #             "keywayTaperFinish": data_keywayTaperFinish,
            #             "ht": data_ht,
            #             "grinding": data_grinding,
            #             "hardChrome": data_hardChrome,
            #             "qualityCheck": data_qualityCheck,
            #             "packingDispach": data_packingDispach,
            #             "estimatedDelivery": data_estimatedDelivery,
            #             "actualDelivery": data_actualDelivery,
            #             "dispachMode": data_dispachMode,
            #             "couriesNumber": data_couriesNumber,
            #             "remark": data_remark

            #         }
            #         tabledata.append(obj)
        
    params = {
        "tabledata":ProductionData.objects.all()
    }
    return render(request,"admin/admindeleteform.html",params)



def logout_page(request):
    logout(request)
    # return HttpResponseRedirect('login') 
    return redirect('login')




def user_log(request):
    data=""
    form=""
    level=""
    tabledata = []
    storeid = []
    if request.user.is_superuser:
        if request.method == "POST":
            formid = request.POST.get('abc')
            
        else:
            formid = ""   
        user_id = request.user.id
        
        lvl = 5
        if lvl == 5:
            data = "yes"
            frm = UserLog.objects.all()
            
            table = UserLog.objects.all()
            for i in table:
                
                obj = {
                    "id":i.id,
                    "formid":i.formid,
                    "user_id":i.id,
                    "user_name":i.user_name,
                    "modified_date":i.modified_date,
                    "Type":i.Type,
                    "level":"Admin"
                }
                tabledata.append(obj)
            
            if formid:
                form = UserLog.objects.get(id=formid)
                
                obj1={
                    "user_id":form.user_id,
                    "user_name":form.user_name,
                    "modified_date":form.modified_date,
                    "oldorderDate":form.orderDate,
                    "neworderDate":form.new_orderDate,
                    "oldorderNumber":form.orderNumber,
                    "neworderNumber":form.new_orderNumber,
                    "oldclientName":form.clientName,
                    "newclientName":form.new_clientName,
                    "oldvalue":form.value,
                    "newvalue":form.new_value,
                    "oldmoc":form.moc,
                    "newmoc":form.new_moc,
                    "oldtoolType":form.toolType,
                    "newtoolType":form.new_toolType,
                    "oldshape":form.shape,
                    "newshape":form.new_shape,
                    "oldtabletSize":form.tabletSize,
                    "newtabletSize":form.new_tabletSize,
                    "oldu1":form.u1,
                    "newu1":form.new_u1,
                    "oldu2":form.u2,
                    "newu2":form.new_u2,
                    "oldl1":form.l1,
                    "newl1":form.new_l1,
                    "oldl2":form.l2,
                    "newl2":form.new_l2,
                    "oldd":form.d,
                    "newd":form.new_d,
                    "oldsett":form.sett,
                    "newsett":form.new_sett,
                    "oldplatingType":form.platingType,
                    "newplatingType":form.new_platingType,
                    "oldorder_remarks":form.order_remarks,
                    "neworder_remarks":form.new_order_remarks,
                    "oldactualDelivery":form.actualDelivery,
                    "newactualDelivery":form.new_actualDelivery,
                    "olddispachMode":form.dispachMode,
                    "newdispachMode":form.new_dispachMode,
                    "oldcouriesNumber":form.couriesNumber,
                    "newcouriesNumber":form.new_couriesNumber,


                    "oldrawMaterial":form.rawMaterial,
                    "newrawMaterial":form.new_rawMaterial,
                    "oldpriority":form.priority,
                    "newpriority":form.new_priority,
                    "oldstatus":form.status,
                    "newstatus":form.new_status,
                    "olddwgNumber":form.dwgNumber,
                    "newdwgNumber":form.new_dwgNumber,
                    "olddrgDate":form.drgDate,
                    "newdrgDate":form.new_drgDate,
                    "oldapprovalDate":form.approvalDate,
                    "newapprovalDate":form.new_approvalDate,
                    "oldmaster":form.master,
                    "newmaster":form.new_master,
                    "oldmasterOut":form.masterOut,
                    "newmasterOut":form.new_masterOut,
                    "oldmasterIn":form.masterIn,
                    "newmasterIn":form.new_masterIn,
                    "oldpunchBlankUsed":form.punchBlankUsed,
                    "newpunchBlankUsed":form.new_punchBlankUsed,
                    "olddieBlankUsed":form.dieBlankUsed,
                    "newdieBlankUsed":form.new_dieBlankUsed,
                    "oldhitDate":form.hitDate,
                    "newhitDate":form.new_hitDate,
                    "oldestimatedDelivery":form.estimatedDelivery,
                    "newestimatedDelivery":form.new_estimatedDelivery,
                    "oldplanningOut":form.planningOut,
                    "newplanningOut":form.new_planningOut,
                    "oldplanningIn":form.planningIn,
                    "newplanningIn":form.new_planningIn,
                    "oldblank":form.blank,
                    "newblank":form.new_blank,
                    "oldprocess":form.process,
                    "newprocess":form.new_process,
                    "oldbodyTipMachining":form.bodyTipMachining,
                    "newbodyTipMachining":form.new_bodyTipMachining,
                    "oldheadMachining":form.headMachining,
                    "newheadMachining":form.new_headMachining,
                    "oldkeywayTaperFinish":form.keywayTaperFinish,
                    "newkeywayTaperFinish":form.new_keywayTaperFinish,
                    "oldht":form.ht,
                    "newht":form.new_ht,
                    "oldgrinding":form.grinding,
                    "newgrinding":form.new_grinding,
                    "oldhardChrome":form.hardChrome,
                    "newhardChrome":form.new_hardChrome,
                    "oldqualityCheck":form.qualityCheck,
                    "newqualityCheck":form.new_qualityCheck,
                    "oldpackingDispach":form.packingDispach,
                    "newpackingDispach":form.new_packingDispach,
                    "oldremark":form.remark,
                    "newremark":form.new_remark,

                    "Type":form.Type
                }
                return JsonResponse({"passdata":obj1})


        else:
            data="no"
    params={
        "isloggedin":data,
        "data":tabledata,

    }
    return render(request,"userlog.html",params)

    # return render(request,"test.html")


