from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks"
    )

    class Meta:
        ordering = ["status", "-start_date"]

    def toggle_status(self):
        self.status = not self.status
        self.save()
