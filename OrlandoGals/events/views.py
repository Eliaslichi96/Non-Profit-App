# orlandogals/events/views.py
from rest_framework import viewsets
from .serializers import EventSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Event
from .forms import PostForm, EventForm

def home(request):
    posts = Post.objects.all()
    events = Event.objects.all()
    return render(request, 'events/home.html', {'posts': posts, 'events': events})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'events/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'events/post_detail.html', {'post': post})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

@login_required
def add_post(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'events/add_post.html', {'form': form})

@login_required
def add_event(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})
