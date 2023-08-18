from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

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


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 2


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("my_app:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("my_app:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("my_app:tag-list")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("my_app:index")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("my_app:index")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("my_app:index")


class TaskChangeStatusView(LoginRequiredMixin, generic.DeleteView):
    model = Task

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=self.kwargs["pk"])
        if not task.status:
            task.status = True
        else:
            task.status = False

        return redirect("my_app:index")
