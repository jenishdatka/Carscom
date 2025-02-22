from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_view),
    path('car_detail/<int:pk>', views.detail_view, name='detail'),
    path('car_detail_2/<int:pk>', views.detail_view_2, name='detail_2'),
    path('car_create/', views.car_created_view),
    path('category/<str:category>', views.category_view),
    path('car_create_2/', views.car_create_view_2),
    path('car_delete/int:pk', views.delete_view, name='delete')

    ]