import os
import csv
import shutil


# Save All List/Directory Data Into A Created File
def sfile(books_list):
    if not os.path.exists("Books"):
        os.mkdir("Books")

    # create a TXT file in given path
    # with open('Books/Record_file', "w") as Record_file:  # Open the file in 'w' mode to overwrite it
    #     # Save All List/Directory Data Into A Given File
    #     RF = "\n".join(books_list)
    #     Record_file.write(RF)
    # print("Data saved to file successfully!")

    # Create a CSV file in the given path
    with open('Books/Record_file.csv', "w") as Record_file:
        # Save All List/Directory Data Into A Given File
        fields = ['Books Name']
        Record_file_writer = csv.writer(Record_file)

        # Write the header row
        Record_file_writer.writerow(fields)

        # Write the data from the books_list
        for book in books_list:
            Record_file_writer.writerow([book])
    print("Data saved to file successfully!")


# Remove Duplicate Elements
def Duplicates_File():
    unique = set(l.books)
    l.books = list(unique)
    return l.books


AllBooks = ['The 5 AM Club', 'Atomic Habits', 'Rich Dad, Poor Dad']


class library:
    def __init__(self):
        self.books = list(set(AllBooks))

    # Display Books
    def display_books(self):
        print(
            f"\nCurrently {len(self.books)} Books Available In Library\n\n{self.books}\n\nNote: Duplicate books are automatically removed from the list.\n")
        Duplicates_File()

    # Add Books
    def add_books(self):
        self.display_books()
        a = input("\nEnter The Name Of The Book You Want To Add: ")
        self.books.append(a)
        print(f"\n{Duplicates_File()}\n\nYour Book {a} Added Successfully")
        sfile(self.books)

    # Remove Books
    def remove_books(self):
        self.display_books()
        b = input("\nEnter The Name Of The Book You Want To Remove: ")
        self.books.remove(b)
        print(f"\n{Duplicates_File()}\n\nYour Book '{b}' Removed Successfully")

        # Save changes to file
        sfile(self.books)


l = library()
sfile(l.books)
print("\nWelcom To My Library\n")

# Create A Loop To Contue This Peocess!

while True:
    print("\n1 Books Available In Library \n2 The Books You Want To Add \n3 The Books You Want To Remove ")
    d = int(input("Select Your Options(1, 2 & 3): "))

    if d == 1:
        l.display_books()
    elif d == 2:
        l.add_books()
    elif d == 3:
        l.remove_books()

    E = input("If You Want To Continue Press c And For Quit Press q: ")
    if E == 'q':
        if os.path.exists("Books/Record_file"):
            os.remove("Books/Record_file")
        if os.path.exists("Books"):
            shutil.rmtree("Books")
            # os.rmdir("Books")
            print("Books directory has been removed successfully.")
        break
