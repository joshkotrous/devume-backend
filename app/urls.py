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
from devume.views.cities_view import CitiesListView, CitiesCreateView, CitiesRetrieveView, CitiesUpdateView
from devume.views.countries_view import CountriesCreateView, CountriesListView, CountriesRetrieveView, CountriesUpdateView
from devume.views.states_view import StatesCreateView, StatesListView, StatesRetrieveView, StatesUpdateView
from devume.views.work_experience_view import WorkExperienceCreateView, WorkExperienceListView, WorkExperienceRetrieveView, WorkExperienceUpdateView

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
    path('api/cities', CitiesListView.as_view(), name="cities_get"),
    path('api/cities/create', CitiesCreateView.as_view(), name="cities_create"),
    path('api/cities/<int:pk>', CitiesRetrieveView.as_view(), name='cities_retrieve'),
    path('api/cities/<int:pk>', CitiesUpdateView.as_view(), name='cities_update'),
    path('api/countries', CountriesListView.as_view(), name="countries_list"),
    path('api/countries/<int:pk>', CountriesRetrieveView.as_view(), name="countries_retrieve"),
    path('api/countries/create', CountriesCreateView.as_view(), name="countries_create"),
    path('api/countries/<int:pk>/update', CountriesUpdateView.as_view(), name="countries_update"),
    path('api/states', StatesListView.as_view(), name="states_list"),
    path('api/states/<int:pk>', StatesRetrieveView.as_view(), name="states_retrieve"),
    path('api/states/create', StatesCreateView.as_view(), name="states_create"),
    path('api/states/<int:pk>/update', StatesUpdateView.as_view(), name="states_update"),
    path('api/work_experience', WorkExperienceListView.as_view(), name='work_experience_list'),
    path('api/work_experience/<uuid:profile_id>', WorkExperienceRetrieveView.as_view(), name='work_experience_retrieve'),
    path('api/work_experience/create', WorkExperienceCreateView.as_view(), name='work_experience_create'),
    path('api/work_experience/<int:pk>/update', WorkExperienceUpdateView.as_view(), name='work_experience_update'),

    



]
