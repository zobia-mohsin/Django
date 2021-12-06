from django.urls import path

from . import views #dot means from the same folder

app_name = "MainApp"
#1. create url
#2. create views
#path is homepage look at index function in views whose name is index, because location is blank
urlpatterns = [
    path('',views.index,name='index'),
    path('topics',views.topics,name='topics'), #added a new page, create new view after creating URL
    path('topics/<int:topic_id>/',views.topic,name='topic'), #to load individual topics, the id separates chess from rock climbing
    #variable: <int:topic_id>/
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'), #new enrty needs a topic id so knows what the entry is for
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]

