from django.urls import path

from . import views

urlpatterns = [
    path("",views.ProductsList.as_view(), name="products"),
    path("products/<int:id>/", views.LessonsList.as_view(), name="lessons"),
]