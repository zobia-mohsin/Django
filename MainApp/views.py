from django.shortcuts import render
#create new view after creating URL
from .models import Topic #. means look in same directory that the views is in


# Create your views here.
def index(request):
    return render(request, "MainApp/index.html") #look at index.html template in views, every view will have an argument request
#now created folder in mainapp called templates then another folder in it called MainApp

def topics(request):
    topics = Topic.objects.all().order_by('date_added') #minus for descending, or decensending = FALSE
    #to return data use dictionary
    context = {'topics':topics} #THE KEY OF THIS DICTIONARY COMES FROM TEMPLATE, THE VALUE FROM VIEWS
    return render(request, 'MainApp/topics.html', context) #this returns only the skeletal file, not the data in it
    #PASS CONTEXT TO RENDER