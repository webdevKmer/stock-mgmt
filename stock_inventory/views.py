from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "stock_inventory/home.html")