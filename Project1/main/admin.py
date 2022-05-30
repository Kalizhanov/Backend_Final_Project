from django.contrib import admin
from .models import History, Mgp, Tradition, Registration,Presidents


admin.site.register(History)
admin.site.register(Mgp)
admin.site.register(Tradition)
admin.site.register(Registration)

class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}  

admin.site.register(Presidents, PostsAdmin)