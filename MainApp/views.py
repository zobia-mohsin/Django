from django.shortcuts import redirect, render,  get_object_or_404
from .forms import TopicForm, EntryForm, Entry
#create new view after creating URL
from .models import Topic #. means look in same directory that the views is in
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    return render(request, "MainApp/index.html") #look at index.html template in views, every view will have an argument request
#now created folder in mainapp called templates then another folder in it called MainApp

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') #minus for descending, or decensending = FALSE
    #to return data use dictionary
    context = {'topics':topics} #THE KEY OF THIS DICTIONARY COMES FROM TEMPLATE, THE VALUE FROM VIEWS
    return render(request, 'MainApp/topics.html', context) #this returns only the skeletal file, not the data in it
    #PASS CONTEXT TO RENDER

@login_required
def topic(request,topic_id): #the id 1 or 2 gets passed to this function and works on it accordingly
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added') #this will give all entries realted to that id (topic)
    context = {'topic':topic, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm() #if get blank form updated
    else:
        form = TopicForm(data=request.POST) #if post req, load the data into the databases
        if form.is_valid():                 #this will make sure form coplies with rules of model
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            return redirect('MainApp:topics')
    context = {'form':form} #obj that allows us to put data on the skeletal, allows moving of the data
    return render(request, 'MainApp/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False) #save entry after given topic id
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return redirect('MainApp:topic',topic_id=topic_id) #this here because requires the previous webpage

    context = {'form':form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)

@login_required
def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic #lowercase
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST': #means its a get method, not empty form so give it instance
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST) #request.POST to record changes made to database
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id=topic.id) #redirect reader to topic page and specific page topic_id

    context={'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'MainApp/edit_entry.html', context)
