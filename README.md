# Personal Library Management System

Web-based personal library manager built with Python Flask and HTML. Add, remove, and view books in your collection. Duplicates are automatically removed.

## Features

- User Interface for managing your book collection
- Add, Remove and View the list of books to your library
- Automatic removal of duplicate entries

## Installation

1. **Prerequisites:** Ensure you have Python (version 3.x recommended) and pip (Python package installer) installed on your system. You can download them from https://www.python.org/downloads/.

2. **Clone the Repository:** Use git to clone this repository to your local machine:
```bash
  git clone https://<your_github_repository_url>.git
```

3. **Install Dependencies:** Navigate to the project directory and install required dependencies using pip:
```bash
  cd personal-library-management-system
  pip install Flask
```

## Usage Guide

1. **Run the Application:** Open a terminal in the project directory and execute the following command to start the application:
```bash
  python app.py
```

2. **Access the UI:** Once the application starts, open a web browser and navigate to http://127.0.0.1:5001/ (or localhost:5001/) to access the user interface.

3. **Manage Your Library:** Use the provided form to add new books to your library. Enter the book title and click the "Add Book" button. To remove a book, enter its title and click the "Remove Book" button. The book list will automatically update after adding or removing entries.

**Note:** Currently, the application does not persist book data after closing the browser. Future versions may offer database integration for permanent storage.

## Authors

- [Chaitany Chaudhary](https://github.com/ChaitanyChaudhary)
