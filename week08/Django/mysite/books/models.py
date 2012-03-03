from django.db import models

class Book(models.Model):
    def __unicode__(self):
        return self.bookTitle
    bookTitle = models.CharField(max_length=200)

class Info(models.Model):
    def __unicode__(self):
	return self.book.bookTitle
    book = models.ForeignKey(Book)
    isbn = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

