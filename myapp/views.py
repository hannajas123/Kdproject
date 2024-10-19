from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,'Login.html')
def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    res=Login.objects.filter(username=username,password=password)
    if res.exists():
        res=Login.objects.get(username=username,password=password)
        request.session['lid']=res.id
        if res.type == 'admin':
         return HttpResponse('''<script>alert('Login Successfully');window.location='/myapp/admin_home/'</script>''')
        elif res.type == 'kdunit':
         return HttpResponse('''<script>alert('Login Successfully');window.location='/myapp/kd_Home/'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid Password or user');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse(
            '''<script>alert('User not Found');window.location='/myapp/login/'</script>''')
def logout(request):
    request.session['lid'] = ''
    return HttpResponse('''<script>alert('Logout');window.location='/myapp/login/'</script>''')

def admin_home(request):
    return render(request,'admin/adminindex.html')
def Add_kdunit(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
     return render(request,'admin/Add kdUnit.html')
def Addkunit_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        name=request.POST['textfield']
        unitno=request.POST['textfield3']
        place=request.POST['textfield4']
        ward=request.POST['textfield5']
        pnchyth=request.POST['textfield6']
        district=request.POST['textfield7']
        email=request.POST['textfield8']
        phone=request.POST['textfield9']
        oo=Login()
        oo.username=email
        oo.password=phone
        oo.type='kdunit'
        oo.save()
        obj=K_dunit()
        obj.name=name
        obj.unit_no=unitno
        obj.place=place
        obj.panchayath=pnchyth
        obj.ward=ward
        obj.district=district
        obj.Email=email
        obj.phone=phone
        obj.LOGIN_id=oo.id
        obj.save()
        return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/Add_kdunit/'</script>''')
