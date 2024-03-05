from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(),name='home'),
    path('about/', views.AboutView.as_view(), name="about"),
    path('book/', views.BookingViewSet.as_view(
        {'get':'list','post':'create'}
    ), name="book"),
    path('bookings/', views.BookingViewSet.as_view(
        {'get':'retrieve'}
    ), name="bookings"),
    path('reservations/', views.Reservations.as_view(), name="reservations"),

    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),

    path('api-token-auth', obtain_auth_token),
]