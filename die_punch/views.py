from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect , HttpResponseRedirect
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.decorators import user_passes_test
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
    clientnamelist = []
    moclist = []
    tooltypelist = []
    shapelist = []
    tabletSizelist = []
    u1list = []
    u2list = []
    l1list = []
    l2list = []
    dlist = []
    setlist = []
    platingtypelist = []
    updateplaceholder = []
    dispatchlist = []
    dispatchdata = AutoAddDispatch.objects.filter(dispachMode__isnull = False).order_by('dispachMode')
    for i in dispatchdata:
        dispatchlist.append(i.dispachMode)
    clientnamedata = CustomerDetail.objects.filter(customerCompanyName__isnull = False).order_by('customerCompanyName')
    for i in clientnamedata:
        clientnamelist.append(i.customerCompanyName)
    mocdata = AutoAddMain.objects.filter(moc__isnull = False).order_by('moc')
    for i in mocdata:
        moclist.append(i.moc)
    tooltypedata = AutoAddMain.objects.filter(toolType__isnull = False).order_by('toolType')
    for i in tooltypedata:
        tooltypelist.append(i.toolType)
    shapedata = AutoAddMain.objects.filter(shape__isnull = False).order_by('shape')
    for i in shapedata: 
        shapelist.append(i.shape)
    tabletdata = AutoAddMain.objects.filter(tabletSize__isnull = False).order_by('tabletSize')
    for i in tabletdata:
        tabletSizelist.append(i.tabletSize)
    u1data = AutoAddMain.objects.filter(u1__isnull = False).order_by('u1')
    for i in u1data:
        u1list.append(i.u1)
    u2data = AutoAddMain.objects.filter(u2__isnull = False).order_by('u2')
    for i in u2data:
        u2list.append(i.u2)
    l1data = AutoAddMain.objects.filter(l1__isnull = False).order_by('l1')
    for i in l1data:
        l1list.append(i.l1)
    l2data = AutoAddMain.objects.filter(l2__isnull = False).order_by('l2')
    for i in l2data:
        l2list.append(i.l2)
    ddata = AutoAddMain.objects.filter(d__isnull = False).order_by('d')
    for i in ddata:
        dlist.append(i.d)
    setdata = AutoAddMain.objects.filter(sett__isnull = False).order_by('sett')
    for i in setdata:
        setlist.append(i.sett)
    platingtypedata = AutoAddMain.objects.filter(platingType__isnull = False).order_by('platingType')
    for i in platingtypedata:
        platingtypelist.append(i.platingType)
    
    placeholder = {
        "clientname":clientnamelist,
        "moc":moclist,
        "tooltype":tooltypelist,
        "shape":shapelist,
        "tabletsize":tabletSizelist,
        "u1":u1list,
        "u2":u2list,
        "l1":l1list,
        "l2":l2list,
        "d":dlist,
        "set":setlist,
        "platingtype":platingtypelist,
        "dispachMode" : dispatchlist
    }
    
    a=""
    user_name=""
    showformdata=""
    updateform = ""
    tabledata = []
    getid = ""
    update = ""
    isloggedin = ""
    first = ""
    last = ""
    add = ""
    ag = ""
    orderdate1=""
    ordernumber1=""
    clientname1=""
    value1=""
    moc1=""
    tooltype1=""
    shape1=""
    tabletsize1=""
    u11=""
    u21=""
    l11=""
    l21=""
    d1=""
    set1=""
    platingtype1=""
    rawmaterial1=""
    priority1=""
    status1=""
    alerta=""
    errlogin= ""
    test = ""
    passdata = ""
    updateform = ""
    check=""
    orderremark=""
    if request.method == 'POST':
        test = request.POST.get('abc')
        # print("test data is :",test)
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
        rawmaterial = request.POST.get('rawmaterial')
        priority = request.POST.get('priority')

        edd = request.POST.get('edd')
        actualdeliverydate = request.POST.get('actualdeliverydate')
        modeofdispatch = request.POST.get('modeofdispatch')
        couriernumber = request.POST.get('couriernumber')
        dwgnumber = request.POST.get('dwgnumber')
        drgdate = request.POST.get('drgdate')
        approvaldate = request.POST.get('approvaldate')
        master = request.POST.get('master')
        masterout = request.POST.get('masterout')
        masterin = request.POST.get('masterin')
        # punchblank = request.POST.get('punchblank')
        # dieblank = request.POST.get('dieblank')
        htdate = request.POST.get('htdate')
        estimateddelivery = request.POST.get('estimateddelivery')
        planningout = request.POST.get('planningout')
        planningin = request.POST.get('planningin')

        status = request.POST.get('status')        
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            query = User.objects.filter(Q(username=username))
            if query:
                for i in query:
                    userid=i.id
                    userlvl = UserLevel.objects.get(user_id=userid)
                    level = userlvl.level
                    # print("logged in userlevel is :",level)
                    superuser = i.is_superuser
                    if superuser == False and level == 1:
                        authen = authenticate(username=username, password=password)
                        if authen:
                            login(request, authen)
                        else:
                            errlogin = "invalid"
                    else:
                        errlogin = "invalid"
            else:
                errlogin = "invalid"
    else:
        first = ""
        last = ""
        add = ""
        ag = ""
        dwgnumber = ""
        drgdate = ""
        approvaldate = ""
        master = ""
        masterout = ""
        masterin = ""
        punchblank = ""
        dieblank = ""
        htdate = ""
        estimateddelivery = ""
        planningout = ""
        planningin = ""

        edd = ""
        actualdeliverydate = ""
        modeofdispatch = ""
        couriernumber = ""
    if request.user.is_user_role_1:
        user_id = request.user.id

        # print("logged in user id is :",user_id)
        user_name = request.user.first_name
        a = "addyes"
        if a == "addyes":
            if request.method == "POST":
                orderdate1 = request.POST.get('orderdate1')
                ordernumber1 = request.POST.get('ordernumber1')
                clientname1 = request.POST.get('clientname1')
                value1 = request.POST.get('value1')
                # print("value is :",value1)
                moc1 = request.POST.get('moc1')
                tooltype1 = request.POST.get('tooltype1')
                shape1 = request.POST.get('shape1')
                tabletsize1 = request.POST.get('tabletsize1')
                u11 = request.POST.get('u11')
                u21 = request.POST.get('u21')
                l11 = request.POST.get('l11')
                l21 = request.POST.get('l21')
                d1 = request.POST.get('d1')
                set1 = request.POST.get('set1')
                platingtype1 = request.POST.get('platingtype1')
                rawmaterial1 = request.POST.get('rawmaterial1')
                priority1 = request.POST.get('priority1')
                status1 = request.POST.get('status1')
                orderremark = request.POST.get('orderremark')
                updateform = request.POST.get('updateform')

            else:
                orderdate1=""
                ordernumber1=""
                clientname1=""
                value1=""
                moc1=""
                tooltype1=""
                shape1=""
                tabletsize1=""
                u11=""
                u21=""
                l11=""
                l21=""
                d1=""
                set1=""
                platingtype1=""
                rawmaterial1=""
                priority1=""
                status1=""
            # print("yes showdata")
            # print(lvlid)
            frm = ProductionData.objects.all().order_by('id')
            for j in frm:
                data_id= j.id
                data_orderdate1  = j.orderDate
                data_orderdate = datetime.datetime.strptime(data_orderdate1, "%Y-%m-%d").strftime("%d-%m-%Y")
                data_ordernumber    = j.orderNumber
                data_clientname =j.clientName
                data_value =j.value
                data_moc = j.moc
                data_tooltype =j.toolType
                data_shape =j.shape
                data_tabletsize =j.tabletSize
                data_u1 =j.u1
                data_u2 =j.u2
                data_l1 =j.l1
                data_l2 =j.l2
                data_d =j.d
                data_set =j.sett
                data_platingtype =j.platingType
                data_rawmaterial =j.rawMaterial
                data_priority =j.priority
                data_orderremark = j.order_remarks
                data_edd = j.estimatedDelivery
                data_actualdd=j.actualDelivery
                
                # print("edd :",data_edd)
                # print("actual edd :",data_actualdd)
                data1 = j.blank
                data2 = j.process
                data3 = j.bodyTipMachining
                data4 = j.headMachining
                data5 = j.keywayTaperFinish
                data6 = j.ht
                data7 = j.grinding
                data8 = j.hardChrome
                data9 = j.qualityCheck
                data10 = j.packingDispach
                
                
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
                obj = {
                    "id":data_id,
                    "orderdate" : data_orderdate,
                    "ordernumber" :data_ordernumber,
                    "clientname" :data_clientname,
                    "value" :data_value,
                    "moc" :data_moc,
                    "tooltype" :data_tooltype,
                    "shape" :data_shape,
                    "tabletsize" :data_tabletsize,
                    "u1" :data_u1,
                    "u2" :data_u2,
                    "l1" :data_l1,
                    "l2" :data_l2,
                    "d" :data_d,
                    "set" :data_set,
                    "platingtype" :data_platingtype,
                    "rawmaterial" :data_rawmaterial,
                    "priority" :data_priority,
                    "orderremarks":data_orderremark,
                    "status" :data_status,
                    'edd':data_edd,
                    'actualdeliverydate':data_actualdd

                }
                tabledata.append(obj)
        
        else:
            a="no"
        if a == "addyes":
            isloggedin = "yes"
        else:
            isloggedin = "no"
        
        if test:
            check = ProductionData.objects.get(orderNumber=test)
            request.session['id'] = check.id
            passdata = {
                "orderdate" : check.orderDate,
                "ordernumber" : check.orderNumber,
                "clientname" :check.clientName,
                "value" : check.value,
                "moc" : check.moc,
                "tooltype" : check.toolType,
                "shape" : check.shape,
                "tabletsize" : check.tabletSize,
                "u1" : check.u1,
                "u2" : check.u2,
                "l1" : check.l1,
                "l2" : check.l2,
                "d" : check.d,
                "set" : check.sett,
                "platingtype" : check.platingType,
                "orderremark" : check.order_remarks,
                "actualdeliverydate" : check.actualDelivery,
                "modeofdispatch" : check.dispachMode,
                "couriernumber" : check.couriesNumber

            }
            return JsonResponse({"passdata":passdata})
        if updateform:
            # print("yes i got to update",updateform)
            update = "yes"
            request.session['updateformid'] = updateform
            udata = ProductionData.objects.filter(id = updateform)
            for i in udata:
                update_orderdate = str(i.orderDate)
                u_u1 = i.u1
                u_l1 = i.l1
                if u_u1 and u_l1:
                    updatepunchblank = int(u_u1) +int(u_l1)
                else :
                    updatepunchblank = ""
                
                # print("date is :",parsed_date)
                # dt_stamp = datetime.datetime(update_orderdate)
                # print(dt_stamp)
                # dateorder = dt_stamp.strftime("%Y-%m-%d")
                # print(dateorder)
                obj = {
                    "update_id":i.id,
                    "update_orderdate" : update_orderdate,
                    "update_ordernumber" :i.orderNumber,
                    "update_clientname" :i.clientName,
                    "update_value" :i.value,
                    "update_moc" :i.moc,
                    "update_tooltype" :i.toolType,
                    "update_shape" :i.shape,
                    "update_tabletsize" :i.tabletSize,
                    "update_u1" :i.u1,
                    "update_u2" :i.u2,
                    "update_l1" :i.l1,
                    "update_l2" :i.l2,
                    "update_d" :i.d,
                    "update_set" :i.sett,
                    "update_platingtype" :i.platingType,
                    "update_rawmaterial" :i.rawMaterial,
                    "update_priority" :i.priority,
                    "update_orderremarks":i.order_remarks,
                    "update_status" :i.status,

                    "update_dwgnumber":i.dwgNumber,
                    "update_drgdate":i.drgDate,
                    "update_approvalDate":i.approvalDate,
                    "update_master":i.master,
                    "update_masterOut":i.masterOut,
                    "update_masterIn":i.masterIn,
                    "update_punchBlankUsed":updatepunchblank,
                    "update_dieBlankUsed":i.d,
                    "update_hitDate":str(i.hitDate),
                    "update_estimatedDelivery":str(i.estimatedDelivery),
                    "update_planningOut":str(i.planningOut),
                    "update_planningIn":str(i.planningIn),

                    "update_eed":str(i.estimatedDelivery),
                    "update_actual":str(i.actualDelivery),
                    "update_dispatchmode":i.dispachMode,
                    "update_courierno":i.couriesNumber
                }
                updateplaceholder.append(obj)
            
        
        else:
            # print("no didnt get")
            update = "no"
        
        if 'updateformid'  in request.session:
            sessdata = request.session['updateformid']
        else:
            sessdata = ""
        if 'id' in request.session:
            sessdata = request.session['id']
        if orderdate1 or ordernumber1 or clientname1 or value1 or moc1 or tooltype1  or shape1  or tabletsize1  or u11  or u21  or l11  or l21  or d1  or set1  or platingtype1 or orderremark or rawmaterial1  or priority1  or status1 or dwgnumber or drgdate or approvaldate or master or masterout or masterin  or htdate or estimateddelivery or planningout or planningin or edd or actualdeliverydate or modeofdispatch or couriernumber:
            form = ProductionData.objects.get(id = sessdata)
            print("logged in user is blah :",user_id,user_name)
            type="Updated"
            # status=form.status,dwgNumber=form.dwgNumber,drgDate=form.drgDate,approvalDate=form.approvalDate,master=form.master,masterOut=form.masterOut,masterIn=form.masterIn,punchBlankUsed=form.punchBlankUsed,dieBlankUsed=form.dieBlankUsed,hitDate=form.hitDate,estimatedDelivery=form.estimatedDelivery,planningOut=form.planningOut,planningIn=form.planningIn,blank=form.blank,process=form.process,bodyTipMachining=form.bodyTipMachining,headMachining=form.headMachining,keywayTaperFinish=form.keywayTaperFinish,ht=form.ht,grinding=form.grinding,hardChrome=form.hardChrome,qualityCheck=form.qualityCheck,packingDispach=form.packingDispach
            log = UserLog(formid=sessdata,user_id=user_id,user_name=user_name,orderDate=form.orderDate,orderNumber=form.orderNumber,clientName=form.clientName,value=form.value,moc=form.moc,toolType=form.toolType,shape=form.shape,tabletSize=form.tabletSize,u1=form.u1,u2=form.u2,l1=form.l1,l2=form.l2,d=form.d,sett=form.sett,platingType=form.platingType,rawMaterial=form.rawMaterial,priority=form.priority,order_remarks=form.order_remarks,actualDelivery=form.actualDelivery,dispachMode=form.dispachMode,couriesNumber=form.couriesNumber,new_orderDate=orderdate1,new_orderNumber=ordernumber1 ,new_clientName=clientname1 ,new_value=value1 ,new_moc=moc1 ,new_toolType=tooltype1  ,new_shape=shape1  ,new_tabletSize=tabletsize1  ,new_u1=u11  ,new_u2=u21  ,new_l1=l11  ,new_l2=l21  ,new_d=d1  ,new_sett=set1  ,new_platingType=platingtype1,new_order_remarks=orderremark,new_actualDelivery=actualdeliverydate ,new_dispachMode=modeofdispatch ,new_couriesNumber=couriernumber,Type=type)
            log.save()
            if orderdate1:
                form.orderDate = orderdate1
                form.save()
            if ordernumber1:
                form.orderNumber = ordernumber1
                form.save()
            if clientname1:
                form.clientName = clientname1
                form.save()
            if value1:
                form.value = value1
                form.save()
            if moc1:
                form.moc = moc1
                form.save()
            if tooltype1:
                form.toolType = tooltype1
                form.save()
            if shape1:
                form.shape = shape1
                form.save()
            if tabletsize1:
                form.tabletSize = tabletsize1
                form.save()
            if u11:
                form.u1 = u11
                form.save()
            if u21:
                form.u2 = u21
                form.save()
            if l11:
                form.l1 = l11
                form.save()
            if l21:
                form.l2 = l21
                form.save()
            if d1:
                form.d = d1
                form.save()
            if set1:
                form.sett = set1
                form.save()
            if platingtype1:
                form.platingType = platingtype1
                form.save()
            if rawmaterial1:
                form.rawMaterial = rawmaterial1
                form.save()
            if priority1:
                form.priority = priority1
                form.save()
            if orderremark:
                form.order_remarks = orderremark
                form.save()
            if status1:
                form.status = status1
                form.save()
            if dwgnumber:
                form.dwgNumber = dwgnumber
                form.save()
            if drgdate:
                form.drgDate = drgdate
                form.save()
            if approvaldate:
                form.approvalDate = approvaldate
                form.save()
            if master:
                form.master = master
                form.save()
            if masterout:
                form.masterOut = masterout
                form.save()
            if masterin:
                form.masterIn = masterin
                form.save()
            if htdate:
                form.hitDate = htdate
                form.save()
            if estimateddelivery:
                form.estimatedDelivery = estimateddelivery
                form.save()
            if planningout:
                form.planningOut = planningout
                form.save()
            if planningin:
                form.planningIn = planningin
                form.save()
            if edd:
                form.estimatedDelivery = edd
                form.save()
            if actualdeliverydate:
                form.actualDelivery = actualdeliverydate
                form.save()
            if modeofdispatch:
                form.dispachMode = modeofdispatch
                form.save()
            if couriernumber:
                form.couriesNumber = couriernumber
                form.save()
            
            return redirect('index1')
            
        else:
            print("form is not there")
    # print("table data :",tabledata)
    # print(updateplaceholder)
    return render(request,"dashboard_user1.html",{"errlogin":errlogin,"alerta":alerta,"isloggedin":isloggedin,"data":a,"name":user_name,"tabledata":tabledata,"update":update,"placeholder":placeholder,"updateplaceholder":updateplaceholder})

