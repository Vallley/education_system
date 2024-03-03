from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=300)
    start_time = models.DateTimeField()
    cost = models.IntegerField()
    min_group = models.IntegerField()
    max_group = models.IntegerField()
    
    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=100)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Groups(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    users = models.ManyToManyField(Users)

    def __str__(self):
        return self.name


        



