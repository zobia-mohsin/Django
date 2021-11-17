from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "MainApp/index.html") #look at index.html template in views, every view will have an argument request
#now created folder in mainapp called templates then another folder in it called MainApp
