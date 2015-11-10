from django.db import models

class Author(models.Model):
    AuthorID = models.CharField(max_length = 10)
    Name = models.CharField(max_length=50)
    Age = models.DateField(max_length=30)
    Sex = models.BooleanField(default=True)
    Country = models.CharField(max_length=30)

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    Title = models.CharField(max_length=50)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=50)
    PublishDate = models.DateField(max_length=30)
    Price = models.CharField(max_length=30)