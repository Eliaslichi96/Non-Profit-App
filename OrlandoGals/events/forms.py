from django import forms
from .models import Post, Event
from django.forms.widgets import Select, DateInput

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = Select(choices=self.get_time_choices())

    def get_time_choices(self):
        choices = []
        for hour in range(12):
            for minute in (0, 5, 10, 15):
                time = f"{hour:02d}:{minute:02d}"
                choices.append((time, time))
        return choices

class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EventAdminForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = Select(choices=self.get_time_choices())

    def get_time_choices(self):
        choices = []
        for hour in range(24):
            for minute in (0, 15, 30, 45):
                time = f"{hour:02d}:{minute:02d}"
                choices.append((time, time))
        return choices
