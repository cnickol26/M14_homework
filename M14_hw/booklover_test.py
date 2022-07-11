import pandas as pd
import numpy as np
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        book = BookLover("Connor","can2hr","fiction")
        book.add_book("Harry Potter",5)
        print(book.book_list)
        
        book_test = "Harry Potter"
        self.assertEqual(book_test,book.book_list["book_name"].values)
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book = BookLover("Connor","can2hr","fiction")
        book.add_book("Harry Potter",5)
        book.add_book("Harry Potter",5)
        print(book.book_list)

        book_test = "Harry Potter"
        self.assertEqual(book_test,book.book_list["book_name"].values)
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book = BookLover("Connor","can2hr","fiction")
        book.add_book("Harry Potter",5)
        print(book.has_read("Harry Potter"))

        self.assertTrue(book.has_read("Harry Potter"))

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book = BookLover("Connor","can2hr","fiction")
        book.add_book("Harry Potter",5)
        print(book.add_book)

        self.assertFalse(book.add_book("Harry Potter",5))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book = BookLover("Connor","can2hr","fiction")
        book.add_book("Harry Potter",5)
        book.add_book("Death on the Nile",3)
        book.add_book("Wizard School",4)
        book.add_book("Harry Potter",5)
        print(book.book_list)

        expected = 3
        self.assertEqual(book.num_books,expected)
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book = BookLover("Connor","can2hr","fiction")
        book.add_book("Harry Potter",5)
        book.add_book("Death on the Nile",3)
        book.add_book("Wizard School",4)
        print(book.fav_books())

        self.assertEqual(sum(book.book_list["book_rating"].values > 3),2)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
