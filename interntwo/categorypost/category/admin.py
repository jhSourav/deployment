from django.contrib import admin
from .models import Posts,PostType
# Register your models here.

admin.site.register(PostType)
admin.site.register(Posts)