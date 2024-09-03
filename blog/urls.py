from django.contrib.auth import views as auth_views
from django.urls import path

from .services.auth import RegisterUserView
from .views import basic, post_list, post_detail, post_create, post_edit, post_delete

urlpatterns = [
    path("basic", basic),
    path("", post_list, name="post_list"),
    path("posts/<int:pk>", post_detail, name="post_detail"),
    path("posts/new/", post_create, name="post_create"),
    path('posts/edit/<int:pk>/', post_edit, name='post_edit'),
    path('posts/delete/<int:pk>/', post_delete, name='post_delete'),
    path('login/', auth_views.LoginView.as_view(next_page="post_list", template_name="blog/login.html"), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'), name='logout'),
]
