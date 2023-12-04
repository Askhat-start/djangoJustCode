# myscript.py

import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
django.setup()

from main.models import Author,Book


def main():

    author_jk_rowling = Author.objects.create(name='J.K Rowling')
    author_pushkin = Author.objects.create(name='Pushkin')
    author_abai = Author.objects.create(name='Abai')

    Book.objects.create(title='Harry Potter', author_id=author_jk_rowling)
    Book.objects.create(title='Harry Potter', author_id=author_jk_rowling)
    Book.objects.create(title='42 Black Words', author_id=author_abai)
    Book.objects.create(title='Running Grave', author_id=author_jk_rowling)
    Book.objects.create(title='Abai Way', author_id=author_abai)
    Book.objects.create(title='Eugene Onegin', author_id=author_pushkin)
    Book.objects.create(title='The Queen of Spades', author_id=author_pushkin)


    jk_books = Book.objects.filter(author_id=Author.objects.get(name='J.K Rowling'))
    for i in jk_books:
        print(i.title)


    def new_book(author_name:str, new_book:str):
        try:
            Book.objects.create(title=new_book, author_id=Author.objects.get(name=author_name))
        except:
            print(f"No {author_name} author in 'Author' table!")

    name = input('Enter Author: ')
    new_book_title = input(f'Enter title of new book for {name}: ')

    new_book(name, new_book_title)

if __name__ == "__main__":
    main()
