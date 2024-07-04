from django.shortcuts import render
# from .models import Food


# Create your views here.
# tracker/views.py

from django.shortcuts import render, redirect,get_object_or_404
from .models import FoodItem



def food_list(request):
    foods = FoodItem.objects.all()
    total_calories = sum(food.calories for food in foods)
    context = {
        'foods': foods,
        'total_calories': total_calories
    }
    return render(request, 'tracker/food_list.html', context)

def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = int(request.POST.get('calories'))
        FoodItem.objects.create(name=name, calories=calories)
        return redirect('food_list')
    return render(request, 'tracker/add_food.html')

def remove_food(request, food_id):
    food = FoodItem.objects.get(id=food_id)
    if request.method == 'POST':
        food.delete()
        return redirect('food_list')
    context = {'food': food}
    return render(request, 'tracker/remove_food.html', context)

# def remove_food(request, food_id):
#     food = get_object_or_404(Food, pk=food_id)
    
#     if request.method == 'POST':
#         # Perform deletion logic
#         food.delete()
#         return redirect('food_list')  # Redirect to food list page or another appropriate page
    
#     # Handle GET request (usually render a confirmation page or form)
#     return render(request, 'remove_food.html', {'food': food})

def reset_calories(request):
    if request.method == 'POST':
        FoodItem.objects.all().delete()
        return redirect('food_list')
    return render(request, 'tracker/reset_calories.html')