def index1Add(request):
    clientnamelist = []
    moclist = []
    tooltypelist = []
    shapelist = []
    tabletSizelist = []
    u1list = []
    u2list = []
    l1list = []
    l2list = []
    dlist = []
    setlist = []
    platingtypelist = []
    rawmateriallist = []
    updateplaceholder = []
    dispatchlist = []
    dispatchdata = AutoAddDispatch.objects.filter(dispachMode__isnull = False).order_by('dispachMode')
    for i in dispatchdata:
        dispatchlist.append(i.dispachMode)
    clientnamedata = CustomerDetail.objects.filter(customerCompanyName__isnull = False).order_by('customerCompanyName')
    for i in clientnamedata:
        clientnamelist.append(i.customerCompanyName)
    mocdata = AutoAddMain.objects.filter(moc__isnull = False).order_by('moc')
    for i in mocdata:
        moclist.append(i.moc)
    tooltypedata = AutoAddMain.objects.filter(toolType__isnull = False).order_by('toolType')
    for i in tooltypedata:
        tooltypelist.append(i.toolType)
    shapedata = AutoAddMain.objects.filter(shape__isnull = False).order_by('shape')
    for i in shapedata: 
        shapelist.append(i.shape)
    tabletdata = AutoAddMain.objects.filter(tabletSize__isnull = False).order_by('tabletSize')
    for i in tabletdata:
        tabletSizelist.append(i.tabletSize)
    u1data = AutoAddMain.objects.filter(u1__isnull = False).order_by('u1')
    for i in u1data:
        u1list.append(i.u1)
    u2data = AutoAddMain.objects.filter(u2__isnull = False).order_by('u2')
    for i in u2data:
        u2list.append(i.u2)
    l1data = AutoAddMain.objects.filter(l1__isnull = False).order_by('l1')
    for i in l1data:
        l1list.append(i.l1)
    l2data = AutoAddMain.objects.filter(l2__isnull = False).order_by('l2')
    for i in l2data:
        l2list.append(i.l2)
    ddata = AutoAddMain.objects.filter(d__isnull = False).order_by('d')
    for i in ddata:
        dlist.append(i.d)
    setdata = AutoAddMain.objects.filter(sett__isnull = False).order_by('sett')
    for i in setdata:
        setlist.append(i.sett)
    platingtypedata = AutoAddMain.objects.filter(platingType__isnull = False).order_by('platingType')
    for i in platingtypedata:
        platingtypelist.append(i.platingType)
    rawmaterialdata = AutoAddMain.objects.filter(rawMaterial__isnull = False)
    for i in rawmaterialdata:
        rawmateriallist.append(i.rawMaterial)
    placeholder = {
        "clientname":clientnamelist,
        "moc":moclist,
        "tooltype":tooltypelist,
        "shape":shapelist,
        "tabletsize":tabletSizelist,
        "u1":u1list,
        "u2":u2list,
        "l1":l1list,
        "l2":l2list,
        "d":dlist,
        "set":setlist,
        "platingtype":platingtypelist,
        "rawmaterial":rawmateriallist,
        "dispachMode" : dispatchlist

    }
    isloggedin=""
    if request.user.is_user_role_1:
        user_id = request.user.id
        user_name = request.user.first_name
        isloggedin = "yes"
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
            orderremark = request.POST.get('orderremark')
            # rawmaterial = request.POST.get('rawmaterial')
            # priority = request.POST.get('priority')
            
            # edd = request.POST.get('edd')
            actualdeliverydate = request.POST.get('actualdeliverydate')
            modeofdispatch = request.POST.get('modeofdispatch')
            couriernumber = request.POST.get('couriernumber')

            if orderdate or clientname or value or moc or tooltype or shape or tabletsize or u1 or u2 or l1 or l2 or d or set or platingtype or actualdeliverydate or modeofdispatch or couriernumber :
                type="New Form"
                formadd = ProductionData(orderDate=orderdate,orderNumber=ordernumber,clientName=clientname,value=value,moc=moc,toolType=tooltype,shape=shape,tabletSize=tabletsize,u1=u1,u2=u2,l1=l1,l2=l2,d=d,sett=set,platingType=platingtype,order_remarks=orderremark,actualDelivery=actualdeliverydate,dispachMode=modeofdispatch,couriesNumber=couriernumber)
                log = UserLog(user_id=user_id,user_name=user_name,new_orderDate=orderdate,new_orderNumber=ordernumber ,new_clientName=clientname ,new_value=value ,new_moc=moc ,new_toolType=tooltype  ,new_shape=shape  ,new_tabletSize=tabletsize  ,new_u1=u1  ,new_u2=u2  ,new_l1=l1  ,new_l2=l2  ,new_d=d  ,new_sett=set  ,new_platingType=platingtype,new_order_remarks=orderremark,new_actualDelivery=actualdeliverydate ,new_dispachMode=modeofdispatch ,new_couriesNumber=couriernumber,Type=type)
                
                if formadd:
                    formadd.save()
                    log.save()
                    return redirect('index1')

        else:
            orderdate = ""
            ordernumber = ""
            clientname = ""
            value = ""
            moc = ""
            tooltype = ""
            shape = ""
            tabletsize = ""
            u1 = ""
            u2 = ""
            l1 = ""
            l2 = ""
            d = ""
            set = ""
            platingtype = ""
            rawmaterial = ""
            priority = ""
            status = ""
    params = {
        "isloggedin":isloggedin,
        "placeholder":placeholder
    }
    return render(request,"1add.html",params)




