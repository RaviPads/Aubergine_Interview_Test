from django.db import models
from django.contrib.auth.models import User


# Image Model which has basic information Full Path, Short Path.

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    full_path = models.URLField(verbose_name="Image Full Path")
    short_path = models.URLField(verbose_name="Image Short Path")
    create_date = models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name="Record Create Date")
    update_date = models.DateTimeField(auto_created=True, auto_now=True, verbose_name="Last Update Date")

    def __str__(self):
        return str(self.user) + " | " + str(self.short_path)
