from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Blog,Reviews
from django.contrib import messages



# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    blogs=Blog.objects.all()
    reviews=Reviews.objects.all()
    context={'blogs':blogs,'reviews':reviews} 
    print(blogs[0].id)   
    return render(request,'index.html',context)

def register(request):
    if request.method == "POST":
        fname=request.POST['fname']
        email=request.POST['email']
        uname=request.POST['uname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        print(fname,email,uname,pass1,pass2)
        
        #validations
        if len(uname)>10:
            return redirect(register)
        
        if (pass1!= pass2):
            return redirect(register)


        myuser = User.objects.create_user(uname,email,pass1)
        myuser.first_name = fname
        myuser.save()
        user=authenticate(username=myuser.username,password=pass1)
        login(request,user)
        return redirect(home)
    return render(request,'register.html')


def loginPage(request):
    if request.method == "POST":
        uname=request.POST['uname']
        pass1=request.POST['pass']
        print(uname,pass1)
        user=authenticate(username=uname,password=pass1)
        login(request,user)
        messages.success(request,'login Successfully')
        return redirect(home)    
    return render(request,'login.html')


def logoutPage(request):
    logout(request)
    return redirect(home)

def profile(request):
    return redirect(home)

def addblog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        print(title,content)
        blog=Blog(user=request.user,title=title,content=content)
        blog.save()
        return redirect(home)
    return render(request,'addblog.html')

def blog(request,id):
    blog=Blog.objects.get(id=id)
    reviews=Reviews.objects.filter(blog=blog)
    context={'blog':blog,'reviews':reviews}
    # context={'blog':blog}
    return render(request,'blog.html',context)


def comment(request):
    if request.method == "POST":
        id=request.POST['id']
        comment=request.POST['comment']
        blog=Blog.objects.get(id=id)
        review=Reviews(user=request.user,blog=blog,comment=comment)
        review.save()
        return redirect(home)