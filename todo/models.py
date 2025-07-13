from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    status = models.BooleanField(default=False, help_text="Виконано?")
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return f"{self.content[:20]}... (Deadline: {self.deadline})"

    class Meta:
        ordering = ["-status"]


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
