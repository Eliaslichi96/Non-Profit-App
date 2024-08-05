from django.contrib import admin
from events.models import Post, Event  # Use absolute import

admin.site.register(Post)
admin.site.register(Event)
