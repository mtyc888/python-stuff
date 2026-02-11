from django.shortcuts import render

# Create your views here.
def index(request):
    """home page for meal plans"""
    return render(request, 'meal_plans/index.html')