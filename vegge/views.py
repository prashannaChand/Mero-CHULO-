from django.shortcuts import render,redirect
from .models import *


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
    context = {
        'recipes': queryset
    }
    return render(request, 'recipes.html', context)

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('recipes')