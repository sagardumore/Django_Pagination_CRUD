from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.AddLaptopView,name='add_laptop'),
    path('show/',views.ShowLaptopView,name='show_laptop'),
    path('update/<int:i>/',views.UpdateLaptopView,name='update'),
    path('delete/<int:i>/',views.DeleteLaptopView,name='delete'),
]