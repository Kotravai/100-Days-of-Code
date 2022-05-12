# import sqlite3
#
# db = sqlite3.connect("book-collection.db")
# cursor = db.cursor()

## creates new table named books with column headings mentioned in (); NO NULL = cannot be empty
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float(), unique=True, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

    def create_app(self):
        app = Flask(__name__)
        db.init_app(app)
        return app

# db.create_all()

# new_book = Book(id= 3, title="Harry ", author ="J.Rowling", rating= 9 )
# db.session.add(new_book)
# db.session.commit()