def index2(request):
    rawmaterial = ""
    priority=""
    update_punchBlankUsed = ""
    update_dieBlankUsed = ""
    errlogin=""
    alerta = ""
    a=""
    user_name=""
    tabledata= []
    placeholderdata = []
    update = ""
    updateform = ""
    mobile = ""
    salary = ""
    test = ""
    updateplaceholder = []
    blanklist = []
    processlist = []
    bodyTipMachininglist = []
    headMachininglist = []
    keywayTaperFinishlist = []
    htlist = []
    grindinglist = []
    hardChromelist = []
    qualityChecklist = []
    packingDispachlist = []
    rawmateriallist= []
    blankdata = AutoAddManufacturing.objects.filter(blank__isnull = False).order_by('blank')
    for i in blankdata:
        blanklist.append(i.blank)
    processdata = AutoAddManufacturing.objects.filter(process__isnull = False).order_by('process')
    for i in processdata:
        processlist.append(i.process)
    bodyTipMachiningdata = AutoAddManufacturing.objects.filter(bodyTipMachining__isnull = False).order_by('bodyTipMachining')
    for i in bodyTipMachiningdata:
        bodyTipMachininglist.append(i.bodyTipMachining)
    headMachiningdata = AutoAddManufacturing.objects.filter(headMachining__isnull = False).order_by('headMachining')
    for i in headMachiningdata:
        headMachininglist.append(i.headMachining)
    keywayTaperFinishdata = AutoAddManufacturing.objects.filter(keywayTaperFinish__isnull = False).order_by('keywayTaperFinish')
    for i in keywayTaperFinishdata:
        keywayTaperFinishlist.append(i.keywayTaperFinish)
    htdata = AutoAddManufacturing.objects.filter(ht__isnull = False).order_by('ht')
    for i in htdata:
        htlist.append(i.ht)
    grindingdata = AutoAddManufacturing.objects.filter(grinding__isnull = False).order_by('grinding')
    for i in grindingdata:
        grindinglist.append(i.grinding)
    hardChromedata = AutoAddManufacturing.objects.filter(hardChrome__isnull = False).order_by('hardChrome')
    for i in hardChromedata:
        hardChromelist.append(i.hardChrome)
    qualityCheckdata = AutoAddManufacturing.objects.filter(qualityCheck__isnull = False).order_by('qualityCheck')
    for i in qualityCheckdata:
        qualityChecklist.append(i.qualityCheck)
    packingDispachdata = AutoAddManufacturing.objects.filter(packingDispach__isnull = False).order_by('packingDispach')
    for i in packingDispachdata:
        packingDispachlist.append(i.packingDispach)
    dispatchlist = []
    dispatchdata = AutoAddDispatch.objects.filter(dispachMode__isnull = False).order_by('dispachMode')
    for i in dispatchdata:
        dispatchlist.append(i.dispachMode)
    rawmaterialdata = AutoAddMain.objects.filter(rawMaterial__isnull = False)
    for i in rawmaterialdata:
        rawmateriallist.append(i.rawMaterial)
    placeholder = {
        "blank" : blanklist,
        "process":processlist,
        "bodyTipMachining":bodyTipMachininglist,
        "headMachining":headMachininglist,
        "keywayTaperFinish":keywayTaperFinishlist,
        "ht":htlist,
        "grinding":grindinglist,
        "hardChrome":hardChromelist,
        "qualityCheck":qualityChecklist,
        "packingDispach":packingDispachlist,
        "dispachMode" : dispatchlist,
        "rawmaterial":rawmateriallist
    }
    
    if request.method == 'POST':
        test = request.POST.get('abc')
        print("test data is :",test)
        rawmaterial = request.POST.get('rawmaterial')
        priority = request.POST.get('priority')
        print(rawmaterial , priority)
        dwgnumber = request.POST.get('dwgnumber')
        drgdate = request.POST.get('drgdate')
        approvaldate = request.POST.get('approvaldate')
        master = request.POST.get('master')
        masterout = request.POST.get('masterout')
        masterin = request.POST.get('masterin')
        htdate = request.POST.get('htdate')
        estimateddelivery = request.POST.get('estimateddelivery')
        planningout = request.POST.get('planningout')
        planningin = request.POST.get('planningin')
        # print(dwgnumber)
        # print(drgdate)
        # print(approvaldate)
        # print(master)
        # print(masterout)
        # print(masterin)
        # print(htdate)
        # print(estimateddelivery)
        # print(planningout)
        # print(planningin)

        blank = request.POST.get('blank')
        process = request.POST.get('process')
        bodytipping = request.POST.get('bodytipping')
        headmachine = request.POST.get('headmachine')
        keyway = request.POST.get('keyway')
        ht = request.POST.get('ht')
        grinding = request.POST.get('grinding')
        hardchrome = request.POST.get('hardchrome')
        qualitycheck = request.POST.get('qualitycheck')
        packingdispach = request.POST.get('packingdispach')

        username = request.POST.get('username')
        password = request.POST.get('password')
        
        updateform = request.POST.get('updateform')
        
        if username and password:
            query = User.objects.filter(Q(username=username))
            if query:
                for i in query:
                    userid=i.id
                    userlvl = UserLevel.objects.get(user_id=userid)
                    level = userlvl.level
                    # print("logged in userlevel is :",level)
                    superuser = i.is_superuser
                    if superuser == False and level == 2:
                        authen = authenticate(username=username, password=password)
                        if authen:
                            login(request, authen)
                        else:
                            errlogin = "invalid"
                    else:
                        errlogin = "invalid"
            else:
                errlogin = "invalid"
        # if username and password:
        #     query = User.objects.filter(Q(username=username))
        #     for i in query:
        #         superuser = i.is_superuser
        #         if superuser == False:
        #             authen = authenticate(username=username, password=password)
        #             if authen:
        #                 login(request, authen)
    else:
        dwgnumber = ""
        drgdate = ""
        approvaldate = ""
        master = ""
        masterout = ""
        masterin = ""
        htdate = ""
        estimateddelivery = ""
        planningout = ""
        planningin = ""

        blank = ""
        process = ""
        bodytipping = ""
        headmachine = ""
        keyway = ""
        ht = ""
        grinding = ""
        hardchrome = ""
        qualitycheck = ""
        packingdispach = ""
    if request.user.is_user_role_2:
        user_id = request.user.id
        user_name = request.user.first_name
        # print("logedin user name is :",user_name)
        # print("loged in user is:",user_id)
        lvl = 2
        if lvl == 2:
            a="yes"
        else:
            a='no'
        
        form = ProductionData.objects.all()
        for xj in form:
            data_id= xj.id
            data_orderdate1  = xj.orderDate
            data_orderdate = datetime.datetime.strptime(data_orderdate1, "%Y-%m-%d").strftime("%d-%m-%Y")
            data_ordernumber    = xj.orderNumber
            data_clientname =xj.clientName
            data_value =xj.value
            data_moc = xj.moc
            data_tooltype =xj.toolType
            data_shape =xj.shape
            data_tabletsize =xj.tabletSize
            data_u1 =xj.u1
            data_u2 =xj.u2
            data_l1 =xj.l1
            data_l2 =xj.l2
            data_d =xj.d
            data_set =xj.sett
            data_platingtype =xj.platingType
            data_rawmaterial =xj.rawMaterial
            data_priority =xj.priority
            data_orderremark = xj.order_remarks
            data_edd = xj.estimatedDelivery
            data_actualdd=xj.actualDelivery
            
            # print("edd :",data_edd)
            # print("actual edd :",data_actualdd)
            data1 = xj.blank
            data2 = xj.process
            data3 = xj.bodyTipMachining
            data4 = xj.headMachining
            data5 = xj.keywayTaperFinish
            data6 = xj.ht
            data7 = xj.grinding
            data8 = xj.hardChrome
            data9 = xj.qualityCheck
            data10 = xj.packingDispach
            
            
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
            
            if data_orderdate and data_ordernumber and data_clientname and data_value and data_moc and data_tooltype and data_shape and data_tabletsize and data_u1 and data_u2 and data_l1 and data_l2 and data_d and data_set and data_platingtype  :
                obj = {
                "id":data_id,
                "orderdate" : data_orderdate,
                "ordernumber" :data_ordernumber,
                "clientname" :data_clientname,
                "value" :data_value,
                "moc" :data_moc,
                "tooltype" :data_tooltype,
                "shape" :data_shape,
                "tabletsize" :data_tabletsize,
                "u1" :data_u1,
                "u2" :data_u2,
                "l1" :data_l1,
                "l2" :data_l2,
                "d" :data_d,
                "set" :data_set,
                "platingtype" :data_platingtype,
                "rawmaterial" :data_rawmaterial,
                "priority" :data_priority,
                "remarks":data_orderremark,
                "status" :data_status,
                'edd':data_edd,
                'actualdeliverydate':data_actualdd
            }
            tabledata.append(obj)
        
        if test:
            udata = ProductionData.objects.get(orderNumber = test)
            print(udata)
            data1 = udata.blank
            data2 = udata.process
            data3 = udata.bodyTipMachining
            data4 = udata.headMachining
            data5 = udata.keywayTaperFinish
            data6 = udata.ht
            data7 = udata.grinding
            data8 = udata.hardChrome
            data9 = udata.qualityCheck
            data10 = udata.packingDispach
            # print(data1)
            # print(data2)
            # print(data3)
            # print(data4)
            # print(data5)
            # print(data6)
            # print(data7)
            # print(data8)
            # print(data9)
            # print(data10)
            
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
            print("total is :",totaldata)
            data_status = str(totaldata) + str("%")
            if data_status:
                udata.status = data_status
                udata.save()
            if udata.u1 and udata.l1:
                udata.punchBlankUsed = int(udata.u1) + int(udata.l1)
                udata.save()
            if udata.d:
                udata.dieBlankUsed = udata.d
                udata.save()
            
        # else:
        #     print("no didnt get")
        #     update = "no"
        # if 'updateformid'  in request.session:
        #     sessdata = request.session['updateformid']
        # else:
        #     sessdata = ""
        if test:
            check = ProductionData.objects.get(orderNumber=test)
            request.session['id'] = check.id
            punchblank = int(check.u1) + int(check.l1)
            dieblank = int(check.d)
            print("lala",punchblank,dieblank)
            print("set",check.sett)
            passdata = {
                "set" : check.sett,
                "rawmaterial" : check.rawMaterial,
                "priority" : check.priority,
                "dwgnumber" : check.dwgNumber,
                "drgdate" : check.drgDate,
                "approvaldate" : check.approvalDate,
                "master" : check.master,
                "masterout" : check.masterOut,
                "masterin" : check.masterIn,
                "punchblank":punchblank,
                "dieblank":dieblank,
                "htdate" : check.hitDate,
                "estimateddelivery" : check.estimatedDelivery,
                "planningout" : check.planningOut,
                "planningin" : check.planningIn,
                "orderdate" : check.orderDate,
                "ordernumber" : check.orderNumber,
                "clientname" :check.clientName,
                "value" : check.value,
                "moc" : check.moc,
                "tooltype" : check.toolType,
                "shape" : check.shape,
                "tabletsize" : check.tabletSize,
                "u1" : check.u1,
                "u2" : check.u2,
                "l1" : check.l1,
                "l2" : check.l2,
                "d" : check.d,
                
                "platingtype" : check.platingType,
                "orderremark" : check.order_remarks,
                "actualdeliverydate" : check.actualDelivery,
                "modeofdispatch" : check.dispachMode,
                "couriernumber" : check.couriesNumber,               
                "blank" : check.blank,
                "process" : check.process,
                "bodytipping" : check.bodyTipMachining,
                "headmachine" : check.headMachining,
                "keyway" : check.keywayTaperFinish,
                "ht" : check.ht,
                "grinding" : check.grinding,
                "hardchrome" : check.hardChrome,
                "qualitycheck" : check.qualityCheck,
                "packingdispach" : check.packingDispach

            }
            return JsonResponse({"passdata":passdata})
        if 'id' in request.session:
            sessdata = request.session['id']
        if rawmaterial or priority or dwgnumber or drgdate or approvaldate or master or masterout or masterin or htdate or estimateddelivery or planningout or planningin or blank or process or bodytipping or headmachine or keyway or ht or grinding or hardchrome or qualitycheck or packingdispach :
            print("yes satisfied")
            print("logged in user is blah :",user_id,user_name)
            form = ProductionData.objects.get(id = sessdata)
            type="Updated"
            # status=form.status,dwgNumber=form.dwgNumber,drgDate=form.drgDate,approvalDate=form.approvalDate,master=form.master,masterOut=form.masterOut,masterIn=form.masterIn,punchBlankUsed=form.punchBlankUsed,dieBlankUsed=form.dieBlankUsed,hitDate=form.hitDate,estimatedDelivery=form.estimatedDelivery,planningOut=form.planningOut,planningIn=form.planningIn,blank=form.blank,process=form.process,bodyTipMachining=form.bodyTipMachining,headMachining=form.headMachining,keywayTaperFinish=form.keywayTaperFinish,ht=form.ht,grinding=form.grinding,hardChrome=form.hardChrome,qualityCheck=form.qualityCheck,packingDispach=form.packingDispach
            log = UserLog(formid=sessdata,user_id=user_id,user_name=user_name,rawMaterial=form.rawMaterial,priority=form.priority,dwgNumber=form.dwgNumber,drgDate=form.drgDate,approvalDate=form.approvalDate,master=form.master,masterOut=form.masterOut,masterIn=form.masterIn,hitDate=form.hitDate,estimatedDelivery=form.estimatedDelivery,planningOut=form.planningOut,planningIn=form.planningIn,blank=form.blank,process=form.process,bodyTipMachining=form.bodyTipMachining,headMachining=form.headMachining,keywayTaperFinish=form.keywayTaperFinish,ht=form.ht,grinding=form.grinding,hardChrome=form.hardChrome,qualityCheck=form.qualityCheck,packingDispach=form.packingDispach,new_rawMaterial=rawmaterial,new_priority=priority,new_dwgNumber=dwgnumber,new_drgDate=drgdate,new_approvalDate=approvaldate,new_master=master,new_masterOut=masterout,new_masterIn=masterin,new_hitDate=htdate,new_estimatedDelivery=estimateddelivery,new_planningOut=planningout,new_planningIn=planningin,new_blank=blank,new_process=process,new_bodyTipMachining=bodytipping,new_headMachining=headmachine,new_keywayTaperFinish=keyway,new_ht=ht,new_grinding=grinding,new_hardChrome=hardchrome,new_qualityCheck=qualitycheck,new_packingDispach=packingdispach,Type=type)
            log.save()
            if rawmaterial:
                form.rawMaterial = rawmaterial
                form.save()
            if priority:
                form.priority = priority
                form.save()
            if dwgnumber:
                print("got dwgnumber")
                form.dwgNumber = dwgnumber
                form.save()
            if drgdate:
                form.drgDate = drgdate
                form.save()
            if approvaldate:
                form.approvalDate = approvaldate
                form.save()
            if master:
                form.master = master
                form.save()
            if masterout:
                form.masterOut = masterout
                form.save()
            if masterin:
                form.masterIn = masterin
                form.save()
            if htdate:
                form.hitDate = htdate
                form.save()
            if estimateddelivery:
                form.estimatedDelivery = estimateddelivery
                form.save()
            if planningout:
                form.planningOut = planningout
                form.save()
            if planningin:
                form.planningIn = planningin
                form.save()
            if blank:
                print("yes blank")
                form.blank = blank
                form.save()
            if process:
                form.process = process
                form.save()
            if bodytipping:
                form.bodyTipMachining = bodytipping
                form.save()
            if headmachine:
                form.headMachining = headmachine
                form.save()
            if keyway:
                form.keywayTaperFinish = keyway
                form.save()
            if ht:
                form.ht = ht
                form.save()
            if grinding:
                form.grinding = grinding
                form.save()
            if hardchrome:
                form.hardChrome = hardchrome
                form.save()
            if qualitycheck:
                form.qualityCheck = qualitycheck
                form.save()
            if packingdispach:
                form.packingDispach = packingdispach
                form.save()
            alerta = "yes"
            return redirect('index2')
        else:
            print("not satisfied")
    
    return render(request,"dashboard_user2.html",{"errlogin":errlogin,"alerta":alerta,"data":a,"name":user_name,"tabledata":tabledata,"update":update,"updateplaceholder":updateplaceholder,"placeholder":placeholder})






