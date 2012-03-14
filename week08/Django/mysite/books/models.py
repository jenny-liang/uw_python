from django.db import models
import datetime

class Book(models.Model):
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
    
    def __unicode__(self):
        return self.bookTitle
    bookTitle = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Info(models.Model):
    def __unicode__(self):
	return "Book Info"
    book = models.ForeignKey(Book)
    isbn = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

