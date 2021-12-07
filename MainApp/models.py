from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):  # has two fields, one text and one with date
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #migrate!!
    # with string method you can return anything like text
    def __str__(self):
        return self.text  # returns name of topic
# anytime you make changes to model.py file:
# 1. py manage.py makemigrations
# 2. py manage.py migrate
# 3. register - admin.py
class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    #this means show text attribute of object in website which is why topc.text was not needed in topics.html
    def __str__(self):
        return f"{self.text[:50]}..." #print statment, returning back text but only first 50 characters with ...
