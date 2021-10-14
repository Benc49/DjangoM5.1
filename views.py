from django.shortcuts import render

# Create your views here.

def root(request):
    if request.GET:
        name = str(request.GET["name"])
        return render(request, "root.html", {"name": name})
    else: 
        return render(request, "root.html")


def age_in(request):
    if request.GET:
        b_year = int(request.GET["age"])
        age_in_2050 = 2050 - b_year
        return render(request, "age_in_2050.html", {"age_in_2050": age_in_2050})
    else:
        return render(request, "age_in_2050.html")


def order(request):
    if request.GET:
        burger = int(request.GET["burger"])* 4.50
        fries = int(request.GET["fries"])* 1.50
        drink = int(request.GET["drink"])* 1.00
        total = burger + fries + drink
        return render(request, "order.html", {"burger": burger, "fries": fries, "drink": drink, "total": total})
    else:
        return render(request, "order.html")



