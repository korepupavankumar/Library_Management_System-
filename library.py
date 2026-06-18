BOOKS_FILE = "books.txt"
ISSUED_FILE = "issued.txt"


def add_book():
    book = input("Enter Book Name: ")

    with open(BOOKS_FILE, "r") as file:
        books = [b.strip().lower() for b in file]

    if book.lower() in books:
        print("Book Already Exists!")
        return

    with open(BOOKS_FILE, "a") as file:
        file.write(book + "\n")
        print("\n",book)

    print("Book Added Successfully!")


def view_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            books = file.readlines()

        if not books:
            print("No Books Available")
            return

        print("\nAvailable Books")
        print("----------------")

        for num, book in enumerate(books, 1):
            print(f"{num}. {book.strip()}")

    except FileNotFoundError:
        print("Book file not found.")


def search_book():
    name = input("Enter Book Name: ").lower()

    with open(BOOKS_FILE, "r") as file:
        books = file.readlines()

    found = False

    for book in books:
        if name in book.lower():
            print("Book Found:", book.strip())
            found = True

    if not found:
        print("Book Not Found")


def issue_book():
    name = input("Enter Book Name to Issue: ")

    with open(BOOKS_FILE, "r") as file:
        books = file.readlines()

    found = False

    with open(BOOKS_FILE, "w") as file:
        for book in books:
            if book.strip().lower() == name.lower():
                found = True

                with open(ISSUED_FILE, "a") as issue:
                    issue.write(book)

            else:
                file.write(book)

    if found:
        print("Book Issued Successfully")
    else:
        print("Book Not Available")


def return_book():
    name = input("Enter Book Name to Return: ")

    with open(ISSUED_FILE, "r") as file:
        books = file.readlines()

    found = False

    with open(ISSUED_FILE, "w") as file:
        for book in books:
            if book.strip().lower() == name.lower():
                found = True

                with open(BOOKS_FILE, "a") as available:
                    available.write(book)

            else:
                file.write(book)

    if found:
        print("Book Returned Successfully")
    else:
        print("Book Was Not Issued")


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")