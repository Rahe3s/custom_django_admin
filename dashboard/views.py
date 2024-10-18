from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserDetailsForm,loginForms,UpdateForm
from .models import User_Details
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

def registration(request):
    if request.method == 'POST':
    
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')

            
            if User_Details.objects.filter(username=username).exists():
                
                form.add_error('username', "Username is already registered.")
            else:
                user = form.save(commit=False)
                password = form.cleaned_data.get('password')
                user.set_password(password)
                user.save()
                response=redirect(login_page)

                return response
        else:
            
            return render(request, "register.html", {'form': form})
    else:
        form = UserDetailsForm()

    return render(request, 'register.html', {'form': form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        loginform = loginForms(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:            
            login(request, user)
            if user.is_staff:

                response = redirect('dashboard')            
                return response
            else:
                return redirect('home')
        else:
            loginform.add_error('username', "User doesn't exist.")

    else:
        loginform = loginForms()
    
    return render(request, 'login_page.html',  {'loginform': loginform})



@login_required(login_url='login_page')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):   
    
    return render(request, "home.html")



@login_required(login_url='login_page')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):   
    user_data=User_Details.objects.all()    
    return render(request, "dashboard.html" ,{'user_data': user_data}   )



def delete_user(request,id):
    user_data = User_Details.objects.get(id=id)    
    print(user_data)
    user_data.delete()
    return redirect('dashboard')


def update_user(request,id):     
    user_data = User_Details.objects.get(id=id)
    if request.method == "POST":
        form = UserDetailsForm(request.POST, instance=user_data)
        if form.is_valid():
            form.save() 
            return redirect('dashboard')  
    else:   
        form = UserDetailsForm(instance=user_data)
        
    return render(request, 'update_user.html', {'form': form ,  'user_data': user_data})


def create_user(request):
    if request.method == 'POST':
    
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')

            
            if User_Details.objects.filter(username=username).exists():
                
                form.add_error('username', "Username is already registered.")
            else:
                user = form.save(commit=False)
                password = form.cleaned_data.get('password')
                user.set_password(password)
                user.save()
                
                
                return redirect("dashboard")

                
        else:
            
            return render(request, "create_user.html", {'form': form})
    else:
        form = UpdateForm()

    return render(request, 'create_user.html', {'form': form})


def search_user(request):
    query = request.GET.get('search')  

    if query:
        
        user_data = User_Details.objects.filter(username__startswith=query)
    else:
        user_data = User_Details.objects.all()

    return render(request, 'dashboard.html', {'user_data': user_data, 'query': query})


def logout_page(request):
    logout(request)
    response = redirect('login_page')
    return response