from django.urls import path
from account import views
from posts.views import HomeView


urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("login", views.LogInView.as_view(), name="login"),
    path("logout", views.logoutfn, name="logout"),
    path("profile/add", views.ProfileView.as_view(), name="addprofile"),
    path("profile/update/<int:user_id>", views.UpdateProfileView.as_view(), name="updateprofile")
]

