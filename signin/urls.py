from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('signout/', views.logout),
    path('emailverification/', views.forgotPassword),
    path('email/', views.email),
    path('resetpwd/', views.resetPwd),
    path('newPassword/', views.newPassword),

]
