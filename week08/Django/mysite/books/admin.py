from books.models import Book
from django.contrib import admin
from books.models import Info

class ChoiceInline(admin.TabularInline):
    model = Info
    extra = 1
 
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['bookTitle']})
     ]
    inlines = [ChoiceInline]
    

admin.site.register(Book, BookAdmin)

