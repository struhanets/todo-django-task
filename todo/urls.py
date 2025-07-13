from django.urls import path

from todo.views import (
    TodoListView,
    TagsListView,
    TaskCreateView,
    TagsCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleView,
    TagsUpdateView,
    TagsDeleteView,
)

app_name = "todo"

urlpatterns = [
    path("", TodoListView.as_view(), name="tasks"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task-create/<int:pk>/task-togle/", TaskToggleView.as_view(), name="task-toggle"
    ),
    path("task-create/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task-create/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags-delete"),
]
