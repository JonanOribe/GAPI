from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('register/', views.registerPage,name="register"),
    path('login/', views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('user/', views.userPage,name="user-page"),
    path('products/', views.products,name="products"),
    path('customer/<str:pk>/', views.customer,name="customer"),
    path('account/', views.accountSettings, name="account"),
    path('create_order/<str:pk>', views.create_order,name="create_order"),
    path('update_order/<str:pk>/', views.update_order,name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order,name="delete_order"),
]