def admin(request):
    data_status = ""
    test = ""
    clientnamelist = []
    moclist = []
    tooltypelist = []
    shapelist = []
    tabletSizelist = []
    u1list = []
    u2list = []
    l1list = []
    l2list = []
    dlist = []
    setlist = []
    platingtypelist = []
    rawmateriallist = []
    blanklist = []
    processlist = []
    bodyTipMachininglist = []
    headMachininglist = []
    keywayTaperFinishlist = []
    htlist = []
    grindinglist = []
    hardChromelist = []
    qualityChecklist = []
    packingDispachlist = []
    dispatchlist = []
    dispatchdata = AutoAddDispatch.objects.filter(dispachMode__isnull = False)
    for i in dispatchdata:
        dispatchlist.append(i.dispachMode)
    blankdata = AutoAddManufacturing.objects.filter(blank__isnull = False)
    for i in blankdata:
        blanklist.append(i.blank)
    processdata = AutoAddManufacturing.objects.filter(process__isnull = False)
    for i in processdata:
        processlist.append(i.process)
    bodyTipMachiningdata = AutoAddManufacturing.objects.filter(bodyTipMachining__isnull = False)
    for i in bodyTipMachiningdata:
        bodyTipMachininglist.append(i.bodyTipMachining)
    headMachiningdata = AutoAddManufacturing.objects.filter(headMachining__isnull = False)
    for i in headMachiningdata:
        headMachininglist.append(i.headMachining)
    keywayTaperFinishdata = AutoAddManufacturing.objects.filter(keywayTaperFinish__isnull = False)
    for i in keywayTaperFinishdata:
        keywayTaperFinishlist.append(i.keywayTaperFinish)
    htdata = AutoAddManufacturing.objects.filter(ht__isnull = False)
    for i in htdata:
        htlist.append(i.ht)
    grindingdata = AutoAddManufacturing.objects.filter(grinding__isnull = False)
    for i in grindingdata:
        grindinglist.append(i.grinding)
    hardChromedata = AutoAddManufacturing.objects.filter(hardChrome__isnull = False)
    for i in hardChromedata:
        hardChromelist.append(i.hardChrome)
    qualityCheckdata = AutoAddManufacturing.objects.filter(qualityCheck__isnull = False)
    for i in qualityCheckdata:
        qualityChecklist.append(i.qualityCheck)
    packingDispachdata = AutoAddManufacturing.objects.filter(packingDispach__isnull = False)
    for i in packingDispachdata:
        packingDispachlist.append(i.packingDispach)
    clientnamedata = CustomerDetail.objects.filter(customerCompanyName__isnull = False).order_by('customerCompanyName')
    for i in clientnamedata:
        clientnamelist.append(i.customerCompanyName)
    mocdata = AutoAddMain.objects.filter(moc__isnull = False)
    for i in mocdata:
        moclist.append(i.moc)
    tooltypedata = AutoAddMain.objects.filter(toolType__isnull = False)
    for i in tooltypedata:
        tooltypelist.append(i.toolType)
    shapedata = AutoAddMain.objects.filter(shape__isnull = False)
    for i in shapedata:
        shapelist.append(i.shape)
    tabletdata = AutoAddMain.objects.filter(tabletSize__isnull = False)
    for i in tabletdata:
        tabletSizelist.append(i.tabletSize)
    u1data = AutoAddMain.objects.filter(u1__isnull = False)
    for i in u1data:
        u1list.append(i.u1)
    u2data = AutoAddMain.objects.filter(u2__isnull = False)
    for i in u2data:
        u2list.append(i.u2)
    l1data = AutoAddMain.objects.filter(l1__isnull = False)
    for i in l1data:
        l1list.append(i.l1)
    l2data = AutoAddMain.objects.filter(l2__isnull = False)
    for i in l2data:
        l2list.append(i.l2)
    ddata = AutoAddMain.objects.filter(d__isnull = False)
    for i in ddata:
        dlist.append(i.d)
    setdata = AutoAddMain.objects.filter(sett__isnull = False)
    for i in setdata:
        setlist.append(i.sett)
    platingtypedata = AutoAddMain.objects.filter(platingType__isnull = False)
    for i in platingtypedata:
        platingtypelist.append(i.platingType)
    rawmaterialdata = AutoAddMain.objects.filter(rawMaterial__isnull = False)
    for i in rawmaterialdata:
        rawmateriallist.append(i.rawMaterial)
    placeholder = {
        "clientname":clientnamelist,
        "moc":moclist,
        "tooltype":tooltypelist,
        "shape":shapelist,
        "tabletsize":tabletSizelist,
        "u1":u1list,
        "u2":u2list,
        "l1":l1list,
        "l2":l2list,
        "d":dlist,
        "set":setlist,
        "platingtype":platingtypelist,
        "rawmaterial":rawmateriallist,
        "blank" : blanklist,
        "process":processlist,
        "bodyTipMachining":bodyTipMachininglist,
        "headMachining":headMachininglist,
        "keywayTaperFinish":keywayTaperFinishlist,
        "ht":htlist,
        "grinding":grindinglist,
        "hardChrome":hardChromelist,
        "qualityCheck":qualityChecklist,
        "packingDispach":packingDispachlist,
        "dispatchlist":dispatchlist
    }
    # print(placeholder)
    errlogin=""
    a = ''
    user_name=""
    view = ""
    tabledata = []
    deleteid = ""
    update = ""
    updateform = []
    status_bg=""
    bgcolor = ""
    test = ""
    updateplaceholder = []
    if request.method == 'POST':
        test = request.POST.get('abc')
        print("test data is :",test)
        username = request.POST.get('username')
        password = request.POST.get('password')
        viewform = request.POST.get('viewform')
        updateform = request.POST.get('updateform')
        deleteform = request.POST.get('deleteform')
        
        addusername = request.POST.get('addusername')
        addpassword = request.POST.get('addpassword')
        addlevel = request.POST.get('addlevel')


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
        orderremark = request.POST.get('orderremark')
        rawmaterial = request.POST.get('rawmaterial')
        priority = request.POST.get('priority')
        status = request.POST.get('status')    
        dwgnumber = request.POST.get('dwgnumber')
        drgdate = request.POST.get('drgdate')
        approvaldate = request.POST.get('approvaldate')
        master = request.POST.get('master')
        masterout = request.POST.get('masterout')
        masterin = request.POST.get('masterin')
        punchblank = request.POST.get('punchblank')
        dieblank = request.POST.get('dieblank')
        htdate = request.POST.get('htdate')
        estimateddelivery = request.POST.get('estimateddelivery')
        planningout = request.POST.get('planningout')
        planningin = request.POST.get('planningin')
        blank = request.POST.get('blank')
        process = request.POST.get('process')
        bodytipping = request.POST.get('bodytipping')
        headmachine = request.POST.get('headmachine')
        keyway = request.POST.get('keyway')
        ht = request.POST.get('ht')
        grinding = request.POST.get('grinding')
        hardchrome = request.POST.get('hardchrome')
        qualitycheck = request.POST.get('qualitycheck')
        packingdispach = request.POST.get('packingdispach')
        edd = request.POST.get('edd')
        actualdeliverydate = request.POST.get('actualdeliverydate')
        modeofdispatch = request.POST.get('modeofdispatch')
        couriernumber = request.POST.get('couriernumber')
        remarks = request.POST.get('remarks')
        # add data into tables as select options
        addlientname = request.POST.get('addlientname')
        addmoc = request.POST.get('addmoc')
        addtooltype = request.POST.get('addtooltype')
        addshape = request.POST.get('addshape')
        addtabletsize = request.POST.get('addtabletsize')
        addu1 = request.POST.get('addu1')
        addu2 = request.POST.get('addu2')
        addl1 = request.POST.get('addl1')
        addl2 = request.POST.get('addl2')
        addd = request.POST.get('addd')
        addset = request.POST.get('addset')
        addplatingtype = request.POST.get('addplatingtype')
        addrawmaterial = request.POST.get('addrawmaterial')

        addpunchblank = request.POST.get('addpunchblank')
        adddieblank = request.POST.get('adddieblank')


        addblank = request.POST.get('addblank')
        addprocess = request.POST.get('addprocess')
        addbodytipping = request.POST.get('addbodytipping')
        addheadmachining = request.POST.get('addheadmachining')
        addkeyway = request.POST.get('addkeyway')
        addht = request.POST.get('addht')
        addgrinding = request.POST.get('addgrinding')
        addhardchrome = request.POST.get('addhardchrome')
        addqualitycheck = request.POST.get('addqualitycheck')
        addpackaging = request.POST.get('addpackaging')
        
        adddispachmode = request.POST.get('adddispachmode')

        

        # print(orderdate)
        # print(ordernumber) 
        # print(clientname )
        # print(value )
        # print(moc )
        # print(tooltype) 
        # print(shape )
        # print(tabletsize) 
        # print(u1 )
        # print(u2 )
        # print(l1 )
        # print(l2 )
        # print(d )
        # print(set) 
        # print(platingtype) 
        # print(rawmaterial)
        # print(priority)
        # print(status   )
        # print(dwgnumber )
        # print(drgdate )
        # print(approvaldate)
        # print(master ) 
        # print(masterout) 
        # print(masterin )
        # print(punchblank)
        # print(dieblank )
        # print(htdate )
        # print(estimateddelivery)
        # print(planningout  )
        # print(planningin  )
        # print(blank  )
        # print(process ) 
        # print(bodytipping ) 
        # print(headmachine  )
        # print(keyway )
        # print(ht  )
        # print(grinding ) 
        # print(hardchrome )
        # print(qualitycheck  )
        # print(packingdispach  )
        # print(edd  )
        # print(actualdeliverydate ) 
        # print(modeofdispatch  )
        # print(couriernumber  )
        #login check/authenticate..and login
        if username and password:
            query = User.objects.filter(Q(username=username))
            if query:
                for i in query:
                    userid=i.id
                    userlvl = UserLevel.objects.get(user_id=userid)
                    level = userlvl.level
                    # print("logged in userlevel is :",level)
                    superuser = i.is_superuser
                    if superuser == True and level == 5:
                        authen = authenticate(username=username, password=password)
                        if authen:
                            login(request, authen)
                        else:
                            errlogin = "invalid"
                    else:
                        errlogin = "invalid"
            else:
                errlogin = "invalid"
        # if username and password:
        #     # print(username,password)
        #     query = User.objects.filter(Q(username=username))
        #     for i in query:
        #         superuser = i.is_superuser
        #         if superuser == True:
        #             authen = authenticate(username=username, password=password)
        #             if authen:
        #                 login(request, authen)
            

        #creation of normal users level 1 to 3
        
    else:
        orderdate= ""
        ordernumber= "" 
        clientname = ""
        value = ""
        moc = ""
        tooltype= "" 
        shape = ""
        tabletsize= "" 
        u1 = ""
        u2 = ""
        l1 = ""
        l2 = ""
        d = ""
        set= "" 
        platingtype= "" 
        rawmaterial= ""
        priority= ""
        status   = ""
        dwgnumber = ""
        drgdate = ""
        approvaldate= ""
        master = "" 
        masterout= "" 
        masterin = ""
        punchblank= ""
        dieblank = ""
        htdate = ""
        estimateddelivery= ""
        planningout  = ""
        planningin  = ""
        blank  = ""
        process = "" 
        bodytipping = "" 
        headmachine  = ""
        keyway = ""
        ht  = ""
        grinding = "" 
        hardchrome = ""
        qualitycheck  = ""
        packingdispach  = ""
        edd  = ""
        actualdeliverydate = "" 
        modeofdispatch  = ""
        couriernumber  = ""
        deleteform = ""
        viewform = ""

        addlientname = ""
        addmoc =''
        addtooltype = ''
        addshape = ''
        addtabletsize =''
        addu1 = ''
        addu2 = ''
        addl1 = ''
        addl2 = ''
        addd = ''
        addset = ''
        addplatingtype = ''
        addrawmaterial = ''


        addpunchblank=''
        adddieblank = ''

        orderremark=''
        addblank = ''
        addprocess = ''
        addbodytipping = ''
        addheadmachining = ''
        addkeyway = ''
        addht = ''
        addgrinding = ''
        addhardchrome = ''
        addqualitycheck = ''
        addpackaging = ''
        remarks = ''
        adddispachmode = ''
        
    if request.user.is_authenticated:
        user_id = request.user.id
        user_name = request.user.username
        abcd = User.objects.get(id=user_id)
        if abcd.is_superuser == True:
            a = "yes"
        else:
            a = "no"
        # print("logedin user name is :",user_name)
        # print("loged in user is:",user_id)
        
        # print("user id is:",user_id)
        
            # for j in userlevel:
            #     print("loop :1")
            form = ProductionData.objects.all()
            for x in form:
                data_id= x.id
                data_orderdate1  = x.orderDate
                data_orderdate = datetime.datetime.strptime(data_orderdate1, "%Y-%m-%d").strftime("%d-%m-%Y")
                data_ordernumber    = x.orderNumber
                data_clientname =x.clientName
                data_value =x.value
                data_moc = x.moc
                data_tooltype =x.toolType
                data_shape =x.shape
                data_tabletsize =x.tabletSize
                data_u1 =x.u1
                data_u2 =x.u2
                data_l1 =x.l1
                data_l2 =x.l2
                data_d =x.d
                data_set =x.sett
                data_platingtype =x.platingType
                data_rawmaterial =x.rawMaterial
                data_priority =x.priority
                data_orderremark = x.order_remarks
                data_dwgNumber = x.dwgNumber
                data_drgDate = x.drgDate
                data_approvalDate = x.approvalDate
                data_master = x.master
                data_masterOut = x.masterOut
                data_masterIn = x.masterIn
                if data_u1 and data_u2:
                    data_punchBlankUsed = int(data_u1)+ int(data_l1)
                else:
                    data_punchBlankUsed =0
                # print(data_punchBlankUsed)
                data_dieBlankUsed = data_d
                data_hitDate = x.hitDate
                data_estimatedDelivery = x.estimatedDelivery
                data_planningOut=x.planningOut
                data_planningIn=x.planningIn
                data_blank=x.blank
                data_process=x.process
                data_bodyTipMachining=x.bodyTipMachining
                data_headMachining=x.headMachining
                data_keywayTaperFinish=x.keywayTaperFinish
                data_ht=x.ht
                data_grinding=x.grinding
                data_hardChrome=x.hardChrome
                data_qualityCheck=x.qualityCheck
                data_packingDispach=x.packingDispach
                data_estimatedDelivery=x.estimatedDelivery
                data_actualDelivery=x.actualDelivery
                data_dispachMode=x.dispachMode
                data_couriesNumber=x.couriesNumber
                data_remark=x.remark
                data1 = x.blank
                data2 = x.process
                data3 = x.bodyTipMachining
                data4 = x.headMachining
                data5 = x.keywayTaperFinish
                data6 = x.ht
                data7 = x.grinding
                data8 = x.hardChrome
                data9 = x.qualityCheck
                data10 = x.packingDispach
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
                # print(totaldata%2)
                data_status = str(totaldata) + str("%")

                # print("status is :",data_id,data_status)
                if data_orderdate or data_ordernumber or data_clientname or data_value or data_moc or data_tooltype or data_shape or data_tabletsize or data_u1 or data_u2 or data_l1 or data_l2 or data_d or data_set or data_platingtype or data_rawmaterial or data_priority or data_status:
                    obj = {
                        "id":data_id,
                        "orderdate" : data_orderdate,
                        "ordernumber" :data_ordernumber,
                        "clientname" :data_clientname,
                        "value" :data_value,
                        "moc" :data_moc,
                        "tooltype" :data_tooltype,
                        "shape" :data_shape,
                        "tabletsize" :data_tabletsize,
                        "u1" :data_u1,
                        "u2" :data_u2,
                        "l1" :data_l1,
                        "l2" :data_l2,
                        "d" :data_d,
                        "set" :data_set,
                        "platingtype" :data_platingtype,
                        "rawmaterial" :data_rawmaterial,
                        "priority" :data_priority,
                        "remarks":data_orderremark,
                        
                        "status" :data_status,
                        "dwgNumber" :  data_dwgNumber,
                        "drgDate" :  data_drgDate,
                        "approvalDate" :  data_approvalDate,
                        "master" :  data_master,
                        "masterOut" :  data_masterOut,
                        "masterIn" :  data_masterIn,
                        "punchBlankUsed" :  data_punchBlankUsed,
                        "dieBlankUsed" :  data_dieBlankUsed,
                        "hitDate" :  data_hitDate,
                        "estimatedDelivery" :  data_estimatedDelivery,
                        "planningOut": data_planningOut,
                        "planningIn": data_planningIn,
                        "blank": data_blank,
                        "process": data_process,
                        "bodyTipMachining": data_bodyTipMachining,
                        "headMachining": data_headMachining,
                        "keywayTaperFinish": data_keywayTaperFinish,
                        "ht": data_ht,
                        "grinding": data_grinding,
                        "hardChrome": data_hardChrome,
                        "qualityCheck": data_qualityCheck,
                        "packingDispach": data_packingDispach,
                        "estimatedDelivery": data_estimatedDelivery,
                        "actualDelivery": data_actualDelivery,
                        "dispachMode": data_dispachMode,
                        "couriesNumber": data_couriesNumber,
                        "remark": data_remark

                    }
                    tabledata.append(obj)
        
        if test:
            udata = ProductionData.objects.get(orderNumber = test)
            print(udata)
            data1 = udata.blank
            data2 = udata.process
            data3 = udata.bodyTipMachining
            data4 = udata.headMachining
            data5 = udata.keywayTaperFinish
            data6 = udata.ht
            data7 = udata.grinding
            data8 = udata.hardChrome
            data9 = udata.qualityCheck
            data10 = udata.packingDispach
            # print(data1)
            # print(data2)
            # print(data3)
            # print(data4)
            # print(data5)
            # print(data6)
            # print(data7)
            # print(data8)
            # print(data9)
            # print(data10)
            
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
            print("total is :",totaldata)
            data_status = str(totaldata) + str("%")
            if data_status:
                udata.status = data_status
                udata.save()
            if udata.u1 and udata.l1:
                udata.punchBlankUsed = int(udata.u1) + int(udata.l1)
                udata.save()
            if udata.d:
                udata.dieBlankUsed = udata.d
                udata.save()
        if test:
            check = ProductionData.objects.get(orderNumber=test)
            request.session['id'] = check.id
            punchblank = int(check.u1) + int(check.l1)
            dieblank = int(check.d)
            print(punchblank,dieblank)
            
            passdata = {
                
                "rawmaterial" : check.rawMaterial,
                "priority" : check.priority,
                "dwgnumber" : check.dwgNumber,
                "drgdate" : check.drgDate,
                "approvaldate" : check.approvalDate,
                "master" : check.master,
                "masterout" : check.masterOut,
                "masterin" : check.masterIn,
                "punchblank":punchblank,
                "dieblank":dieblank,
                "htdate" : check.hitDate,
                "estimateddelivery" : check.estimatedDelivery,
                "planningout" : check.planningOut,
                "planningin" : check.planningIn,
                
                "blank" : check.blank,
                "process" : check.process,
                "bodytipping" : check.bodyTipMachining,
                "headmachine" : check.headMachining,
                "keyway" : check.keywayTaperFinish,
                "ht" : check.ht,
                "grinding" : check.grinding,
                "hardchrome" : check.hardChrome,
                "qualitycheck" : check.qualityCheck,
                "packingdispach" : check.packingDispach,

                "orderdate" : check.orderDate,
                "ordernumber" : check.orderNumber,
                "clientname" :check.clientName,
                "value" : check.value,
                "moc" : check.moc,
                "tooltype" : check.toolType,
                "shape" : check.shape,
                "tabletsize" : check.tabletSize,
                "u1" : check.u1,
                "u2" : check.u2,
                "l1" : check.l1,
                "l2" : check.l2,
                "d" : check.d,
                "set" : check.sett,
                "platingtype" : check.platingType,
                "orderremark" : check.order_remarks,
                "actualdeliverydate" : check.actualDelivery,
                "modeofdispatch" : check.dispachMode,
                "couriernumber" : check.couriesNumber
            }
            return JsonResponse({"passdata":passdata})
        if viewform:
            view = "yes"
        else:
            view = "no"
        
        
        if 'updateformid'  in request.session:
            sessdata = request.session['updateformid']
        else:
            sessdata = ""
        if deleteform:
            print("Form Number :",deleteform," is deleted !")
            delobject = ProductionData.objects.get(id = deleteform)
            if delobject:
                delobject.delete()
                return redirect('admin')
        if 'id' in request.session:
            sessdata = request.session['id']
        if orderdate or ordernumber or clientname or value or moc or tooltype  or shape  or tabletsize  or u1  or u2  or l1  or l2  or d  or set  or platingtype or orderremark or rawmaterial  or priority  or status or dwgnumber or drgdate or approvaldate or master or masterout or masterin  or htdate or estimateddelivery or planningout or planningin or blank or process or bodytipping or headmachine or keyway or ht or grinding or hardchrome or qualitycheck or packingdispach or edd or actualdeliverydate or modeofdispatch or couriernumber or remarks:
            print("yes satisfied")
            form = ProductionData.objects.get(id = sessdata)
            type="Updated"
            log = UserLog(formid=sessdata,user_id=user_id,user_name=user_name,orderDate=form.orderDate,orderNumber=form.orderNumber,clientName=form.clientName,value=form.value,moc=form.moc,toolType=form.toolType,shape=form.shape,tabletSize=form.tabletSize,u1=form.u1,u2=form.u2,l1=form.l1,l2=form.l2,d=form.d,sett=form.sett,platingType=form.platingType,order_remarks=form.order_remarks,actualDelivery=form.actualDelivery,dispachMode=form.dispachMode,couriesNumber=form.couriesNumber,new_orderDate=orderdate,new_orderNumber=ordernumber ,new_clientName=clientname ,new_value=value ,new_moc=moc ,new_toolType=tooltype  ,new_shape=shape  ,new_tabletSize=tabletsize  ,new_u1=u1  ,new_u2=u2  ,new_l1=l1  ,new_l2=l2  ,new_d=d  ,new_sett=set  ,new_platingType=platingtype,new_order_remarks=orderremark,new_actualDelivery=actualdeliverydate ,new_dispachMode=modeofdispatch ,new_couriesNumber=couriernumber,rawMaterial=form.rawMaterial,priority=form.priority,dwgNumber=form.dwgNumber,drgDate=form.drgDate,approvalDate=form.approvalDate,master=form.master,masterOut=form.masterOut,masterIn=form.masterIn,hitDate=form.hitDate,estimatedDelivery=form.estimatedDelivery,planningOut=form.planningOut,planningIn=form.planningIn,blank=form.blank,process=form.process,bodyTipMachining=form.bodyTipMachining,headMachining=form.headMachining,keywayTaperFinish=form.keywayTaperFinish,ht=form.ht,grinding=form.grinding,hardChrome=form.hardChrome,qualityCheck=form.qualityCheck,packingDispach=form.packingDispach,new_rawMaterial=rawmaterial,new_priority=priority,new_dwgNumber=dwgnumber,new_drgDate=drgdate,new_approvalDate=approvaldate,new_master=master,new_masterOut=masterout,new_masterIn=masterin,new_hitDate=htdate,new_estimatedDelivery=estimateddelivery,new_planningOut=planningout,new_planningIn=planningin,new_blank=blank,new_process=process,new_bodyTipMachining=bodytipping,new_headMachining=headmachine,new_keywayTaperFinish=keyway,new_ht=ht,new_grinding=grinding,new_hardChrome=hardchrome,new_qualityCheck=qualitycheck,new_packingDispach=packingdispach,Type=type)
            log.save()
            if orderdate:
                form.orderDate = orderdate
                form.save()
            if ordernumber:
                form.orderNumber = ordernumber
                form.save()
            if clientname:
                form.clientName = clientname
                form.save()
            if value:
                form.value = value
                form.save()
            if moc:
                form.moc = moc
                form.save()
            if tooltype:
                form.toolType = tooltype
                form.save()
            if shape:
                form.shape = shape
                form.save()
            if tabletsize:
                form.tabletSize = tabletsize
                form.save()
            if u1:
                form.u1 = u1
                form.save()
            if u2:
                form.u2 = u2
                form.save()
            if l1:
                form.l1 = l1
                form.save()
            if l2:
                form.l2 = l2
                form.save()
            if d:
                form.d = d
                form.save()
            if set:
                form.sett = set
                form.save()
            if platingtype:
                form.platingType = platingtype
                form.save()
            if orderremark:
                form.order_remarks = orderremark
                form.save()
            if rawmaterial:
                form.rawMaterial = rawmaterial
                form.save()
            if priority:
                form.priority = priority
                form.save()
            if status:
                form.status = status
                form.save()
            if dwgnumber:
                form.dwgNumber = dwgnumber
                form.save()
            if drgdate:
                form.drgDate = drgdate
                form.save()
            if approvaldate:
                form.approvalDate = approvaldate
                form.save()
            if master:
                form.master = master
                form.save()
            if masterout:
                form.masterOut = masterout
                form.save()
            if masterin:
                form.masterIn = masterin
                form.save()
            if htdate:
                form.hitDate = htdate
                form.save()
            if estimateddelivery:
                form.estimatedDelivery = estimateddelivery
                form.save()
            if planningout:
                form.planningOut = planningout
                form.save()
            if planningin:
                form.planningIn = planningin
                form.save()
            if blank:
                print("yes blank")
                form.blank = blank
                form.save()
            if process:
                form.process = process
                form.save()
            if bodytipping:
                form.bodyTipMachining = bodytipping
                form.save()
            if headmachine:
                form.headMachining = headmachine
                form.save()
            if keyway:
                form.keywayTaperFinish = keyway
                form.save()
            if ht:
                form.ht = ht
                form.save()
            if grinding:
                form.grinding = grinding
                form.save()
            if hardchrome:
                form.hardChrome = hardchrome
                form.save()
            if qualitycheck:
                form.qualityCheck = qualitycheck
                form.save()
            if packingdispach:
                form.packingDispach = packingdispach
                form.save()
            if edd:
                form.estimatedDelivery = edd
                form.save()
            if actualdeliverydate:
                form.actualDelivery = actualdeliverydate
                form.save()
            if modeofdispatch:
                form.dispachMode = modeofdispatch
                form.save()
            if couriernumber:
                form.couriesNumber = couriernumber
                form.save()
            if remarks:
                form.remark = remarks
                form.save()
            print("remarks is",remarks)
            return redirect('admin')
                
               
    if updateform:
        print("Updated Element is :",updateform)
    print(updateplaceholder)
    return render(request,"admin.html",{"view":view,"errlogin":errlogin,"data":a,"name":user_name,"tabledata":tabledata,"updateplaceholder":updateplaceholder,"update":update,"placeholder":placeholder})

