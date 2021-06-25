from django.urls import path

from . import views

app_name = "forum"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>", views.PostDetailView.as_view(), name="detail"),
    
    #path("users", views.UserFormView.as_view(), name="user_create"),

    path("create", views.PostCreateView.as_view(), name="create"),
    path("edit/<int:pk>", views.PostUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>", views.PostDeleteView.as_view(), name="delete"),
]