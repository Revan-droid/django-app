
from django.contrib import admin
from django.urls import path
from apple import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignUpPage,name='signup'),
    path('home/results/',views.ResultsPage,name='results'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
]
