from django.db import models

class Person(models.Model):
    name = models. CharField(max_length=50)
    age = models.ImageField()
    position = models.CharField(max_length=30)
    city=models.CharField(max_length=10)
    image = models. TextField(max_length=2000)


    def __str__(self):
        return self.name