def customer_detail(request):
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
            
    return render(request,"admin_addcustomer.html")

def customerCheck(request):
    customername = ''
    customeremail = ''
    customermobile = ''
    companyname = ''
    companyaddress = ''
    companystate = ''
    companycity = ''
    companypincode = ''
    if request.user.is_authenticated:
        if request.method == "POST":
            custid=request.POST.get('custid')
            print(custid)
            request.session['custid'] = custid
            
            # print("data is :",request.session['custid'])
            customername = request.POST.get('customername')
            customeremail = request.POST.get('customeremail')
            customermobile = request.POST.get('customermobile')
            companyname = request.POST.get('companyname')
            companyaddress = request.POST.get('companyaddress')
            companystate = request.POST.get('state')
            companycity = request.POST.get('companycity')
            companypincode = request.POST.get('companypincode')
            
                    
                    
                    
                
            if custid:
                custdata = CustomerDetail.objects.get(id=custid)
                obj = {
                    "custname":custdata.customerName,
                    "custmobile":custdata.customerMobile,
                    "custemail":custdata.customerEmail,
                    "custCompanyName":custdata.customerCompanyName,
                    "custCompanyAddress":custdata.customerCompanyAddress,
                    "custCompanyCiy":custdata.customerCompanyCity,
                    "custCompanyState":custdata.customerCompanyState,
                    'custCompanyPincode':custdata.customerCompanyPincode
                }
                return JsonResponse({"custdata":obj})
        user_id = request.user.id
        user_name = request.user.first_name
        abcd = User.objects.get(id=user_id)
        if abcd.is_superuser == True:
            level = 5
            a = "yes"
        else:
            level = ""
            a="no"
   
    if a=="yes":
        cust = CustomerDetail.objects.all()
    if 'custid' in request.session:
        sessdata = request.session['custid']
        print(sessdata)
    if customername or customeremail or customermobile or companyname or companyaddress or companystate or companycity or companypincode:
        custdata = CustomerDetail.objects.get(id=sessdata)
        if customername:
            custdata.customerName=customername
            custdata.save()                     
        if customeremail:
            custdata.customerEmail=customeremail
            custdata.save()                   
        if customermobile:
            custdata.customerMobile=customermobile
            custdata.save()                      
        if companyname:
            custdata.customerCompanyName=companyname
            custdata.save()
        if companyaddress:
            custdata.customerCompanyAddress=companyaddress
            custdata.save()
        if companystate:
            custdata.customerCompanyState=companystate
            custdata.save()
        if companycity:
            custdata.customerCompanyCity=companycity
            custdata.save()
        if companypincode:
            custdata.customerCompanyPincode=companypincode
            custdata.save()
    params={
        "data":a,
        'cust':cust
    }
    return render(request,"customerdetails.html",params)


