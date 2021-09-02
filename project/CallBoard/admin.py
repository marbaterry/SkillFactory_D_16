from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Response)
admin.site.register(Post)
admin.site.register(CreateResponse)
admin.site.register(Comment)