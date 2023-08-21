from django.urls import path

from task_manager.views import (
    index,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskChangeStatusView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "<int:pk>/change/",
        TaskChangeStatusView.as_view(),
        name="change-status"
    ),
]

app_name = "task_manager"
