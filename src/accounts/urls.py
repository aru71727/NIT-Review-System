from django.conf.urls import url
from django.urls import path,include
from .views import registerview
from .views import givereview,reviewsview,graphviews,graphsviews,placementviews
from .views import loginview,logoutview

app_name='accounts'

urlpatterns = [
    
    path(r'register/', registerview, name="register"),
    path(r'login/', loginview, name="login"),
    path(r'logout/', logoutview, name="logout"),
    path(r'review/(?p<id>)/', givereview,name="review"),
    path(r'reviews/(?p<colg>)/', reviewsview, name="reviews"),
    path(r'simple.pngs', graphviews,name="graph"),
    path(r'simple.pngs/(?p<colg>)/', graphsviews,name="graphs"),
    path(r'placement.pngs', placementviews,name="placement"),

]