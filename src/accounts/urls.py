from django.conf.urls import url
from django.urls import path,include
from .views import registerview

app_name='accounts'

urlpatterns = [
    
    path(r'^register/', registerview, name="register"),
   
]