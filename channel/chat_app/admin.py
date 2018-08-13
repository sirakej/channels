from django.contrib import admin
from .models import Channel
from .models import Post

# Register your models here.
admin.site.register(Channel)
admin.site.register(Post)
