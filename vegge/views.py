from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from time import sleep



# Create your views here.
def recipes(request):
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
       queryset = queryset.filter(name__icontains=request.GET.get('search'))
    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)
    

def delete_recipe(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to delete a recipe!")
        return redirect('login_page')
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('recipes')

def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to edit a recipe!")
        return redirect('login_page')
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')
        if name:
            recipe.name = name
            recipe.description = description
            if image:
                recipe.image = image
            recipe.save()
            return redirect('recipes')
        else:
            print("Name is missing!")
    return render(request, 'edit_recipe.html', {'recipe': recipe})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or password!")
            return redirect('login_page')
        else:
            login(request, user)
            messages.success(request, "Login successful!")
            sleep(1)  # Adding a delay for better UX
            return redirect('recipes')
        
    return render(request, 'login.html')
        

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=User.objects.filter(username=username)
        if user:
            # If user already exists, show a message and redirect
            messages.error(request, "Username already exists!") 
            print("Username already exists!")
            return redirect('register')


        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        messages.success(request, "User registered successfully!")
        print("User registered successfully!")  
        return redirect('register')
    

    return render(request, 'register.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect('login_page')
    else:
        messages.error(request, "You are not logged in!")
        return redirect('login_page')
    
def add_recipe(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add a recipe!")
        return redirect('login_page')
    if request.method == 'POST':
        if 'name' in request.POST:
            data = request.POST
            print("POST data:", data)
            name = data.get('name')
            description = data.get('description')
            image = request.FILES.get('image')
            if name:
                Recipe.objects.create(
                    name=name,
                    description=description,
                    image=image
                )
            else:
                print("Name is missing!")
            return redirect('recipes')
        return redirect('recipes')
    # For GET requests, render the form
    return render(request, 'add_recipe.html')