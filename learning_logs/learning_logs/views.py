from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.
def index(request):
    """The home page for learning log"""
    return render(request, 'learning_logs/index.xhtml')

def topics(request):
    """Topics page"""
    # query the database for topic objects and order them by the date_added field, assign to topics
    topics = Topic.objects.order_by('date_added')
    # create an context and send to the template
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.xhtml', context)

def topic(request, topic_id):
    """Topic page"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request,  'learning_logs/topic.xhtml', context)

def new_topic(request):
    """Adding a new topic"""
    if request.method != 'POST':
        # no data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    # display a blank or invalid form
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.xhtml', context)

def new_entry(request, topic_id):
    """Adding a new entry to a topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.xhtml', context)

def edit_entry(request, entry_id):
    """Edit a entry from a topic"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.xhtml', context)