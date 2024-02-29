from Entity.user import User
from Entity.book import Book

class Library(object):
     
     def __init__(self) -> None:
          self.registered_users = []
          self.registered_admins=[]
          self.books = []
          self.config = {}  
     
     def filter_book(self, name:str):
          books = []
          
     def validate_membership(self, user:User):
          membership_type = user.get_membership()
          
     #Class to define membership types
     class Membership:
          YEARLY_MEMBER = 'YEAR'
          MONTHLY_MEMBER = 'MONTH'
          STUDENT_MEMBER = 'STUDENT'
          INVALID = 'INVALID'      #Expired membership
          