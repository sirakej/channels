from django.forms import Form, ModelForm
from django import forms
from .models import Channel , Post


class CreateChannelForm(ModelForm):
    name = forms.CharField( required=True, widget=forms.TextInput())
    class Meta:
        model = Channel
        fields = ['name']


class CreateChatForm(ModelForm):
    message = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'write_msg','placeholder':'Type your message here'}))
    class Meta:
        model = Post
        fields = ['message']
