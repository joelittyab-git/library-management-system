from Entity.user import User
from Entity.book import Collection
from Entity.book import Book
from datetime import datetime

class Library(object):
     
     '''
     :<list>:registered_users -> stores the list of registered users
     :<list>:registered_admins -> stores the list of registered admins
     :<list>:collections -> stores the list collections of books
     '''
     def __init__(self) -> None:
          self.registered_users = []
          self.registered_admins = []
          self.collections = []
          self.config = {}  
     
     def filter_book(self, name:str):
          books = []
          
     def add_collection(self, book:Book, count:int = 1):
          collection_id = len(self.collections) + 1
          collection = Collection(book,count,collection_id)
          self.collections.append(collection)
          
     # validates a user's membership based on the latest registered date
     def validate_membership(self,user:User):
          membership_type = user.get_membership()
          renewed_date = user.get_registered_date()
          
          # extracting date time infor of the current instance
          now = datetime.now()
          cur_month = now.month
          cur_day = now.day
          cur_year = now.year
          
          now = datetime.now()
          renewed_month = renewed_date.month
          renewed_day = renewed_date.day
          renewed_year = renewed_date.year
          
          # conditions to check if set membership validity according to the respective membership type
          if(membership_type==Library.Membership.STUDENT_MEMBER or
             membership_type==Library.Membership.YEARLY_MEMBER):
               if((cur_year>=renewed_year+2) or 
               (cur_year>renewed_year and cur_month>renewed_month
                  and cur_day>renewed_day)):
                    user.set_validity(False)
                    return
          elif(membership_type==Library.Membership.MONTHLY_MEMBER):
               if(cur_month>renewed_month
                  and cur_day>renewed_day):
                    user.set_validity(False)
                    return
               elif(cur_year>renewed_year and renewed_month!=12):
                    user.set_validity(False)
                    return          
               elif(renewed_month==12 and cur_month>1):
                    user.set_validity(False)
                    return
               
          user.set_validity(True)
          
     # returns a dictionary containing the data of the books in the library
     def get_books_data(self)->list:
          '''Blue print for the dictionary in the list
          {
               '<collection_id>':{
                    book_id:[]
                    title:...,
                    genre:[...],
                    author...,
                    published:...,
                    available:...
                    
               }
          }
          '''
          books_r = {}
          
          for collection in self.collections:
               collection:Collection = (collection)
               books_r[collection.id] = {
                    'book_id':[],
                    'title':collection.get_title(),
                    'genre':collection.get_genres(),
                    'author':collection.get_author(),
                    'published':collection.get_published(),
                    'available':collection.get_published()
               }
               
               books:list = collection.get_books()
               for book in books:
                    book:Book = book
                    books_r[collection.id]["book_id"].append(book.get_id())
               
          return books_r
          
     # A method to retun a books data
     def get_book_data(self,collection_id:int)->dict:
          collection = self.get_collection(collection_id)
          if(collection is None):return None
          return {
                    'title':collection.get_title(),
                    'genre':collection.get_genres(),
                    'author':collection.get_author(),
                    'published':collection.get_published(),
                    'available':collection.get_published()
               }
          
     def get_book(self, id:int)->Book:
          for collection in self.collections:
               books:Collection = collection
               for book in books.books:
                    book:Book = book
                    if(book.get_id()==id):
                         return book
          return None
     
     # method to return the collection by its id
     def get_collection(self, collection_id:int)->Collection:
          # linear searches the collection by its id
          for col in self.collections:
               col:Collection = (col)
               if(col.id==collection_id):
                    return col
               
          return None    #returns none if no collection is found
     
     '''
     return a <class 'list'> of tuple [(book, date checked out),...]
     for history
     '''
     def get_history_for(self, user:User)->list:
          history = user.get_history()
          return_list = []
          
          # loop to create a list
          for item in history:
               book_id = item["book_id"]
               check_out = str(item["datetime"])
               book = self.get_book(book_id)
               return_list.append((book,check_out))
               
          return return_list
     '''
     return a <class 'list'> of tuple [(book, date checked out),...]
     for pending list
     '''
     def get_pending_returns_for(self, user:User):
          pending = user.get_checked_out()
          return_list = []
          
          for item in pending:
               book_id = item["book_id"]
               check_out = str(item["datetime"])
               book = self.get_book(book_id)
               return_list.append((book,check_out))
               
          return return_list
          
          #loop to create a pending list
          
               
     # Checks out a specific book present in the library
     def check_out(self, book:Book, user:User):
          book.set_unavailable()
          user.check_out(book)
     
     #Class to define membership types
     class Membership:
          YEARLY_MEMBER = 'YEARLY'
          MONTHLY_MEMBER = 'MONTHLY'
          STUDENT_MEMBER = 'STUDENT'
          INVALID = 'INVALID'      #Expired membership
          