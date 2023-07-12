from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book.db"
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    genre = db.Column(db.String(64))
    subgenre = db.Column(db.String(64))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name}, {self.genre}, {self.subgenre}"

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    genre = request.form['genre']
    subgenre = request.form['subgenre']
    price = request.form['price']
    flag = request.form['flag']
    new_book = Book(name=name,genre=genre,subgenre=subgenre,price=price)
    try:
        db.session.add(new_book) 
        db.session.commit()
        return render_template('confirmation.html',flag=flag)
    except Exception as e:
        return str(e)
    
@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@app.route('/delete-book/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    try:
        db.session.delete(book)
        db.session.commit()
        return render_template('confirmation.html',flag="D")
    except Exception as e:
        return str(e)
    
@app.route('/update-book/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        # Update book details
        try:
            book.name = request.form['name']
            book.genre = request.form['genre']
            book.subgenre = request.form['subgenre']
            book.price = request.form['price']
            db.session.commit()
            return render_template('confirmation.html',flag="U")
        except Exception as e:
            return str(e)
    else:
        # Display update form
        return render_template('update_book.html', book=book)


if __name__=='__main__':
    app.run(debug=True,port=10000)