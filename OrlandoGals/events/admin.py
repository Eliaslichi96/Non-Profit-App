from django.contrib import admin
from .models import Post, Event
from .forms import EventAdminForm

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
