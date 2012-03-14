from books.models import Book
from django.contrib import admin
from books.models import Info

class ChoiceInline(admin.TabularInline):
    model = Info
    extra = 1
 
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['bookTitle']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
     ]
    inlines = [ChoiceInline]
    list_display = ('bookTitle', 'pub_date', 'was_published_today')
    search_fields = ['bookTitle']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date' 

admin.site.register(Book, BookAdmin)

