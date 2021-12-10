from django import forms

from .models import Topic, Entry
#allows use to use models as forms and change the appearance of it
class TopicForm(forms.ModelForm):
    class Meta: #subclass of TopicForm, do not need meta class if creating from scratch and not database
        model =  Topic #case sensitive
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model =  Entry #case sensitive
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text':forms.Textarea(attrs={'colgs':80})}