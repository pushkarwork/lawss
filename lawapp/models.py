from django.db import models

# Create your models here.


class Practise(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.firstname + " " + self.lastname
