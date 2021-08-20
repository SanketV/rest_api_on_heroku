from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

booksArr = [
    {
        "id": 1,
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "isbn": "111"
    },
    {
        "id": 2,
        "title": "The Choice",
        "author": "Edith Eger",
        "isbn": "222"
    },
    {
        "id": 3,
        "title": "A Tree Grows in Brooklyn",
        "author": "Betty Smith",
        "isbn": "333"
    },
    {
        "id": 4,
        "title": "If only he knew",
        "author": "Gary Smalley",
        "isbn": "444"
    },
    {
        "id": 5,
        "title": "Matilda",
        "author": "Roald Dahl",
        "isbn": "555"
    },
    {
        "id": 6,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "isbn": "666"
    },
    {
        "id": 7,
        "title": "Charlotte's Webb",
        "author": "E.B. White",
        "isbn": "777"
    }
]

app = Flask(__name__)

ENV = 'PROD'

if ENV == 'dev':
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/ApnaDB101'
    app.debug = True
else:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://auoiprnvtnalbh:2baa9acd5b82e85631a8bbdeeb6f1829911a8029cd3ae0cbd6307138a62d0287@ec2-3-218-149-60.compute-1.amazonaws.com:5432/dfatnsjk7odsmv'
    app.debug = False

db = SQLAlchemy(app)

class books(db.Model):
    __tablename__ = 'books'
    bookid = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(300), nullable = False)
    authors = db.Column(db.String(200), nullable = False)
    average_rating = db.Column(db.Integer())
    isbn = db.Column(db.Integer())
    language_code = db.Column(db.String(3))
    num_pages = db.Column(db.Integer())
    ratings_count = db.Column(db.Integer())
    text_reviews_count = db.Column(db.Integer())
    publication_date = db.Column(db.Date())
    publisher = db.Column(db.String(100))

    def __init__(self, bookid, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date, publisher):
        self.bookid = bookid
        self.title = title
        self.authors = authors
        self.average_rating = average_rating
        self.isbn = isbn
        self.isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = num_pages
        self.ratings_count = ratings_count
        self.text_reviews_count = text_reviews_count
        self.publication_date = publication_date
        self.publisher = publisher

@app.route("/")
def index():
    return "Hola Mundo!"

@app.route("/library/v1.0/books", methods=["GET"])
def get_books():
    return jsonify({"books": booksArr})

@app.route("/library/v1.0/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    result = {}
    for bk in booksArr:
        if bk["id"] == book_id:
            result = jsonify({"book": bk})
    return result


# ApnaDB01 - REST endpoints from postgres database
@app.route("/library/v2.0/books", methods=["GET"])
def get_books_db():
    bookList = books.query.all()
    result = []
    for book in bookList:
        currBook = {}
        currBook['id'] = book.bookid
        currBook['title'] = book.title
        currBook['authors'] = book.authors
        currBook['average_rating'] = book.average_rating
        currBook['isbn'] = book.isbn
        currBook['publication_date'] = book.publication_date
        result.append(currBook)
        print('• ' + str(currBook))

    return jsonify({"books": result})


if __name__ == "__main__":
    app.run()