from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Form(models.Model):
    title = models.CharField(max_length=50)
    jsonForm = models.CharField(max_length=100000)
    publishedDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title


class FormSubmission(models.Model):
    form = models.ForeignKey(Form)
    jsonSubmission = models.CharField(max_length=100000)
    publishedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.form.title + " submission"
