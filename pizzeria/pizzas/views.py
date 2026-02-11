from django.shortcuts import render
from .models import Pizza
# Create your views here.
def index(request):
    """The home page for pizzas"""
    return render(request, 'pizzas/index.xhtml')

def pizzas(request):
    """list the pizzas"""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.xhtml', context)

def pizza(request, pizza_id):
    """single pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.xhtml', context)