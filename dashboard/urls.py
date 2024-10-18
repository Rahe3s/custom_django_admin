from django.urls import path

from . import views

urlpatterns = [
    path("registration", views.registration, name='registration'),
    path("", views.home, name='home'),
    path("logout_page", views.logout_page, name='logout_page'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("login_page", views.login_page, name='login_page'),
    path("create_user", views.create_user, name='create_user'),
    path("delete_user/<int:id>/", views.delete_user, name='delete_user'),
    path("update_user/<int:id>/", views.update_user, name='update_user'),
    path("search_user", views.search_user, name='search_user'),
]