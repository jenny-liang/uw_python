"""
Minimal Flask + forms demo

Send HTML page that echoes message from HTTP request
To get started, point browser at echo_flask.html
"""

from flask import Flask, request
import bookdb

# no need for template here - just a constant string

BOOK_TITLE_LINE="""<html>
<head><title>Books</title></head>
<body>
%s
</body>
</html>
"""

BOOK_INFO_LINE = """
<html>
<head>
<title>%s</title>
</head>
<body>
%s
</body>
</html>
"""

# No need for message page
# Flask converts view function return string to HTML page

app = Flask(__name__)

app.debug = True # development only - remove on production machines
bookDb = bookdb.BookDB()
# View functions generate HTTP responses including HTML pages and headers

@app.route('/book_pages.py') #decorate another view function.
def message_page():
    # Flask Quickstart suggests request.form should work, but here it is empty
    # Flask converts return string to HTML page
    #return 'Message: %s' % request.args['message']  # args is a dictionary. 'message' is the key.
    bookTitle = []
    bookTitleLines = ''
    for titleDict in bookDb.titles():
        title = titleDict['title']
        bookTitle.append(title)
    for b in bookTitle:
        bookTitleLines = bookTitleLines + "<a href='%s'>%s</a>" %(b, b) + "\n<br>"
    return bookTitleLines

@app.route('/<bookTitle>')
def show_user_profile(bookTitle):
    info = ''
    for titleDict in bookDb.titles():
        if titleDict['title'] == bookTitle:
            id = titleDict['id']
            bookInfoDict = bookDb.title_info(id)
            for key in bookInfoDict:
               info = info + key + ":" + bookInfoDict[key] + '<br>\n'
    return BOOK_INFO_LINE % (bookTitle, info)

# No function needed for other routes - Flask will send 404 page

if __name__ == '__main__':
    app.run()

