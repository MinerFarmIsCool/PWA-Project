from django.db import models
from django.utils import timezone

class Task(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the task name.")
    completed = models.BooleanField(default=False, help_text="Is the task completed?")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The time when the task was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The time when the task was last updated.")
    description = models.CharField(max_length=1000, help_text="Enter the task description.", default="None")

    def __str__(self):
        return f"{self.name}, (Completed: {self.completed}), Description: {self.description}"