from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        print(data)
        print(image)

        Recipe.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            image=image
        )
        return redirect('recipes')
    return render(request, 'recipes.html')