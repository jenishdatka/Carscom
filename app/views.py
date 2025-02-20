from django.shortcuts import render, redirect
from .models import Car, Category,Color


def all_view(request):
    cars = Car.objects.all()

    return render(request=request, template_name='app/main_all_cars.html', context={"cars":cars})

def detail_view(request, pk):
    car = Car.objects.get(id=pk)

    return render(request=request, template_name='app/detail.html', context={"car":car})

def category_view(request, category):
    cars = Car.objects.filter(category__title=category)

    category = Category.objects.get(title=category)

    return render(request=request, template_name='app/categories.html', context={"cars": cars, "category": category})

def car_created_view(request):
    categories = Category.objects.all()
    colors = Color.objects.all()

    if request.method == 'POST':
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']
        description = request.POST['description']
        price = request.POST['price']
        color_id = request.POST['color_id']
        category_id = request.POST['category_id']
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)
        color = Color.objects.get(id=color_id)

        car = Car(make=make, category=category, model=model, year=year, description=description,
                  price=price, color=color, image=image)
        car.save()

        return redirect('')

    return render(request, 'app/car_create.html', context={"categories": categories, "colors": colors})

