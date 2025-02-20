from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_view),
    path('car/<int:pk>', views.detail_view, name='detail'),
    path('car_create/', views.car_created_view),
    path('category/<str:category>', views.category_view),
    ]