def View_kdunit(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=K_dunit.objects.all()
        return render(request,'admin/View kdunit.html',{'data':res})
def vkunit_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        srch=request.POST['textfield']
        res=K_dunit.objects.filter(name__icontains=srch)
        return render(request,'admin/View kdunit.html',{'data':res})
def Edit_kdunit(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=K_dunit.objects.get(id=id)
        return render(request,'admin/Edit kdUnit.html',{'data':res})
def editkdunit_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        name = request.POST['textfield']
        unitno = request.POST['textfield3']
        place = request.POST['textfield4']
        ward = request.POST['textfield5']
        pnchyth = request.POST['textfield6']
        district = request.POST['textfield6']
        id = request.POST['id1']

        obj = K_dunit.objects.get(id=id)
        obj.name = name
        obj.unit_no = unitno
        obj.place = place
        obj.panchayath = pnchyth
        obj.ward = ward
        obj.district = district
        obj.LOGIN_id = request.session['lid']
        obj.save()
        return HttpResponse('''<script>alert('Updated Successfully');window.location='/myapp/View_kdunit/'</script>''')
def delete_kdunit(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=K_dunit.objects.filter(id=id).delete()
        return HttpResponse('''<script>alert('Deleted ');window.location='/myapp/View_kdunit/'</script>''')

def Add_meeting(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=K_dunit.objects.get(id=id)
        return render(request,'admin/Add meeting.html',{'id':res.id})
def addmeeting_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        date=request.POST['textfield']
        time=request.POST['textfield2']
        purpose=request.POST['textarea']
        did=request.POST['id1']
        obj=Meetig()
        obj.date=date
        obj.time=time
        obj.purpose=purpose
        obj.KDUNIT_id=did
        obj.save()
        return HttpResponse('''<script>alert('Added ');window.location='/myapp/View_kdunit/'</script>''')
def View_meeting(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Meetig.objects.all()
        return render(request,'admin/View Meeting.html',{'data':res})
def viewmeeting_post(request):
    return HttpResponse("ok")
def Edit_meeting(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res = Meetig.objects.get(id=id)
        return render(request,'admin/Edit meeting.html',{'data':res})
def editmeting_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        date = request.POST['textfield']
        time = request.POST['textfield2']
        purpose = request.POST['textarea']
        did = request.POST['id1']
        obj = Meetig.objects.get(id=did)
        obj.date = date
        obj.time = time
        obj.purpose = purpose
        # obj.KDUNIT_id = did
        obj.save()
        return HttpResponse('''<script>alert('Added ');window.location='/myapp/View_kdunit/'</script>''')
def delete_meeting(request,id):
    res = Meetig.objects.filter(id=id).delete()

    return HttpResponse('''<script>alert('Deleted ');window.location='/myapp/View_kdunit/'</script>''')

def Add_notification(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        return render(request,'admin/Add notification.html')
def addnotification_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        from datetime import date
        date=date.today()
        noti=request.POST['textarea']
        obj=Notification()
        obj.date=date
        obj.notification=noti
        obj.save()
        return HttpResponse('''<script>alert('Added ');window.location='/myapp/Add_notification/'</script>''')
def View_notification(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Notification.objects.all()
        return render(request,'admin/View Notification.html',{'data':res})
def viewnotification_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        frm=request.POST['textfield']
        to=request.POST['textfield1']
        res=Notification.objects.filter(date__range=[frm,to])
        return render(request,'admin/View Notification.html',{'data':res})
def Edit_notification(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Notification.objects.get(id=id)
        return render(request,'admin/Edit notification.html',{'data':res})
def Delete_notification(request,id):
    res=Notification.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('Updated ');window.location='/myapp/View_notification/'</script>''')
def editnotification_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        from datetime import date
        date = date.today()
        noti = request.POST['textarea']
        did = request.POST['id1']
        obj = Notification.objects.get(id=did)
        obj.date = date
        obj.notification = noti
        obj.save()
        return HttpResponse('''<script>alert('Updated ');window.location='/myapp/View_notification/'</script>''')
def Change_paassword(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        return render(request,'admin/Change password.html')
def changepassword_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        curpassword=request.POST['textfield']
        newpswd=request.POST['textfield2']
        cnfmpswd=request.POST['textfield3']
        if newpswd == cnfmpswd:
            res=Login.objects.filter(id=request.session['lid'],password=curpassword)
            if res.exists():
                res=Login.objects.filter(id=request.session['lid']).update(password=newpswd)
                return HttpResponse('''<script>alert('changed pasword');window.location='/myapp/login/'</script>''')
            else:
                return HttpResponse('''<script>alert('Invalid pasword');window.location='/myapp/Change_paassword/'</script>''')
        else:
            return HttpResponse('''<script>alert('New password and confirm password not same');window.location='/myapp/Change_paassword/'</script>''')


def View_events(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Events.objects.all()
        return render(request,'admin/View events.html',{'data':res})
def viewevents_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        frm=request.POST['textfield']
        to=request.POST['textfield1']
        res=Events.objects.filter(date__range=[frm,to])
        return render(request,'admin/View events.html',{'data':res})
def View_feedback(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Feedback.objects.all()
        return render(request,'admin/View Feedback.html',{'data':res})
def viewfeedback_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        frm = request.POST['textfield']
        to = request.POST['textfield1']
        res = Feedback.objects.filter(date__range=[frm, to])
        return render(request,'admin/View Feedback.html',{'data':res})
def View_kdmembers(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        print(id)
        res=K_dmembers.objects.filter(KDUNIT_id=id)
        return render(request,'admin/View kdMembers.html',{'data':res,'id':id})
def viewkdmembers_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        id=request.POST['id1']
        print(id)
        srch=request.POST['textfield']
        res = K_dmembers.objects.filter(KDUNIT_id=id,name__icontains=srch)
        return render(request, 'admin/View kdMembers.html', {'data': res,'id':id})




def View_users(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=User.objects.all()
        return render(request,'admin/View User.html',{'data':res})
def viewusers_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        srch=request.POST['textfield']
        res=User.objects.filter(name__icontains=srch)
        return render(request,'admin/View User.html',{'data':res})
def View_kuris_nd_payment(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Payment.objects.all()
        return render(request,'admin/view payments and kuris.html',{'data':res})
def View_kuris_nd_payment_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        frm = request.POST['textfield']
        to = request.POST['textfield1']
        res=Payment.objects.filter(date__range=[frm,to])
        return render(request,'admin/view payments and kuris.html',{'data':res})

############################################kdunit###################3

def kd_View_profile(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=K_dunit.objects.get(LOGIN_id=request.session['lid'])
        return render(request, 'Kdunit/View Profile.html',{'data':res})


def kd_Home(request):
    return render(request, 'Kdunit/kdunitindex.html')


def kd_Add_member(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        return render(request, 'Kdunit/Add kdmembers.html')
def kd_Add_member_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        name=request.POST['textfield']
        email=request.POST['textfield2']
        phone=request.POST['textfield3']
        place=request.POST['textfield4']
        ward=request.POST['textfield5']
        panchayath=request.POST['textfield6']
        district=request.POST['textfield7']
        oo=Login()
        oo.username=email
        oo.password=phone
        oo.type='kdmember'
        oo.save()
        obj=K_dmembers()
        obj.name=name
        obj.phone=phone
        obj.Email=email
        obj.place=place
        obj.panchayath=panchayath
        obj.ward=ward
        obj.district=district
        obj.LOGIN_id=oo.id
        obj.KDUNIT_id=K_dunit.objects.get(LOGIN_id=request.session['lid'])
        obj.save()
        return HttpResponse('''<script>alert(' Added Successfully');window.location='/myapp/kd_Add_member/'</script>''')


def kd_View_member(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=K_dmembers.objects.filter(KDUNIT__LOGIN_id=request.session['lid'])
        return render(request, 'Kdunit/View kdMembers.html',{'data':res})
def kd_View_member_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        srch=request.POST['textfield']
        res = K_dmembers.objects.filter(KDUNIT__LOGIN_id=request.session['lid'],name__icontains=srch)
        return render(request, 'Kdunit/View kdMembers.html', {'data': res})
def kd_Edit_member(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=K_dmembers.objects.get(id=id)
        return render(request, 'Kdunit/Edit kdmembers.html',{'data':res})
def kd_Edit_member_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        name = request.POST['textfield']
        email = request.POST['textfield2']
        phone = request.POST['textfield3']
        place = request.POST['textfield4']
        ward = request.POST['textfield5']
        panchayath = request.POST['textfield6']
        district = request.POST['textfield7']
        did=request.POST['id1']
        obj = K_dmembers.objects.get(id=did)
        obj.name = name
        obj.phone = phone
        obj.Email = email
        obj.place = place
        obj.panchayath = panchayath
        obj.ward = ward
        obj.district = district
        obj.KDUNIT_id = K_dunit.objects.get(LOGIN_id=request.session['lid'])
        obj.save()
        return HttpResponse('''<script>alert(' Updated Successfully');window.location='/myapp/kd_View_member/'</script>''')


def kd_delete_members(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=K_dmembers.objects.filter(id=id).delete()
        return HttpResponse('''<script>alert(' Deleted ');window.location='/myapp/kd_View_member/'</script>''')

def kd_Add_events(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        return render(request, 'Kdunit/Add Events.html')
def kd_Add_events_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        date=request.POST['textfield']
        time=request.POST['textfield2']
        title=request.POST['textfield3']
        theme=request.POST['textfield4']
        obj=Events()
        obj.date=date
        obj.time=time
        obj.title=title
        obj.theme=theme
        obj.KDUNIT=K_dunit.objects.get(LOGIN_id=request.session['lid'])
        obj.save()
        return HttpResponse('''<script>alert(' Added Successfully');window.location='/myapp/kd_Add_events/'</script>''')
def kd_View_events(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Events.objects.filter(KDUNIT__LOGIN_id=request.session['lid'])
        return render(request, 'Kdunit/View events.html',{'data':res})
def kd_View_events_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        fromd=request.POST['textfield']
        tod=request.POST['textfield1']
        res = Events.objects.filter(KDUNIT__LOGIN_id=request.session['lid'],date__range=[fromd,tod])
        return render(request, 'Kdunit/View events.html', {'data': res})
def kd_Edit_events(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Events.objects.get(id=id)
        return render(request, 'Kdunit/Edit Events.html', {'data': res})
def kd_Edit_events_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        id=request.POST['id1']
        date=request.POST['textfield']
        time=request.POST['textfield2']
        title=request.POST['textfield3']
        theme=request.POST['textfield4']
        obj=Events.objects.get(id=id)
        obj.date=date
        obj.time=time
        obj.title=title
        obj.theme=theme
        # obj.KDUNIT_id=K_dunit.objects.get(LOGIN_id=request.session['lid'])
        obj.save()
        return HttpResponse('''<script>alert(' Updated Successfully');window.location='/myapp/kd_View_events/'</script>''')
def kd_delete_events_post(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Events.objects.filter(id=id).delete()
        return HttpResponse('''<script>alert(' Deleted');window.location='/myapp/kd_View_events/'</script>''')

def kd_view_notification_nd_forward(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Notification.objects.all()
        return render(request, 'Kdunit/View Notification.html',{'data':res})
def frwd_noti(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Notification.objects.filter(id=id).update(status='forwarded')
        return HttpResponse('''<script>alert(' Forwarded' );window.location='/myapp/kd_view_notification_nd_forward/'</script>''')

def kd_view_notification_nd_forward_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        frmd=request.POST['textfield']
        tod=request.POST['textfield1']
        res = Notification.objects.filter(date__range=[frmd,tod])
        return render(request, 'Kdunit/View Notification.html', {'data': res})

def kd_Change_password(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        return render(request, 'Kdunit/Change password.html')
def kd_Change_password_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        curntpswd=request.POST['textfield']
        npswd=request.POST['textfield2']
        cnfmpswd=request.POST['textfield3']
        obj=Login.objects.filter(id=request.session['lid'],password=curntpswd)
        if obj.exists():
            obj = Login.objects.get(id=request.session['lid'], password=curntpswd)
            obj.password=cnfmpswd
            obj.save()
            return HttpResponse('''<script>alert(' Password Changed Successfully');window.location='/myapp/login/'</script>''')

        else:
           return HttpResponse('''<script>alert('Invalid  Password ');window.location='/myapp/kd_Change_password/'</script>''')


def kd_Add_member_meeting(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        return render(request, 'Kdunit/Add meeting.html')
def kd_Add_member_meeting_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        date=request.POST['textfield']
        time=request.POST['textfield2']
        purpose=request.POST['textarea']
        obj=KdMembersMeetig()
        obj.date=date
        obj.time=time
        obj.purpose=purpose
        obj.KDUNIT=K_dunit.objects.get(LOGIN_id=request.session['lid'])
        obj.save()
        return HttpResponse('''<script>alert(' Added Successfully');window.location='/myapp/kd_Add_member_meeting/'</script>''')


def kd_View_member_meeting(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=KdMembersMeetig.objects.filter(KDUNIT__LOGIN_id=request.session['lid'])
        return render(request, 'Kdunit/View Meeting.html',{'data':res})
def kd_View_member_meeting_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        fdate=request.POST['textfield']
        tdate=request.POST['textfield1']
        res = KdMembersMeetig.objects.filter(KDUNIT__LOGIN_id=request.session['lid'],date__range=[fdate,tdate])
        return render(request, 'Kdunit/View Meeting.html', {'data': res})
def kd_Edit_member_meeting(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=KdMembersMeetig.objects.get(id=id)
        return render(request, 'Kdunit/Edit meeting.html', {'data': res})
def kd_Edit_member_meeting_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        date = request.POST['textfield']
        time = request.POST['textfield2']
        purpose = request.POST['textarea']
        id=request.POST['id1']
        obj = KdMembersMeetig.objects.get(id=id)
        obj.date = date
        obj.time = time
        obj.purpose = purpose
        # obj.KDUNIT = K_dunit.objects.get(LOGIN_id=request.session['lid'])
        obj.save()
        return HttpResponse(
            '''<script>alert(' Updated Successfully');window.location='/myapp/kd_View_member_meeting/'</script>''')
def kd_delete_member_meeting_post(request,id):
    res=KdMembersMeetig.objects.filter(id=id).delete()

    return HttpResponse(
        '''<script>alert(' Deleted ');window.location='/myapp/kd_View_member_meeting/'</script>''')
def kd_Add_kuries(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        return render(request, 'Kdunit/Add kuris.html')
def kd_Add_kuries_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        name=request.POST['textfield']
        totalAmount=request.POST['textfield2']
        totalinslmt=request.POST['textfield3']
        sdate=request.POST['textfield4']
        cdate=request.POST['textfield5']
        obj=Kuris()
        obj.name=name
        obj.totalAmount=totalAmount
        obj.totalinstallments=totalinslmt
        obj.startingDate=sdate
        obj.EndingDate=cdate
        obj.KDUNIT=K_dunit.objects.get(LOGIN_id=request.session['lid'])
        obj.save()
        return HttpResponse('''<script>alert(' Added Successfully');window.location='/myapp/kd_Add_kuries/'</script>''')
def kd_View_kuries(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Kuris.objects.filter(KDUNIT__LOGIN_id=request.session['lid'])
        return render(request, 'Kdunit/view kuris.html',{'data':res})
def kd_View_kuries_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        srch=request.POST['textfield']
        res = Kuris.objects.filter(KDUNIT__LOGIN_id=request.session['lid'],name__icontains=srch)
        return render(request, 'Kdunit/view kuris.html', {'data': res})
def kd_Edit_kuries(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Kuris.objects.get(id=id)

        return render(request, 'Kdunit/Edit kuris.html',{'data':res})
def kd_Edit_kuries_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        id=request.POST['id1']
        name = request.POST['textfield']
        totalAmount = request.POST['textfield2']
        totalinslmt = request.POST['textfield3']
        sdate = request.POST['textfield4']
        cdate = request.POST['textfield5']
        obj = Kuris.objects.get(id=id)
        obj.name = name
        obj.totalAmount = totalAmount
        obj.totalinstallments = totalinslmt
        obj.startingDate = sdate
        obj.EndingDate = cdate
        # obj.KDUNIT = K_dunit.objects.get(LOGIN_id=request.session['lid'])
        obj.save()
        return HttpResponse('''<script>alert(' Updated Successfully');window.location='/myapp/kd_View_kuries/'</script>''')
def kd_delete_kuries_post(request,id):
    res=Kuris.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert(' Deleted ');window.location='/myapp/kd_View_kuries/'</script>''')

def kd_Add_Product(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        return render(request, 'Kdunit/Add Product.html')
def kd_Add_Product_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        name=request.POST['textfield']
        quantity=request.POST['textfield3']
        price=request.POST['textfield4']
        details=request.POST['textfield5']
        photo=request.FILES['textfield6']
        fs = FileSystemStorage()
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + '.jpg'
        fn = fs.save(date, photo)
        quanlity=request.POST['textfield7']
        obj=Product()
        obj.quantity=quantity
        obj.quality=quanlity
        obj.name=name
        obj.datails=details
        obj.price=price
        obj.photo=fs.url(date)
        obj.KDUNIT=K_dunit.objects.get(LOGIN_id=request.session['lid'])
        obj.save()
        return HttpResponse('''<script>alert(' Added Successfully');window.location='/myapp/kd_Add_Product/'</script>''')
def kd_View_Product(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Product.objects.filter(KDUNIT__LOGIN_id=request.session['lid'])
        return render(request, 'Kdunit/View product.html',{'data':res})
def kd_View_Product_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        srch=request.POST['textfield']
        res=Product.objects.filter(KDUNIT__LOGIN_id=request.session['lid'],name__icontains=srch)
        return render(request, 'Kdunit/View product.html',{'data':res})
def kd_Edit_Product(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Product.objects.get(id=id)

        return render(request, 'Kdunit/Edit Product.html',{'data':res})
def kd_Edit_Product_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        id=request.POST['id1']
        name = request.POST['textfield']
        quantity = request.POST['textfield3']
        price = request.POST['textfield4']
        details = request.POST['textfield5']
        quanlity = request.POST['textfield7']

        if 'textfield6' in request.FILES:
            photo = request.FILES['textfield6']
            fs = FileSystemStorage()
            from datetime import datetime
            date = datetime.now().strftime("%Y%m%d-%H%M%S")+'.jpg'
            fn = fs.save(date, photo)
            obj = Product.objects.get(id=id)
            obj.quantity = quantity
            obj.quality = quanlity
            obj.name = name
            obj.datails = details
            obj.price = price
            obj.photo = fs.url(date)
            # obj.KDUNIT = K_dunit.objects.get(LOGIN_id=request.session['lid'])
            obj.save()
            return HttpResponse('''<script>alert(' Updated Successfully');window.location='/myapp/kd_View_Product/'</script>''')
        else:
            obj = Product.objects.get(id=id)
            obj.quantity = quantity
            obj.quality = quanlity
            obj.name = name
            obj.datails = details
            obj.price = price
            # obj.KDUNIT = K_dunit.objects.get(LOGIN_id=request.session['lid'])
            obj.save()
            return HttpResponse(
                '''<script>alert(' Updated Successfully');window.location='/myapp/kd_View_Product/'</script>''')


def kd_delete_Product_post(request,id):
    res = Product.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert(' Deleted ');window.location='/myapp/kd_View_Product/'</script>''')
def kd_View_Order(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Order_sub.objects.filter(ORDERMAIN__KDUNIT__LOGIN_id=request.session['lid'])
        return render(request, 'Kdunit/View Orders.html',{'data':res})
def kd_View_Order_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        frmd=request.POST['textfield']
        tod=request.POST['textfield1']
        res = Order_sub.objects.filter(ORDERMAIN__date__range=[frmd,tod],ORDERMAIN__KDUNIT__LOGIN_id=request.session['lid'])
        return render(request, 'Kdunit/View Orders.html',{'data':res})


def kd_View_Payment(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Payment.objects.filter(KDUNIT__LOGIN_id=request.session['lid'])
        return render(request, 'Kdunit/View payment.html',{'data':res})
def kd_View_Payment_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        frmd = request.POST['textfield']
        tod = request.POST['textfield1']
        res=Payment.objects.filter(KDUNIT__LOGIN_id=request.session['lid'],date__range=[frmd,tod])
        return render(request, 'Kdunit/View payment.html',{'data':res})
def kd_View_Kuri_Payment(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        res=Kuri_Payment.objects.filter(KDUNIT__LOGIN_id=request.session['lid'])
        return render(request, 'Kdunit/View Kuris payment.html',{'data':res})
def kd_View_Kuri_Payment_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('Already Logouted');window.location='/myapp/login/'</script>''')
    else:
        frmd = request.POST['textfield']
        tod = request.POST['textfield1']
        res=Kuri_Payment.objects.filter(KDUNIT__LOGIN_id=request.session['lid'],date__range=[frmd,tod])
        return render(request, 'Kdunit/View Kuris payment.html',{'data':res})


#########################member##################

def mem_login(request):
    username=request.POST['username']
    password=request.POST['password']
    obj=Login.objects.filter(username=username,password=password)
    if obj.exists():
        obj=Login.objects.get(username=username,password=password)
        lid=obj.id
        if obj.type == 'kdmember':
            return JsonResponse({'status':'ok','lid':lid,'type':obj.type})
        if obj.type == 'user':
            return JsonResponse({'status':'ok','lid':lid,'type':obj.type})
        else:
            return JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status':'no'})


def mem_view_profile(request):
    lid=request.POST['lid']
    oo=K_dmembers.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','name':oo.name,'phone':oo.phone,
                         'Email':oo.Email,'place':oo.place,'panchayath':oo.panchayath,
                         'ward':oo.ward,'district':oo.district,'unitname':oo.KDUNIT.name})

def mem_change_password(request):
    lid=request.POST['lid']
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    if newpassword == confirmpassword:
        obj=Login.objects.filter(id=lid,password=oldpassword)
        if obj.exists():
            obj = Login.objects.get(id=lid,password=oldpassword)
            obj.password=confirmpassword
            obj.save()
            return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status':'no'})

def mem_forwarded_notification(request):
    oo=Notification.objects.filter(status='forwarded')
    l=[]
    for i in oo:
        l.append({'id':i.id,'date':i.date,'notification':i.notification})

    return JsonResponse({'status':'ok','data':l})

def mem_view_events(request):
    lid=request.POST['lid']
    ee=K_dmembers.objects.get(LOGIN_id=lid)
    d=ee.KDUNIT.id
    oo=Events.objects.filter(KDUNIT_id=d)
    l=[]
    for i in oo:
        l.append({'id':i.id,'date':i.date,'time':i.time,
                  'theme':i.theme,'title':i.title})
    return JsonResponse({'status':'ok','data':l})

def mem_view_kurees(request):
    lid=request.POST['lid']

    ee = K_dmembers.objects.get(LOGIN_id=lid)
    d = ee.KDUNIT.id
    oo=Kuris.objects.filter(KDUNIT=d)
    l=[]
    for i in oo:
        l.append({'id':i.id,'kdid':i.KDUNIT.id,'name':i.name,'totalAmount':i.totalAmount,
                  'totalinstallments':i.totalinstallments,'installmentamount':i.installmentamount,
                  'startingDate':i.startingDate,
                  'EndingDate':i.EndingDate})

    return JsonResponse({'status':'ok','data':l})

def mem_send_payment(request):
    lid = request.POST['lid']
    kid = request.POST['kid']
    kdid=request.POST['kdid']
    amount = request.POST['amount']
    dd=Kuri_Payment()
    dd.KDUNIT_id=kdid
    dd.KDMEMBER=K_dmembers.objects.get(LOGIN_id=lid)
    dd.KURIS_id=kid
    from datetime import datetime
    dd.date=datetime.now()
    dd.amount=amount
    dd.status='paid'
    dd.save()
    return JsonResponse({'status':'ok'})

def mem_view_product(request):
    lid=request.POST['lid']
    ee = K_dmembers.objects.get(LOGIN_id=lid)
    d = ee.KDUNIT.id
    oo=Product.objects.filter(KDUNIT=d)
    l=[]
    for i in oo:
        l.append({'id':i.id,'quantity':i.quantity,'datails':i.datails,
                  'price':i.price,'photo':i.photo,
                  'name':i.name,'quality':i.quality})
    return JsonResponse({'status':'ok','data':l})

####################user############



def usr_signup(request):
    name=request.POST['name']
    phone=request.POST['phone']
    age=request.POST['age']
    email=request.POST['email']
    photo=request.POST['photo']
    place=request.POST['place']
    panchayath=request.POST['panchayath']
    ward=request.POST['ward']
    district=request.POST['district']
    password=request.POST['password']
    cpassword=request.POST['confirmpassword']

    import datetime
    import base64
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    a = base64.b64decode(photo)
    fh = open(r"C:\\Users\\Microsoft\\PycharmProjects\\KDproject\\media\\user\\" + date + ".jpg", "wb")
    path = "/media/user/" + date + ".jpg"
    fh.write(a)
    fh.close()
    if password == cpassword:
        oo=Login()
        oo.username=email
        oo.password=cpassword
        oo.type='user'
        oo.save()
        obj=User()
        obj.name=name
        obj.phone=phone
        obj.age=age
        obj.email=email
        obj.photo=path
        obj.place=place
        obj.panchayath=panchayath
        obj.ward=ward
        obj.district=district
        obj.LOGIN_id=oo.id
        obj.save()
        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'no'})

def usr_view_profile(request):
    lid=request.POST['lid']
    i=User.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','name':i.name,'phone':i.phone,'age':i.age,'email':i.email,'photo':i.photo,'place':i.place,'panchayath':i.panchayath,'ward':i.ward,'district':i.district})

def usr_edit_profile(request):
    lid=request.POST['lid']
    name = request.POST['name']
    phone = request.POST['phone']
    age = request.POST['age']
    email = request.POST['email']
    photo = request.POST['photo']
    place = request.POST['place']
    panchayath = request.POST['panchayath']
    ward = request.POST['ward']
    district = request.POST['district']


    obj = User.objects.get(LOGIN_id=lid)
    obj.name = name
    obj.phone = phone
    obj.age = age
    obj.email = email
    obj.photo = photo
    obj.place = place
    obj.panchayath = panchayath
    obj.ward = ward
    obj.district = district
    obj.save()
    return JsonResponse({'status':'ok'})

def usr_view_kdunit(request):
    oo=K_dunit.objects.all()
    l=[]
    for i in oo:
        l.append({'id':i.id,'name':i.name,'unit_no':i.unit_no,'place':i.place,'panchayath':i.panchayath,'ward':i.ward,'district':i.district,'Email':i.Email,'phone':i.phone})

    return JsonResponse({'status':'ok','data':l})

def usr_view_product(request):
    kid=request.POST['kid']
    oo=Product.objects.filter(KDUNIT_id=kid)
    l=[]
    for i in oo:
        l.append({'id':i.id,'quantity':i.quantity,
                  'datails':i.datails,
                  'price':i.price,'photo':i.photo,
                  'name':i.name,'quality':i.quality})
    return JsonResponse({'status':'ok','data':l})
def usr_view_productall(request):
    oo=Product.objects.all()
    l=[]
    for i in oo:
        l.append({'id':i.id,'quantity':i.quantity,
                  'datails':i.datails,
                  'price':i.price,'photo':i.photo,
                  'name':i.name,'quality':i.quality})
    return JsonResponse({'status':'ok','data':l})

def usr_view_ordered_product(request):
    lid=request.POST['lid']
    oo=Order_sub.objects.filter(ORDERMAIN__USER__LOGIN_id=lid)
    l=[]
    for i in oo:
        l.append({'id':i.id,'pid':i.PRODUCT.id,'pname':i.PRODUCT.name,'pphoto':i.PRODUCT.photo,
                  'quantity':i.quantity,'amount':i.ORDERMAIN.amount,
                  'date':i.ORDERMAIN.date,'KDUNIT':i.ORDERMAIN.KDUNIT.id,
                  'stat':i.ORDERMAIN.status})
    return JsonResponse({'status':'ok','data':l})

# def usr_place_order(request):
#     return JsonResponse({'status':'ok'})
#
# def usr_return_product(request):
#     return JsonResponse({'status':'ok'})
#
# def usr_send_payment(request):
#     return JsonResponse({'status':'ok'})

def usr_send_complaint(request):
    lid=request.POST['lid']
    from datetime import datetime
    date=datetime.now()
    comp=request.POST['complaint']
    obj=Complaint()
    obj.date=date
    obj.complaint=comp
    obj.status='pending'
    obj.USER=User.objects.get(LOGIN_id=lid)
    obj.save()

    return JsonResponse({'status':'ok'})

def usr_view_reply(request):
    lid=request.POST['lid']
    oo=Complaint.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in oo:
        l.append({'id':i.id,'date':i.date,'complaint':i.complaint,'status':i.status,'reply':i.reply})

    return JsonResponse({'status':'ok','data':l})

def  usr_view_events(request):
    oo=Events.objects.all()
    l=[]
    for i in oo:
        l.append({'id':i.id,'date':i.date,
                  'time':i.time,'theme':i.theme,
                  'title':i.title,'KDUNIT':i.KDUNIT.name})

    return JsonResponse({'status':'ok','data':l})

def  usr_change_password(request):
    lid = request.POST['lid']
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    if newpassword == confirmpassword:
        obj = Login.objects.filter(id=lid, password=oldpassword)
        if obj.exists():
            obj = Login.objects.get(id=lid, password=oldpassword)
            obj.password = confirmpassword
            obj.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})


def  usr_send_feeddback(request):
    lid=request.POST['lid']
    feedback=request.POST['feedback']
    from datetime import datetime
    oo=Feedback()
    oo.date=datetime.now()
    oo.USER=User.objects.get(LOGIN_id=lid)
    oo.feedback=feedback
    oo.save()
    return JsonResponse({'status':'ok'})

def User_add_tocart(request):
        pid = request.POST['pid']
        cd = Product.objects.get(id=pid)
        print(cd.photo)
        return JsonResponse({'status': 'ok', 'pid': cd.id, 'name': cd.name, 'photo': cd.photo, 'price': cd.price,
                             'datails': cd.datails,'quality':cd.quality,'kd':cd.KDUNIT.name})


def User_AddCart_post(request):
    lid = request.POST['lid']
    pid = request.POST['pid']
    quantity = request.POST['quantity']
    ob = Cart()
    ob.PRODUCT = Product.objects.get(id=pid)
    ob.USER = User.objects.get(LOGIN_id=lid)
    ob.quantity = quantity
    ob.save()
    return JsonResponse({'status': 'ok'})

def User_return_product(request):
    oid = request.POST['oid']
    i=Order_sub.objects.get(id=oid)
    return JsonResponse({'status': 'ok','pid':i.PRODUCT.id,'pname':i.PRODUCT.name,
                         'pphoto':i.PRODUCT.photo,
                  'quantity':i.quantity,'amount':i.ORDERMAIN.amount,
                  'date':i.ORDERMAIN.date,'KDUNIT':i.ORDERMAIN.KDUNIT.id,
                  'stat':i.ORDERMAIN.status})

def User_return_product_post(request):
    lid=request.POST['lid']
    pid=request.POST['pid']
    oid=request.POST['oid']
    reason=request.POST['reason']
    oo=Order_sub.objects.get(id=oid).id
    bb=Order_main.objects.filter(id=oo).update(status='returned')

    ob=Return_order()
    ob.PRODUCT_id=pid
    ob.USER=User.objects.get(LOGIN_id=lid)
    ob.reason=reason
    ob.save()
    return JsonResponse({'status': 'ok'})

def User_View_cart(request):
    lid = request.POST['lid']
    res = Cart.objects.filter(USER__LOGIN_id=lid)

    l = []
    total=0
    for i in res:
        total+=(float(i.PRODUCT.price)*float(i.quantity))
        l.append(
            {'id': i.id, 'name': i.PRODUCT.name, 'photo': i.PRODUCT.photo, 'price': i.PRODUCT.price, 'datails': i.PRODUCT.datails,'quantity':i.quantity})
    return JsonResponse({'status': 'ok', 'data': l, 'total':total})


################################payment########################


from django.db import transaction

# def user_makepayment(request):
#     lid=request.POST['lid']
#
#
#     amount=request.POST['amount']
#     wa=Cart.objects.filter(USER__LOGIN_id=lid)
#     for i in wa:
#         od=Order_main()
#         od.USER=User.objects.get(LOGIN_id=lid)
#         from datetime import datetime
#         od.date=datetime.now()
#         od.KDUNIT=i.PRODUCT.KDUNIT
#         od.status='ordered'
#         od.amount=amount
#         od.save()
#
#         v=Order_sub()
#         v.ORDERMAIN=od.id
#         v.PRODUCT=i.PRODUCT
#         v.quantity=i.quantity
#         v.save()
#
#         d=Payment()
#         d.KDUNIT=i.PRODUCT.KDUNIT
#         d.LOGIN=lid
#         d.ORDERMAIN=od.id
#         d.date=datetime.now()
#         d.amount=amount
#         d.status='paid'
#         d.save()
#     return JsonResponse({'status':'ok'})



def user_makepayment(request):
    lid=request.POST['lid']



    res = Cart.objects.filter(USER__LOGIN_id=lid).values_list('PRODUCT__KDUNIT').distinct()

    for i in res:
            print(i)
            mytotal = 0

            res2 = Cart.objects.filter(USER__LOGIN_id=lid)

            boj = Order_main()
            boj.USER = User.objects.get(LOGIN_id=lid)
            boj.amount = 0
            import datetime
            boj.date = datetime.datetime.now().date().today()
            boj.KDUNIT_id = i[0]
            boj.status = 'ordered'

            boj.save()

            ress = Payment()
            ress.LOGIN_id = lid
            ress.ORDERMAIN = boj
            ress.date = datetime.datetime.now().date().today()
            ress.status = 'paid'
            ress.KDUNIT_id = i[0]
            ress.save()

            for j in res2:



                bs=Order_sub()
                bs.ORDERMAIN=boj
                bs.PRODUCT_id=j.PRODUCT_id
                bs.quantity=j.PRODUCT_id
                bs.save()

                mytotal+=(float(j.PRODUCT.price)*int(j.quantity))





            print(mytotal)
            Cart.objects.filter(USER__LOGIN_id=lid).delete()
            boj=Order_main.objects.get(id=boj.id)
            boj.amount=mytotal

            boj.save()



    return JsonResponse({'k':'0','status':"ok"})




