from django import forms
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo.models import Task, Tag


class TodoListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "todo/task_create_form.html"
    success_url = reverse_lazy("todo:tasks")
    fields = ["content", "deadline", "status", "tags"]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["deadline"].widget = forms.DateInput(attrs={"type": "date"})
        return form


class TaskToggleView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.status = not task.status  # змінюємо статус на протилежний
        task.save()
        return redirect("todo:tasks")  # редірект на список або куди треба


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo/task_create_form.html"
    success_url = reverse_lazy("todo:tasks")
    fields = ["content", "deadline", "status", "tags"]


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:tasks")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "tags/tags.html"
    context_object_name = "tags"


class TagsCreateView(generic.CreateView):
    model = Tag
    template_name = "tags/tag_create_form.html"
    success_url = reverse_lazy("todo:tags")
    fields = [
        "name",
    ]


class TagsUpdateView(generic.UpdateView):
    model = Tag
    template_name = "tags/tag_create_form.html"
    success_url = reverse_lazy("todo:tags")
    fields = [
        "name",
    ]


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tags")
