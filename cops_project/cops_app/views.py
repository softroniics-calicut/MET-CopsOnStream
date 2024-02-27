from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Case,CustomUser,Notification
from django.http import HttpResponse
from .forms import CopsEditForm,UserForm,UserEditForm,StatusEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        pic=request.FILES['pic']
        password=request.POST['password']
        if CustomUser.objects.filter(username=username).exists():
            return render(request,'registration.html',{'message':'username already exists'})
        elif CustomUser.objects.filter(email=email).exists():
            return render(request,'registration.html',{'message':'email already exists'})
        else:

            data=CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                phone=phone,
                email=email,
                address=address,
                pic=pic,
                password=password,
                user_type="user",
                entry="approved"
                )
            data.save()
            return redirect(my_login)
    else:
        return render(request,'registration.html')


def police_register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        age=request.POST['age']
        rank=request.POST['rank']
        badge_number=request.POST['badge_number']
        service_years=request.POST['service_years']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        password=request.POST['password']
        pic=request.FILES['pic']
        if CustomUser.objects.filter(username=username).exists():
            return render(request,'police_registration.html',{'message':'Username already exists'})
        elif CustomUser.objects.filter(email=email).exists():
            return render(request,'police_registration.html',{'message':'Email already exists'})
        else:
            data=CustomUser.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                age=age,
                rank=rank,
                badge_number=badge_number,
                service_years=service_years,
                phone=phone,
                email=email,
                address=address,
                password=password,
                pic=pic,
                user_type="police"
                )
            print(data)
            data.save()
            return redirect(my_login)
    else:
        return render(request,'police_registration.html')



def my_login(request):
    if request.method=='POST':
        username=request.POST['username']
        Password=request.POST['password']
        user=authenticate(username=username, password=Password)
        admin_user = authenticate(request, username=username, password=Password)
        if admin_user is not None and admin_user.is_staff:
            login(request, admin_user)
            return redirect(reverse('admin:index'))  # Redirect to the admin dashboard
        elif user is not None:
            login(request,user)

            if user.user_type=="user":
                return redirect(redir_complaint)
            elif user.user_type=="police" and user.entry=='approved':
                return redirect(redir_police)
            else:
                return render(request,'login.html',{'message2':'Please Wait for Admins approval'})
        else:
            return render(request,'login.html',{'message':'Invalid Login Credentials'})
    else:
        return render(request,'login.html')


def log_out(request):
    logout(request)
    return redirect(my_login)






##############################---------- POLICE ------------###################################






@login_required(login_url='/login/')
def edit_police(request,id):
    police=CustomUser.objects.get(id=id)
    if request.method=='POST':
        police.first_name=request.POST['first_name']
        police.last_name=request.POST['last_name']
        police.username=request.POST['username']
        police.phone=request.POST['phone']
        police.address=request.POST['address']
        police.email=request.POST['email']
        if 'pic' in request.FILES:
            police.pic=request.FILES['pic']
        police.save()


        return render(request,'police_profile.html',{'police':police})
    else:
        return render(request,'edit_police.html',{'police':police})




@login_required(login_url='login')
def my_case(request):
    data=CustomUser.objects.get(id=request.user.id)
    print(data)
    case=Case.objects.filter(police=data).order_by('status')
    print(case)
    return render(request,'my_case.html',{'data':data,'case':case})


@login_required(login_url='login')
def history(request):
    data=CustomUser.objects.get(id=request.user.id)
    case=Case.objects.filter(police=data,status="Case_solved/closed")

    return render(request,'history.html',{'data':data,'case':case})


@login_required(login_url='login')
def edit_status(request,id):
    case=Case.objects.get(id=id)
    print(case)
    form=StatusEditForm(instance=case)
    if request.method=='POST':
        form=StatusEditForm(request.POST,instance=case)
        if form.is_valid():
            form.save()
            return redirect(my_case)
    return render(request,'edit_status.html',{'case':case,'form':form})

