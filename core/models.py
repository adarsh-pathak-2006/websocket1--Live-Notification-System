from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    reciever=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    message=models.TextField()
    is_read=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reciever.username}--{self.title[:100]}"