def adduser(request):
    passok=""
    upper = ""
    lower = ""
    mt8 = ""
    digit = ""
    data = ""
    user_match = ""
    if request.user.is_superuser:
        user_id = request.user.id
        
        lvl = 5
        if lvl == 5:
            data = "yes"
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
                        print("not admin")
                        pswd = len(addpassword)
                        print("is upper ?",addpassword.isupper())
                        print("islower ? :",addpassword.islower())
                        for i in addpassword:
                            if i.isupper():
                                upper = True
                            
                        for i in addpassword:
                            if i.islower():
                                lower = True
                            
                        if pswd >= 8:
                            mt8 = True
                            print("password ok") 
                            
                        else:
                            
                            mt8 = False
                        for i in addpassword:
                            if i.isdigit():
                                digit = True
                        
                        print("upper :",upper)
                        print("lower :",lower)
                        print("more than 8",mt8)
                        print("has digits :",digit)
                        if upper == True and lower == True and mt8 == True and digit == True:
                            print("validation Successfull")
                            passok = "yes"
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
                                    
                                
                        else:
                            print("validation Failed")
                            passok = "no"
                    
                
                            
        else:
            data = "no"
                
    params = {
        "data":data,
        "passok":passok,
        "user_match":user_match
    }
            
    return render(request,"adduser.html",params)

