from django.urls import path
from . import views

urlpatterns = [
    path("", views.room_list, name="room_list"),
    path("<int:pk>", views.room_details, name="room_details"),
    path("booking-room", views.book_room, name="booking_room")
]
