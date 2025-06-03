from django.db import models

from users.models import User

from diary import settings


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50, blank = False)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notes', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add= True)


    class Meta:
        ordering = ['date_created']


    def __str__(self):
        return self.title