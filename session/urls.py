from django.urls import path
from session import views
urlpatterns = [
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('signup/', views.registration, name='signup'),
]
