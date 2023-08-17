from django.contrib import admin


from my_app.models import Tag, Task

admin.site.register(Tag)
admin.site.register(Task)

