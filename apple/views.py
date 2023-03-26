from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import joblib
loaded_lr_model = joblib.load("ML_models\lr_bin.joblib")
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    if request.method == 'POST':
        rate=request.POST.get('rate','default')
        sttl=request.POST.get('sttl','default')
        sload=request.POST.get('sload','default')
        dload=request.POST.get('dload','default')
        ct_srv_src=request.POST.get('ct_srv_src','default')
        ct_state_ttl=request.POST.get('ct_state_ttl','default')
        ct_dst_ltm=request.POST.get('ct_dst_ltm','default')
        ct_src_dport_ltm=request.POST.get('ct_src_dport_ltm','default')
        ct_dst_sport_ltm=request.POST.get('ct_dst_sport_ltm','default')		
        ct_dst_src_ltm=request.POST.get('ct_dst_src_ltm','default')
        ct_src_ltm=request.POST.get('ct_src_ltm','default')
        state_CON=request.POST.get('state_CON','default')
        state_INT=request.POST.get('state_INT','default')
        labels=[[float(rate),float(sttl),float(sload),float(dload),float(ct_srv_src),float(ct_state_ttl),float(ct_dst_ltm),float(ct_src_dport_ltm),float(ct_dst_sport_ltm),float(ct_dst_src_ltm),float(ct_src_ltm),float(state_CON),float(state_INT)]]
        our_labels = loaded_lr_model.predict(labels)

        if our_labels[0]==0:
            wine_quality="A Poor Quality Wine"
        if 400<our_labels[0]==1:
            wine_quality="A good Quality Wine"
        		
        print(wine_quality)
    return render (request,'home.html')

def SignUpPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render (request,'incorrect password.html')

    return render (request,'login.html')

    
                
def LogoutPage(request):
    logout(request)
    return redirect('login')