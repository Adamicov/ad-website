from django.db import models
from security.models import User
from django.utils.timezone import now


class Ad(models.Model):
    title = models.CharField(max_length=80)
    CATEGORIES = (
        ('Electronics', 'Electronics'),
        ('Codes', 'Codes'),
        ('Subscriptions', 'Subscriptions'),
    )
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='upload/', default='download.svg' )
    entry_date = models.DateTimeField(default=now)
    bump_date = models.DateTimeField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
