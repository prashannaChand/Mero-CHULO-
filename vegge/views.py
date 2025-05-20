from django.shortcuts import render
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
        # You can add logic to save the data here
    return render(request, 'recipes.html')