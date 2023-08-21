from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from task_manager.models import Tag, Task


def index(request):
    """View function for the home page of the site."""
    task = Task.objects.all()
    tag = Tag.objects.all()
    context = {
        "task": task,
        "tag": tag,
    }
    return render(request, "task_manager/index.html", context=context)


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 2


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_manager:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_manager:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_manager:tag-list")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task_manager:index")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task_manager:index")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:index")


class TaskChangeStatusView(LoginRequiredMixin, View):
    # model = Task

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=self.kwargs["pk"])
        task.toggle_status()

        return redirect("task_manager:index")
