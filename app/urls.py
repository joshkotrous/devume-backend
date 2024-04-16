"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from devume.views.profiles_view import ProfileRetrieveView, ProfileCreateView, ProfileUpdateView, ProfileListView
from devume.views.users_view import UserRetrieveView, UserCreateView, UserUpdateView, UserListView
from devume.views.login_view import LoginView
from devume.views.api_key_view import ApiKeyView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/login', LoginView.as_view(), name="login"),
    path('api/login/', LoginView.as_view(), name="login"),
    path('api/users', UserListView.as_view(), name="users_retrieve"),
    path('api/users/<int:pk>', UserRetrieveView.as_view(), name="users_retrieve"),
    path('api/users/create', UserCreateView.as_view(), name="user_create"),
    path('api/users/create/', UserCreateView.as_view(), name="user_create"),
    path('api/users/<int:pk>/update', UserUpdateView.as_view(), name="users_update"),
    path('api/profiles', ProfileListView.as_view(), name="profiles_list"),
    path('api/profiles/', ProfileListView.as_view(), name="profiles_list"),
    path('api/profiles/<uuid:pk>', ProfileRetrieveView.as_view(), name="profiles_retrieve"),
    path('api/profiles/create', ProfileCreateView.as_view(), name="profiles_create"),
    path('api/profiles/create/', ProfileCreateView.as_view(), name="profiles_create"),
    path('api/profiles/update/<uuid:pk>', ProfileUpdateView.as_view(), name="profiles_update"),
    path('api/keys/create', ApiKeyView.as_view(), name="api_key_create"),




]
