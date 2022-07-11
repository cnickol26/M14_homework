import pandas as pd
import numpy as np

class BookLover:

    def __init__(self,name,email,fav_genre,num_books = 0,
                book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self,book_name,book_rating):
        if book_name in self.book_list.book_name.values:
            print("That book is already in the list")
        else:   
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [book_rating]
            })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            
    def has_read(self,book_name):
        if book_name in self.book_list.book_name.values:
            return True
        else:
            return False
    
    def num_books_read(self):
        return self.book_list.shape[0]
    
    def fav_books(self):
        best_books = self.book_list.loc[self.book_list["book_rating"] > 3, :]
        return best_books