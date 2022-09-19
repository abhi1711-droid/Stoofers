from django.urls import path
from django.contrib.auth import views as auth_views
from users import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("", views.signup, name="signup"),
    path("details/", views.customer, name="customer"),
    path("stooferscard/", views.stooferscard, name="stooferscard"),
]
urlpatterns += staticfiles_urlpatterns()
