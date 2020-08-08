from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):             #to tell django how to find url of any specific instance of a post
        return reverse('post-detail', kwargs={'pk': self.pk})          #redirect actually redirect you to a specific route but reverse will simply return the full url to that route as a string
                                                                       #here we want to get the path to post details and the primary key would be itself
