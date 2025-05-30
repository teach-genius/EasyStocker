from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user=User.objects.create_user(username=username,
                                 password=password)
        login(request,user)
        return redirect('home')
        
    return render(request,"accounts/index.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("home:home")
    logout(request)
    return render(request,"accounts/signin.html")

def logout_user(request):
    logout(request)
    return redirect("login")