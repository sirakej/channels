from .models import Channel, Post
from .forms import CreateChannelForm , CreateChatForm
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializer import createChatSerializer

# Create your views here.

def index(request):
    channels = Channel.objects.all()

    return render(request,'index.html',{'channels':channels} )

def channel(request):
    if request.method == 'POST':
        print("passed")
        form = CreateChannelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        print("failed")
        form = CreateChannelForm()
    return render(request, 'channel.html', {'form':form})


def chat(request, id):
    chats = Post.objects.filter(channel=id)
    if request.method == 'POST':
        print('pased')
        form = CreateChatForm(request.POST)
        if form.is_valid():
            print('valdjfj')
            user = request.user
            chan = Channel.objects.get(id=id)
            chatform = form.save(commit=False)
            chatform.created_by = user
            chatform.channel = chan
            chatform.save()
            return redirect('/post/'+str(id))
        else:
            form = CreateChatForm()
    else:
        form = CreateChannelForm()
        #chats = Post.objects.filter(channel=id)



    return render(request, 'post.html', {'form':form, 'chat':chats})

class IndexViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = createChatSerializer()
