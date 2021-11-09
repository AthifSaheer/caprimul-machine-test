from django.db import models

class Todo(models.Model):
    text = models.TextField(max_length=100)
    done = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)