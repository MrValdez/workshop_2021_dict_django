from django.contrib import admin

from . import models


#@admin.register(models.User)
#class UserAdmin(admin.ModelAdmin):
#    pass

@admin.register(models.Post)                # decorators (python feature)
class PostsAdmin(admin.ModelAdmin):
    pass


#admin.site.register(models.Post, PostsAdmin)