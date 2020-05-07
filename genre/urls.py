from django.urls import path
from . import views

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("details/<pk>/", views.details.as_view(), name="details"),
    path("register/", views.UserFormView.as_view(), name="userform"),
]
