from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):
    post = models.TextField(max_length=800)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    posted_date = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User)

    def liked_users(self):
        liked_users = self.liked_by.all()
        users = [user for user in liked_users]
        return users

    def __str__(self):
        return self.post