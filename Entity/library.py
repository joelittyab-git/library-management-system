from Entity.user import User
from Entity.book import Book

class Library(object):
     def __init__(self) -> None:
          self.registered_users = {}
          self.registered_admins={}
          self.books = {}
          self.config = {}
          
     
     def filter_book(self, name:str):
          books = []
          
          