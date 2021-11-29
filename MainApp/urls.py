from django.urls import path

from . import views #dot means from the same folder

app_name = "MainApp"
#1. create url
#2. create views
#path is homepage look at index function in views whose name is index, because location is blank
urlpatterns = [
    path('',views.index,name='index'),
    path('topics',views.topics,name='topics') #added a new page, create new view after creating URL

]

