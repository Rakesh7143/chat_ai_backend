# models.py
from django.db import models
from django.contrib.auth.models import User

class chat_History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    prompt = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # user is nullable → guard it
        return self.user.username if self.user else "Anonymous"

    class Meta:
        db_table = "chat_history"


class category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.TextField(null=True, blank=True)
    prompt = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # there is no 'name' field → use 'category'
        return self.category or "Unnamed Category"

    class Meta:
        db_table = "category"
