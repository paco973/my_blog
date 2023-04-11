from django.db import models


class NewsLetter(models.Model):
    email = models.EmailField(unique=True)
    abonnement = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
