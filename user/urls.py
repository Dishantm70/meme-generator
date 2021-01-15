from django.urls import path, include


from user import views

urlpatterns = [
    path("profile/", views.UserView.as_view(), name="user-profile"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="loout")
]