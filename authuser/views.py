from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            messages.warning(request,'You Are Logged')
            return redirect('/')
        else:
            return redirect('authuser:login')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']

        next_url=request.POST.get('next')

        if username and password:
            user=authenticate(request,username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    messages.success(request,f'Welcome Mr {username} In Your Application')
                    return redirect(next_url)
                else:
                    messages.error(request,'Sorry This User Not Active')
                    return redirect('authuser:login')
            else:
                messages.error(request,'Sorry this Username or Password Not correct ')
                return redirect('authuser:login')
        messages.error(request,'Sorry this User Not Found ')
        return redirect('authuser:login')
    

    
    

class LogoutView(View):
    def post (self, request):
        logout(request)
        messages.success(request, 'Successful Logged Out')
        return redirect('/')
    

@login_required        
def all_user(request):
    return render(request,'authuser/all_user.html',{})

@login_required
def base(request):
    return render(request,'blank.html',{})


