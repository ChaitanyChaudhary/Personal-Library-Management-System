from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Library:
  def __init__(self):
    # Initialize with unique books
    self.books = list(set(['The 5 AM Club', 'Atomic Habits', 'Rich Dad Poor Dad']))

  def display_books(self):
    return self.books

  def add_book(self, book_title):
    # Add and remove duplicates efficiently
    self.books = list(set(self.books + [book_title]))
    return self.books

  def remove_book(self, book_title):
    if book_title in self.books:
      self.books.remove(book_title)
    return self.books

library = Library()  # Create a library instance


@app.route('/')
def index():
  books = library.display_books()
  return render_template('index.html', books=books)


@app.route('/add_book', methods=['POST'])
def add_book():
  book_title = request.form['book_title']
  library.add_book(book_title)
  books = library.display_books()
  book_list_html = generate_book_list_html(books)
  return jsonify({"book_list_html": book_list_html})


@app.route('/remove_book', methods=['POST'])
def remove_book():
  book_title = request.form['book_title']
  library.remove_book(book_title)
  books = library.display_books()
  book_list_html = generate_book_list_html(books)
  return jsonify({"book_list_html": book_list_html})


def generate_book_list_html(books):
  """Generates HTML string for the updated book list."""
  book_list_html = ""
  for book in books:
    book_list_html += f"<li class='list-group-item'>{book}</li>"
  return book_list_html


if __name__ == '__main__':
  app.run(debug=True, port=5001)
