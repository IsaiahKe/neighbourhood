from django.contrib import auth
from .models import Alert, Business, Category, Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import AlertForm,ProfileForm, UserInformation
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    title="HomePage"
    hood=request.user.profile.hood
    posts=Alert.objects.filter(hood_id=hood)
    category=Category.objects.all()
    
    return render(request,'index.html',{"title":title,"posts":posts,'hood':hood,'categories':category})
@login_required(login_url='/accounts/login/')
def addpost(request):
    if request.method=='POST':
        form=AlertForm(request.POST,request.FILES)
       
        if form.is_valid():
            print("valid")
            form.save(commit=False)
            print(request.user.username)
            print(request.user.profile)
            form.author_id=request.user.id
            form.hood=request.user.profile.hood
            form.save(commit=True)
            
    form=AlertForm() 
    
    return render(request,'addpost.html',{"form":form})
@login_required(login_url='/accounts/login/')
def updateprofile(request,id):
    user=User.objects.get(pk=id)
    if request.method=='POST':
        
        userinfo=UserInformation(request.POST,instance=user)
        if userinfo.is_valid():
            
            userinfo.save()
        prof=Profile.objects.filter(user_id=id).first()
        profile=ProfileForm(request.POST,request.FILES,instance=prof)
        if profile.is_valid():
            profile.save()   
        return redirect('index')
    profile=ProfileForm()
    userinfo=UserInformation()
    return render(request,'profileupdate.html',{'user':user,'form':profile,'userinfo':userinfo})
def facility(request,id):
    facility=Category.objects.get(pk=id)
    return render(request,'facility.html',{"facility":facility})
def business(request):
    hood=request.user.profile.hood
    buzs=Business.objects.filter(location_id=hood)
    return render(request,'business.html',{"businesses":buzs})
def search(request):
    if request.method=="POST":
        name=request.POST.get('businessname')
       
        biz=Business.objects.filter(name__icontains=name)
    
    return render(request,'search.html',{"results":biz,'term':name})
def logout(request):
    auth.logout(request)
    return redirect('register')