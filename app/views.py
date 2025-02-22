from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Car, Category,Color
from .forms import CarCreateForm, CarForm


def all_view(request):
    cars = Car.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        cars = Car.objects.filter(Q(title_icontains=search) | Q(description_icontains=search)
                                  | Q(color_icontains=search))

    return render(request=request, template_name='app/main_all_cars.html', context={"cars":cars})


def detail_view(request, pk):

    car = Car.objects.get(id=pk)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()


    form = CarForm(instance=car)

    return render(request=request, template_name='app/detail.html', context={"car": car, "form": form})


def detail_view_2(request, pk):
    categories = Category.objects.all()
    colors = Color.objects.all()
    car = Car.objects.get(id=pk)

    if  request.method == 'POST':
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

        car.make = make
        car.model= model
        car.year = year
        car.description = description
        car.price = price
        car.color_id = color
        car.category_id = category
        car.image = image

        car.save()
        return redirect('')

    return render(request=request, template_name='app/detail_2.html', context={"car":car, "categories": categories,
                                                                             "colors":colors})

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

def car_create_view_2(request):

    if request.method =='POST':
        form = CarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')

    form = CarCreateForm

    return render(request=request, template_name='app/car_create2', context={'form':form})

def delete_view(reguest, pk):
    car = Car.objects.get(id=pk)
    car.delete()

    return redirect('')