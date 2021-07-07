from flask import Flask, jsonify

books = [
    {
        "id": 1,
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "isbn": "1512379298"
    },
    {
        "id": 2,
        "title": "Lord of the Flies",
        "author": "William Golding",
        "isbn": "0399501487"
    }
]

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!"

@app.route("/library/v1.0/books", methods=["GET"])
def get_books():
    return jsonify({"books": books})

@app.route("/library/v1.0/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    result = {}
    for book in books:
        if book["id"] == book_id:
            result = jsonify({"book": book})
    return result

if __name__ == "__main__":
    app.run()