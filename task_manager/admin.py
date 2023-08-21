from django.contrib import admin


from task_manager.models import Tag, Task

admin.site.register(Tag)
admin.site.register(Task)

