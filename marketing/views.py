from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect , HttpResponseRedirect
from die_punch.models import *
from die_punch.serializers import *
from .serializers import *
from django.db.models import Q
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
import datetime
from .models import *
# Create your views here.

def GetPermission(user):
    permission_list = user.permissions
    permission = permission_list.split(',')
    # print(permission)
    perms = []
    if "1" in permission:
        perms.append("die_punch")
    if "2" in permission:
        perms.append("marketing")
    return perms

@login_required
def Marketing_Dashboard(request):
    if request.user.is_user_role_1:
        # form = MarketingForm.objects.get(id = 1)
        # form.status = 1
        # form.save()
    
        # client_details = ClientDetails.objects.get(id=2)
        # client_details.enquiry_of = "Suma Press & Series 7 + Multi Tips Die Punches"
        # client_details.save()
        params = {
            "permissions":GetPermission(request.user),
            "forms":MarketingForm.objects.all(),
            "all_clients":CustomerDetail.objects.all()
        }
    return render(request, 'user1/marketing_dashboard.html',params)


@login_required
def CreateMarketingForm(request):
    if request.user.is_user_role_1:
        params = {
            "permissions":GetPermission(request.user),
            "all_clients":CustomerDetail.objects.all()
        }
    return render(request, 'user1/add_marketingform.html',params)

def add_marketing_form_user_1(request):
    if request.user.is_user_role_1:
        if request.method == 'POST':
            client_name = request.POST.get('client_name')
            enquiry_of = request.POST.get('enquiry_of')
            contact_number = request.POST.get('contact_number')
            contact_person = request.POST.get('contact_person')
            designation = request.POST.get('designation')
            email = request.POST.get('email')
            address = request.POST.get('address')
            place = request.POST.get('place')
            state = request.POST.get('state')
            enquiry_date = request.POST.get('enquiry_date')
            month = request.POST.get('month')
            enquiry_received_by = request.POST.get('enquiry_received_by')
            enquiry_mode = request.POST.get('enquiry_mode')
            quotation_ref_no = request.POST.get('quotation_ref_no')
            quotation_given_by = request.POST.get('quotation_given_by')
            date = request.POST.get('date')
            quotation_mode = request.POST.get('quotation_mode')
            quotation_remark = request.POST.get('quotation_remark')
            next_follow_up_date = request.POST.get('next_follow_up_date')
            done_by = request.POST.get('done_by')
            status = request.POST.get('status')

            #  po_number =po_number ,
            #     po_date =po_date ,
            #     po_received_on =po_received_on ,
            #     po_mode =po_mode ,
            #     po_amount =po_amount ,
            #     po_others =po_others ,
            #     po_tax =po_tax ,
            #     po_total_amount =po_total_amount ,
            #     po_amount_recieved =po_amount_recieved ,
            #     po_balance_amount =po_balance_amount ,
            #     po_payment_terms =po_payment_terms ,
            #     po_payment_recieved_on =po_payment_recieved_on ,
            #     po_payment_details =po_payment_details ,
            #     po_payment_details_mode =po_payment_details_mode ,
            #     po_account =po_account ,
            #     po_material_to_be_dispatched_by =po_material_to_be_dispatched_by ,
            #     po_bill_no =po_bill_no ,
            #     po_bill_date=po_bill_date,
            # po_number = request.POST.get('po_number')
            # po_date = request.POST.get('po_date')
            # po_received_on = request.POST.get('po_received_on')
            # po_mode = request.POST.get('po_mode')
            # po_amount = request.POST.get('po_amount')
            # po_others = request.POST.get('po_others')
            # po_tax = request.POST.get('po_tax')
            # po_total_amount = request.POST.get('po_total_amount')
            # po_amount_recieved = request.POST.get('po_amount_recieved')
            # po_balance_amount = request.POST.get('po_balance_amount')
            # po_payment_terms = request.POST.get('po_payment_terms')
            # po_payment_recieved_on = request.POST.get('po_payment_recieved_on')
            # po_payment_details = request.POST.get('po_payment_details')
            # po_payment_details_mode = request.POST.get('po_payment_details_mode')
            # po_account = request.POST.get('po_account')
            # po_material_to_be_dispatched_by = request.POST.get('po_material_to_be_dispatched_by')
            # po_bill_no = request.POST.get('po_bill_no')
            # po_bill_date = request.POST.get('po_bill_date')

            # contact_number =contact_number ,
            # contact_person =contact_person ,
            # designation =designation ,
            # email =email ,
            # address =address ,
            # place =place ,
            # state =state ,
            create_client_details = ClientDetails(
                client=CustomerDetail.objects.get(id=client_name),
                enquiry_of = enquiry_of,
                contact_no =contact_number ,
                contact_person =contact_person ,
                designtion =designation ,
                email =email ,
                address =address ,
                place =place ,
                state =state ,
            )
            create_client_details.save()

            latest_client_details = ClientDetails.objects.get(Q(client=CustomerDetail.objects.get(id=client_name)) & Q(contact_no = contact_number) & Q(email=email))

            create_marketing_form = MarketingForm(
                client=CustomerDetail.objects.get(id=client_name),
                client_details=latest_client_details,
                enquiry_date =enquiry_date ,
                month =month ,
                enquiry_received_by =enquiry_received_by ,
                enquiry_mode =enquiry_mode ,
                quotation_ref_no =quotation_ref_no ,
                quotation_given_by =quotation_given_by ,
                date =date ,
                quotation_mode =quotation_mode ,
                quotation_remark =quotation_remark ,
                next_follow_up_date =next_follow_up_date ,
                done_by =done_by ,
                status =status ,
               
                created_by=request.user.id
            )
            create_marketing_form.save()
        params = {
            "permissions":GetPermission(request.user),
            "all_clients":CustomerDetail.objects.all()
        }
    return HttpResponseRedirect('/marketing/dashboard',params)

def update_marketing_form_user_1(request):
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        if form_id:
            try:
                get_marketing_form = MarketingForm.objects.get(id=form_id)
                clientdetails = ClientDetails.objects.get(id = get_marketing_form.client_details.id)
                print("Client Details :",clientdetails)
                print("Form Found :",get_marketing_form)
                get_marketing_data = MarketingFormSerializer(get_marketing_form,many=False)
                get_client_data = ClientDetailsSerializer(clientdetails,many=False)
                return JsonResponse({'data':get_marketing_data.data,'client':get_client_data.data})
            except MarketingForm.DoesNotExist:
                print("no form found")
        

        marketing_form = request.POST.get('marketing_form')
        client_name = request.POST.get('client_name')
        enquiry_of = request.POST.get('enquiry_of')
        contact_number = request.POST.get('contact_number')
        contact_person = request.POST.get('contact_person')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        address = request.POST.get('address')
        place = request.POST.get('place')
        state = request.POST.get('state')
        enquiry_date = request.POST.get('enquiry_date')
        month = request.POST.get('month')
        enquiry_received_by = request.POST.get('enquiry_received_by')
        enquiry_mode = request.POST.get('enquiry_mode')
        quotation_ref_no = request.POST.get('quotation_ref_no')
        quotation_given_by = request.POST.get('quotation_given_by')
        date = request.POST.get('date')
        quotation_mode = request.POST.get('quotation_mode')
        quotation_remark = request.POST.get('quotation_remark')
        next_follow_up_date = request.POST.get('next_follow_up_date')
        done_by = request.POST.get('done_by')
        status = request.POST.get('status')
        
