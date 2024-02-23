from django.urls import path
from backend_portfolio import views

urlpatterns = [

    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/logout/', views.LogoutView.as_view(), name='logout'),
]
