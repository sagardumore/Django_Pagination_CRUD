from django.shortcuts import render,redirect
from .forms import LaptopModelForm
from .models import Laptop
from django.core.paginator import Paginator

def AddLaptopView(request):
    form = LaptopModelForm()
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_laptop")
    template_name = 'LaptopApp/addlaptopform.html'
    context = {'form':form}
    return render(request, template_name, context)

def ShowLaptopView(request):
    laptop_list = Laptop.objects.all()
    paginator = Paginator(laptop_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'LaptopApp/showlaptopinfo.html'
    context = {'page_obj':page_obj}
    return render(request, template_name, context)

def UpdateLaptopView(request,i):
    laptop = Laptop.objects.get(id=i)
    form = LaptopModelForm(instance=laptop)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect("show_laptop")
    template_name = 'LaptopApp/addlaptopform.html'
    context = {'form': form}
    return render(request, template_name, context)

def DeleteLaptopView(request,i):
    laptop = Laptop.objects.get(id=i)
    laptop.delete()
    return redirect("show_laptop")