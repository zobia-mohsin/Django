from django.db import models

# Create your models here.


class Topic(models.Model):  # has two fields, one text and one with date
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # with string method you can return anything like text
    def __str__(self):
        return self.text  # returns name of topic
# anytime you make changes to model.py file:
# 1. py manage.py makemigrations
# 2. py manage.py migrate
