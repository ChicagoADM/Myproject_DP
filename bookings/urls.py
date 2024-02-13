from django.urls import path

from bookings import views

app_name = 'bookings'

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
]