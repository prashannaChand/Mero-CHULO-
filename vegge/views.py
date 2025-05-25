from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def recipes(request):
    if request.method == 'POST':
        # Only process add recipe if the add button was clicked
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
        # Otherwise, ignore POST (it's from Delete/Edit)
        return redirect('recipes')
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
       queryset = queryset.filter(name__icontains=request.GET.get('search'))
    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('recipes')

def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
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
    