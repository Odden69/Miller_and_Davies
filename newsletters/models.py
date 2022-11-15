from django.db import models


class NewsletterSubscriber(models.Model):
    email = models.EmailField()
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
