from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', views.home),
    path('menu/', views.MenuView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('api/menu/', views.MenuItemView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/booking/', views.BookingItemView.as_view()),
    path('api/booking/<int:pk>', views.SingleBookingItemView.as_view()),
    
    # * Token Stuffs
    path('api-token-auth/', obtain_auth_token), # Insomnia: Payload: Username, Password
   #  http://127.0.0.1:8000/auth/token/login/  # Browser: Payload: Username, Password
]

# * iceice: 58ee80a96c57355d0e33fcad893cec172b195854