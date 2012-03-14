from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from books.models import Book
from books.models import Info

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Book.objects.order_by('-pub_date')[:5],
            #context_object_name='latest_book_list',
            template_name='books/index.html')),
    url(r'^$',
        ListView.as_view(   
	    model = Book, 
	    queryset=Book.objects.order_by('bookTitle')[:5],
            template_name='books/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Info,
            template_name='books/detail.html')),
)