def add_data(request):
    data=""
    if request.user.is_superuser:
        user_id = request.user.id
        lvl = 5
        if lvl == 5:
            data = "yes"
            if request.method == "POST":
                addlientname = request.POST.get('addlientname')
                addmoc = request.POST.get('addmoc')
                addtooltype = request.POST.get('addtooltype')
                addshape = request.POST.get('addshape')
                addtabletsize = request.POST.get('addtabletsize')
                addu1 = request.POST.get('addu1')
                addu2 = request.POST.get('addu2')
                addl1 = request.POST.get('addl1')
                addl2 = request.POST.get('addl2')
                addd = request.POST.get('addd')
                addset = request.POST.get('addset')
                addplatingtype = request.POST.get('addplatingtype')
                addrawmaterial = request.POST.get('addrawmaterial')

                addpunchblank = request.POST.get('addpunchblank')
                adddieblank = request.POST.get('adddieblank')


                addblank = request.POST.get('addblank')
                addprocess = request.POST.get('addprocess')
                addbodytipping = request.POST.get('addbodytipping')
                addheadmachining = request.POST.get('addheadmachining')
                addkeyway = request.POST.get('addkeyway')
                addht = request.POST.get('addht')
                addgrinding = request.POST.get('addgrinding')
                addhardchrome = request.POST.get('addhardchrome')
                addqualitycheck = request.POST.get('addqualitycheck')
                addpackaging = request.POST.get('addpackaging')
                
                adddispachmode = request.POST.get('adddispachmode')
                if addlientname or addmoc or addtooltype or addshape or addtabletsize or addu1 or addu2 or addl1 or addl2 or addd or addset or addplatingtype or addrawmaterial:
                    if addlientname:
                        adddata = CustomerDetail(customerCompanyName = addlientname)
                        adddata.save()
                    if addmoc:
                        adddata = AutoAddMain(moc = addmoc)
                        adddata.save()
                    if addtooltype:
                        adddata = AutoAddMain(toolType = addtooltype)
                        adddata.save()
                    if addshape:
                        adddata = AutoAddMain(shape = addshape)
                        adddata.save()
                    if addtabletsize:
                        adddata = AutoAddMain(tabletSize = addtabletsize)
                        adddata.save()
                    if addu1:
                        adddata = AutoAddMain(u1 = addu1)
                        adddata.save()
                    if addu2:
                        adddata = AutoAddMain(u2 = addu2)
                        adddata.save()
                    if addl1:
                        adddata = AutoAddMain(l1 = addl1)
                        adddata.save()
                    if addl2:
                        adddata = AutoAddMain(l2 = addl2)
                        adddata.save()
                    if addd:
                        adddata = AutoAddMain(d = addd)
                        adddata.save()
                    if addset:
                        adddata = AutoAddMain(sett = addset)
                        adddata.save()
                    if addplatingtype:
                        adddata = AutoAddMain(platingType = addplatingtype)
                        adddata.save()
                    if addrawmaterial:
                        adddata = AutoAddMain(rawMaterial = addrawmaterial)
                        adddata.save()
                    
                if addpunchblank or adddieblank:
                    if addpunchblank:
                        adddata = AutoAddPlanning(punchBlankUsed = addpunchblank)
                        adddata.save()
                    if adddieblank:
                        adddata = AutoAddPlanning(dieBlankUsed = adddieblank)
                        adddata.save()
                if addblank or  addprocess or addbodytipping or addheadmachining or addkeyway or addkeyway or addht or addgrinding or addhardchrome or addqualitycheck or addpackaging:
                    if addblank:
                        adddata = AutoAddManufacturing(blank = addblank)
                        adddata.save()
                    if addprocess:
                        adddata = AutoAddManufacturing(process = addprocess)
                        adddata.save()
                    if addbodytipping:
                        adddata = AutoAddManufacturing(bodyTipMachining = addbodytipping)
                        adddata.save()
                    if addheadmachining:
                        adddata = AutoAddManufacturing(headMachining = addheadmachining)
                        adddata.save()
                    if addkeyway:
                        adddata = AutoAddManufacturing(keywayTaperFinish = addkeyway)
                        adddata.save()
                    if addht:
                        adddata = AutoAddManufacturing(ht = addht)
                        adddata.save()
                    if addgrinding:
                        adddata = AutoAddManufacturing(grinding = addgrinding)
                        adddata.save()
                    if addhardchrome:
                        adddata = AutoAddManufacturing(hardChrome = addhardchrome)
                        adddata.save()
                    if addqualitycheck:
                        adddata = AutoAddManufacturing(qualityCheck = addqualitycheck)
                        adddata.save()
                    if addpackaging:
                        adddata = AutoAddManufacturing(packingDispach = addpackaging)
                        adddata.save()

                if adddispachmode:
                    adddata = AutoAddDispatch(dispachMode=adddispachmode)
                    adddata.save()
        else:
            data = "no"
                
    params = {
        "data":data
    }
            
    return render(request,"admin_adddata.html",params)
    
