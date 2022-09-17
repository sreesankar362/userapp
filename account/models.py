from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="users")

    profile_pic = models.ImageField(upload_to="images", null=True, blank=True)
    bio = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True)
    options = (
        ("male", "male"),
        ("female", "female"),
        ("other", "other")
    )
    gender = models.CharField(max_length=12, choices=options, default="male")