from .book import Book
from datetime import datetime
from Entity.book import BookStatus
from Entity.library  import Library
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
     :<list:dict>:history -> list that stores book id and date and time the book has been taken { "book_id":..., "datetime":...}
     :<str>:membership -> defines the type of membership user has registered
     :<list:dict>:checked_out -> defines the rented books, once the user rents a book, the book_id is appended to this list <book_id : datetime> 
          { "book_id":..., "datetime":...}
     <datetime>:registered_date -> defines the date and time the  user has registered or has renewed his membership
     '''
     def __init__(self, username:str,password:str, email:str, 
                  user_id:int, membership:str, registry_date=datetime.now()):
          self.username = username
          self.id = user_id
          self.email = email
          self.password = password
          self.history = []
          self.checked_out = []
          self.registered_date = registry_date
          if(membership==Library.Membership.MONTHLY_MEMBER or membership==Library.Membership.YEARLY_MEMBER or
             membership==Library.Membership.STUDENT_MEMBER):
               self.membership = membership
          else:
               raise Exception("InvalidMembershipError")
          
          
          # TODO
          self.transactions = []
          self.is_valid = True
          
     #method to add books to the history     
     def add_book_to_history(self, book:Book):
          # appends a dictionary object into the list
          self.history.append({
                    "book_id":book.id,
                    "datetime":datetime.now()
               })
     
     #method to take a book from library
     def check_out(self, book:Book):
          self.checked_out.append({
               "book_id":book.id,
               "datetime":datetime.now()
          })   #adding to checkout list
          
          book.set_unavailable()  #setting book status
     
     #method to return a book to the library
     def check_in(self, book:Book):
          
          # linear searches the list and deletes the item from the list
          x = (len(self.checked_out))
          for i in range(x):
               if(self.checked_out[i]["book_id"]==book.id):
                    del self.checked_out[i]  #deletes the book that has been checked in
                    break
               
          book.set_availabale()      #sets the book status back to available
     
     # getters
     def get_membership(self):
          return self.membership