def delete_data(request):
    data=""
    tabledata = []
    if request.user.is_superuser:
        if request.method == "POST":
            deleteform = request.POST.get('deleteform')
        else:
            deleteform = ""   
        user_id = request.user.id
        user_name=request.user.first_name
        lvl = 5
        if lvl == 5:
            data = "yes"
            form = ProductionData.objects.all()
            for x in form:
                data_id= x.id
                data_orderdate1  = x.orderDate
                data_orderdate = datetime.datetime.strptime(data_orderdate1, "%Y-%m-%d").strftime("%d-%m-%Y")
                data_ordernumber    = x.orderNumber
                data_clientname =x.clientName
                data_value =x.value
                data_moc = x.moc
                data_tooltype =x.toolType
                data_shape =x.shape
                data_tabletsize =x.tabletSize
                data_u1 =x.u1
                data_u2 =x.u2
                data_l1 =x.l1
                data_l2 =x.l2
                data_d =x.d
                data_set =x.sett
                data_platingtype =x.platingType
                data_rawmaterial =x.rawMaterial
                data_priority =x.priority
                data_dwgNumber = x.dwgNumber
                data_drgDate = x.drgDate
                data_approvalDate = x.approvalDate
                data_master = x.master
                data_masterOut = x.masterOut
                data_masterIn = x.masterIn
                if data_u1 and data_u2:
                    data_punchBlankUsed = int(data_u1)+ int(data_l1)
                else:
                    data_punchBlankUsed =0
                # print(data_punchBlankUsed)
                data_dieBlankUsed = data_d
                data_hitDate = x.hitDate
                data_estimatedDelivery = x.estimatedDelivery
                data_planningOut=x.planningOut
                data_planningIn=x.planningIn
                data_blank=x.blank
                data_process=x.process
                data_bodyTipMachining=x.bodyTipMachining
                data_headMachining=x.headMachining
                data_keywayTaperFinish=x.keywayTaperFinish
                data_ht=x.ht
                data_grinding=x.grinding
                data_hardChrome=x.hardChrome
                data_qualityCheck=x.qualityCheck
                data_packingDispach=x.packingDispach
                data_estimatedDelivery=x.estimatedDelivery
                data_actualDelivery=x.actualDelivery
                data_dispachMode=x.dispachMode
                data_couriesNumber=x.couriesNumber
                data_remark=x.remark
                data1 = x.blank
                data2 = x.process
                data3 = x.bodyTipMachining
                data4 = x.headMachining
                data5 = x.keywayTaperFinish
                data6 = x.ht
                data7 = x.grinding
                data8 = x.hardChrome
                data9 = x.qualityCheck
                data10 = x.packingDispach
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
                # print(totaldata%2)
                data_status = str(totaldata) + str("%")

                # print("status is :",data_id,data_status)
                if data_orderdate or data_ordernumber or data_clientname or data_value or data_moc or data_tooltype or data_shape or data_tabletsize or data_u1 or data_u2 or data_l1 or data_l2 or data_d or data_set or data_platingtype or data_rawmaterial or data_priority or data_status:
                    obj = {
                        "id":data_id,
                        "orderdate" : data_orderdate,
                        "ordernumber" :data_ordernumber,
                        "clientname" :data_clientname,
                        "value" :data_value,
                        "moc" :data_moc,
                        "tooltype" :data_tooltype,
                        "shape" :data_shape,
                        "tabletsize" :data_tabletsize,
                        "u1" :data_u1,
                        "u2" :data_u2,
                        "l1" :data_l1,
                        "l2" :data_l2,
                        "d" :data_d,
                        "set" :data_set,
                        "platingtype" :data_platingtype,
                        "rawmaterial" :data_rawmaterial,
                        "priority" :data_priority,
                        "status" :data_status,
                        "dwgNumber" :  data_dwgNumber,
                        "drgDate" :  data_drgDate,
                        "approvalDate" :  data_approvalDate,
                        "master" :  data_master,
                        "masterOut" :  data_masterOut,
                        "masterIn" :  data_masterIn,
                        "punchBlankUsed" :  data_punchBlankUsed,
                        "dieBlankUsed" :  data_dieBlankUsed,
                        "hitDate" :  data_hitDate,
                        "estimatedDelivery" :  data_estimatedDelivery,
                        "planningOut": data_planningOut,
                        "planningIn": data_planningIn,
                        "blank": data_blank,
                        "process": data_process,
                        "bodyTipMachining": data_bodyTipMachining,
                        "headMachining": data_headMachining,
                        "keywayTaperFinish": data_keywayTaperFinish,
                        "ht": data_ht,
                        "grinding": data_grinding,
                        "hardChrome": data_hardChrome,
                        "qualityCheck": data_qualityCheck,
                        "packingDispach": data_packingDispach,
                        "estimatedDelivery": data_estimatedDelivery,
                        "actualDelivery": data_actualDelivery,
                        "dispachMode": data_dispachMode,
                        "couriesNumber": data_couriesNumber,
                        "remark": data_remark

                    }
                    tabledata.append(obj)
        if deleteform:
            deletedata = ProductionData.objects.get(id = deleteform)
            if deletedata:
                deletedata.delete()
                type="Deleted"
                log = UserLog(formid=deleteform,user_id=user_id,user_name=user_name,Type=type)
                log.save()
                return redirect('admindelete')
    params = {
        "data":data,
        "tabledata":tabledata
    }
    return render(request,"admindeleteform.html",params)




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


