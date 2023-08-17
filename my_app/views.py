from django.shortcuts import render
from my_app.models import Tag, Task


def index(request):
    """View function for the home page of the site."""
    task = Task.objects.all()
    tag = Tag.objects.all()
    context = {
        "task": task,
        "tag": tag,
    }
    return render(request, "my_app/index.html", context=context)

