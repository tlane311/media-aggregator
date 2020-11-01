from django.contrib import admin
from .models import Communities, Users, Threads, Comments

# Register your models here.
admin.site.register(Communities)
admin.site.register(Users)
admin.site.register(Threads)
admin.site.register(Comments)