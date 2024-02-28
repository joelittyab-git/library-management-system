from .book import Book
from datetime import datetime
from Entity.book import BookStatus
'''
A class that defines a model for user in a library and defines a users functionality to perform 
tasks in a library
'''
class User(object):
     
     YEARLY_MEMBER = 'YEAR'
     MONTHLY_MEMEBER = 'MONTH'
     STUDENT_MEMBER = 'STUDENT'
     
     '''
     :<str>:username -> stores the username of the user
     :<int>:id -> stores the user id of the user
     :<str>:email -> stores the email of the user
     :<dict>:history -> dictionary that stores the date time as the key and the book as the value
     :<str>:membership -> defines the type of membership user has registered
     :<dict>:checked_out -> defines the rented books, once the user rents a book, the book_id is appended to this dictionary <book_id : datetime>
     '''
     def __init__(self, username:str,password:str, email:str, 
                  user_id:int, membership:str):
          self.username = username
          self.id = user_id
          self.email = email
          self.password = password
          self.history = {}
          self.checked_out = {}
          
          if(membership==Membership.MONTHLY_MEMBER or membership==Membership.YEARLY_MEMBER or
             membership==Membership.STUDENT_MEMBER):
               self.membership = membership
          else:
               raise Exception("InvalidMembershipError")
          
     #method to add books to the history     
     def add_book_to_history(self, book:Book):
          self.history[str(datetime.now())] = book
     
     #method to take a book from library
     def check_out(self, book:Book):
          self.checked_out[book.id] = datetime.now()   #adding to checkout list
          book.status = BookStatus.NOT_AVAILABLE  #setting book status
     
     #method to return a book to the library
     def check_in(self, book:Book):
          self.checked_out.pop(book.id)
          


          
#Class to define membership types
class Membership:
     YEARLY_MEMBER = 'YEAR'
     MONTHLY_MEMBER = 'MONTH'
     STUDENT_MEMBER = 'STUDENT'