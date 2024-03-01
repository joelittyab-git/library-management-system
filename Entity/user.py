from .book import Book
from datetime import datetime
from datetime import timedelta
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
                  user_id:int, membership:str = None,
                  registry_date=datetime.now()):
          self.username = username
          self.id = user_id
          self.email = email
          self.password = password
          self.history = []
          self.checked_out = []
          self.registered_date = registry_date
          if(membership==Membership.MONTHLY_MEMBER or membership==Membership.YEARLY_MEMBER or
             membership==Membership.STUDENT_MEMBER):
               self.membership = membership
          elif(membership is None):
               self.membership = Membership.INVALID
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
     def check_out(self, *args:Book):
          for book in args:
               self.checked_out.append({
                    "book_id":book.id,
                    "datetime":datetime.now()
               })   #adding to checkout list
               self.add_book_to_history(book)
          
               book.set_unavailable()  #setting book status
     
     #method to return a book to the library
     def check_in(self, *args:Book):
          
          for book in args:
               # linear searches the list and deletes the item from the list
               x = (len(self.checked_out))
               for i in range(x):
                    if(self.checked_out[i]["book_id"]==book.id):
                         del self.checked_out[i]  #deletes the book that has been checked in
                         break
                    
                    book.set_availabale()      #sets the book status back to available
     
     #A method to set the validity of a user's membership
     def set_validity(self,is_valid:bool):
          self.is_valid = is_valid
          if(is_valid is False):
               self.membership = Membership.INVALID
               return
          
     # returns the (day,month,year) the membership expires
     def get_membership_expiry(self)->tuple:
          renewed:datetime = self.registered_date
          exp:datetime = None
          
          #checks the membership type of the user
          if(self.get_membership()==Membership.YEARLY_MEMBER or 
             self.get_membership()==Membership.STUDENT_MEMBER):
               exp:datetime = renewed + timedelta(weeks=52)
          elif(self.get_membership()==Membership.MONTHLY_MEMBER):
               exp:datetime = renewed + timedelta(weeks=4)
          else: return None   #returns None if membership is expired
          
          return (exp.day, exp.month, exp.year)
     
     def set_renewal(self, type:str,dt:datetime = datetime.now()):
          self.registered_date = dt
          self.membership = type
          
     
     
     
     # getters
     def get_membership(self):
          return self.membership

     def get_registered_date(self):
          return self.registered_date
     
     def get_username(self)->str:
          return self.username
     
     def get_password(self)->str:
          return self.password
     
     def get_email(self)->str:
          return self.email
     
     def get_history(self)->list:
          return self.history

     def get_checked_out(self)->list:
          return self.checked_out

 #Class to define membership types
class Membership:
     YEARLY_MEMBER = 'YEARLY'
     MONTHLY_MEMBER = 'MONTHLY'
     STUDENT_MEMBER = 'STUDENT'
     INVALID = 'INVALID'      #Expired membership