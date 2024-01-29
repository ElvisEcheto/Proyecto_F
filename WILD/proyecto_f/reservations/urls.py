from . import views
from django.urls import path

urlpatterns = [      
    path('', views.reservations, name='reservations'),
	path('reservation_status_/<int:reservation_id>/', views.change_status_reservation, name='reservation_status'),
    path('create/', views.create_reservation, name='create_reservation'),          
]