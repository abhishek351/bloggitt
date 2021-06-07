from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import post,profile
from .forms import contactform,UserUpdateform,ProfileUpdateform,blogForm
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    posts=post.objects.all().order_by("-Sno")
    paginator=Paginator(posts,9)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number) 

    return render(request,'home.html',{"page_obj":page_obj})

def contact(request):
    form = contactform(request.POST or None)
      
    
    if form.is_valid():
        form.save()
        messages.success(request,"Your issue has been submitted! It will solve Soon.")
        return redirect(home)

    
    return render(request,'contact.html',{'form':form})

def blogform(request):
    if  request.user.is_authenticated:
        user=request.user
        
        form = blogForm(request.POST,request.FILES)
        if form.is_valid():
                obj=form.save(commit=False)
                obj.user=user
                obj.save()
                messages.success(request,"Your blog has been created")
                return redirect(home)
        else:
            form = blogForm()
    return render(request, 'blogform.html',{'blogform':form})




def search(request):
    find=request.GET['find']
    
    allpost=post.objects.filter(title__contains=find)
    params={'allpost':allpost}
    return render(request,'search.html',params)


def delete_blog(request,pk):
    blogs=post.objects.get(Sno=pk)
    blogs.delete()
    messages.success(request, 'Your Blog has been deleted.')
    return redirect(home)





def blogview(request, slug):
    blogs=post.objects.filter(slug=slug).first()
    
    return render(request,'blogview.html',{"Blog":blogs})

def login_page(request):
    if request.method == 'POST':


        loginusername=request.POST['loginusername']
        loginPassword=request.POST['loginPassword']


        User=authenticate(username=loginusername,password=loginPassword)

        if User is not None:
            login(request,User)
            messages.success(request, f'Welcome: {loginusername}')
            return redirect(home)

        else:
            messages.success(request, 'Invalid Username or Password')
            return redirect(home)

    
    return HttpResponse('404')

def signup_page(request):
    if request.method == 'POST':

        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        Email=request.POST['Email']
        Password1=request.POST['Password1']
        Password2=request.POST['Password2']

        if Password1 != Password2:
            messages.success(request,"Password  Do Not  Match!")
            return redirect(home)
        else: 
            myuser=User.objects.create_user(username,Email,first_name=fname,last_name=lname,password=Password1)
            myuser.save()
            messages.success(request, 'Your account have been created successfully!')
            return redirect(home)

    
    return render(request,"signup")

def profile(request):   
    if request.method =="POST":
        form1=UserUpdateform(request.POST,instance=request.user)
        form2=ProfileUpdateform(request.POST,request.FILES,instance=request.user.profile)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect(profile)
    else:

        form1=UserUpdateform(instance=request.user)
        form2=ProfileUpdateform(instance=request.user.profile)



        if  request.user.is_authenticated:
            user=request.user
            myform=post.objects.filter(user=user)




    

    
    context= {

        "form1":form1,
        "form2":form2,
        "myform":myform
        
    }





    return render(request,'profile.html',context)



def logout_page(request):
    logout(request)
    messages.success(request, 'Your logged out  successfully!')
    return redirect(home)
