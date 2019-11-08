from django.conf.urls import url
from django.urls import path,include
from .views import registerview
from .views import loginview,logoutview

app_name='accounts'

urlpatterns = [
    
    path(r'register/', registerview, name="register"),
    path(r'login/', loginview, name="login"),
    path(r'logout/', logoutview, name="logout"),
]