@login_required(login_url='login')
def notification(request):
    return render(request,'notification.html')

@login_required(login_url='/login/')
def police_profile(request):
    return render(request,'police_profile.html')


@login_required(login_url='/login/')
def police_notification(request):
    data=Notification.objects.all()
    return render(request,'police_notification.html',{'data':data})


def redir_complaint(request):
    user=CustomUser.objects.get(id=request.user.id)
    # police_officer=CustomUser.objects.filter(user_type=1)
    # user = CustomUser.objects.get(id=id)
    # police_officer = CustomUser.objects.filter(user_type=1)
    if request.method == "POST":
        type = request.POST['type']
        place = request.POST['place']
        date = request.POST['date']
        # culprit = request.POST['culprit']
        victim = request.POST['victim']
        describe = request.POST['describe']
        context = {'message': 'success'}
        # police_officer_id=request.POST['officer']
        # police_officer = CustomUser.objects.get(id=police_officer_id)
        data = Case.objects.create(
                                    type=type, 
                                    place=place, 
                                    date=date, 
                                    # culprit=culprit, 
                                    victim=victim,
                                    describe=describe, 
                                    user=user
                                    )
        
        print(data.type)
        data.save()
        return render(request, 'complaint.html', {'user': user, 'message3': 'Complaint submitted successfully!'})
        
    return render(request,'complaint.html',{'user':user})

def view_feedback(request,id):
    case = Case.objects.get(id=id)
    return render(request, 'view_feedback.html', {'case':case})


def redir_police(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,'police_profile.html',{'user':user})






##################################-------- USER -------##############################




@login_required(login_url='login')
def my_profile(request,id):
    data=CustomUser.objects.get(id=id)
    return render(request,'my_profile.html',{'data':data})


@login_required(login_url='login')
def edit_user(request,id):
    user=CustomUser.objects.get(id=id)
    print(user)
    form=UserEditForm(instance=user)
    if request.method=='POST':
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.username=request.POST['username']
        user.phone=request.POST['phone']
        user.address=request.POST['address']
        user.email=request.POST['email']
        if 'pic' in request.FILES:
            user.pic=request.FILES['pic']

        user.save()
        return render(request,'edit.html',{'message4':'Profile Updated'})
    else:
        return render(request,'edit.html',{'form': form, 'user': user})



@login_required(login_url='/login/')
def file_complaint(request,id):
    d= Case.objects.first()

    context = {
        'd': d,
    }
    user=CustomUser.objects.get(id=id)
    police_officer=CustomUser.objects.filter(user_type=1)
    if request.method=="POST":
        type=request.POST['type']
        place=request.POST['place']
        date=request.POST['date']
        # culprit=request.POST['culprit']
        victim=request.POST['victim']
        describe=request.POST['describe']
        context={'message':'success'}
        # police_officer_id=request.POST['officer']
        # police_officer = CustomUser.objects.get(id=police_officer_id)
        data=Case.objects.create(
            type=type,
            place=place,
            date=date,
            # culprit=culprit,
            victim=victim,
            describe=describe,
            user=user,
            status = "Pending"
            )
        print(data.type)
        data.save()

        return render(request,'complaint.html',{'user':user,'message3':'Complaint submitted successfully!'})
    else:
        return render(request,'complaint.html',{'user':user})
    


@login_required(login_url='/login/')
def show_complaint(request):
    data=CustomUser.objects.get(id=request.user.id)

    case=Case.objects.filter(user=data)

    return render(request,'complaint_view.html',{'data':data,'case':case})

def add_feedback(request,id):
    data = Case.objects.get(id=id)
    if request.method=='POST':
        feedback = request.POST['feedback']
        data.feedback = feedback
        data.save()
        return redirect(show_complaint)
    return render(request, 'add_feedback.html', {'case':data})



@login_required(login_url='my_login')
def my_notification(request):
    data=Notification.objects.all()
    print(data)
    return render(request,'notification.html',{'data':data})


