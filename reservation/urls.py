from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('menu/', views.BookingView.as_view()),
    path('booking/', views.MenuView.as_view()),
    path('api/menu/', views.MenuItemView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/booking/', views.BookingItemView.as_view()),
    path('api/booking/<int:pk>', views.SingleBookingItemView.as_view()),
]