"""This is how we build a form"""
from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        # the form should be based on the Topic model
        model = Topic
        # it should include the 'text' field from Topic
        fields = ['text']
        # the empty string '', tells django not to generate a label for the text field
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}