b1 = {"book_name": "hindi", "author": "chotu","publication": 2002}
b2 = {"book_name": "english", "author": "aditya","publication": 2004}
b3 = {"book_name": "maths", "author": "raju","publication": 2002}
b4 = {"book_name": "dsa", "author": "pappu","publication": 2000}
books = [b1, b2, b3, b4]
def display_books():
    print("Available books:")
    for book in books:
        print(f"Book Name: {book['book_name']}, Author: {book['author']}, Publication Year: {book['publication']}")


        
