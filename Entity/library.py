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
          # extracting date time info of the current instance
          now = datetime.now()          
          dmy = user.get_membership_expiry()
          
          #already set expired
          if(dmy is None):
               user.set_validity(False)
               return
          #checks if its valid
          else:
               day = dmy[0]
               month = dmy[1]
               year = dmy[2]
               
               exp = datetime(year,month,day)
               
               if(now>exp):
                    user.set_validity(False)
               else:
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
          
          # traverses the collections list for book data
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
               
               #  adds the id's of the books in the collection of current itteration
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
     # A method to searhc for user based on username
     def get_user(self,username:str):
          # Linear searches the user list
          for user in self.registered_users:
               user:User = user
               if(user.get_username()==username):
                    return user
          return None
     
     #A method that returns the book by name with the collectio id
     def get_books(self, name:str)->list:
          return_list = []
          
          for collect in self.collections:
               collect:Collection = collect
               if(collect.get_title().lower().strip()
                  == name.lower().strip()):
                    b =  Book(collect.get_title(), collect.get_author(),
                         collect.get_id(), collect.get_genres(),
                         collect.get_published())
                    return_list.append(b)
                    
          return return_list
                    
     def get_available(self, name:str)->list:
          pass
     
     # returns a book for specified id
     def get_book(self, id:int)->Book:
          
          # attempts linear search
          for collection in self.collections:
               books:Collection = collection
               for book in books.books:
                    book:Book = book
                    if(book.get_id()==id):
                         return book
          return None    #returns None if attempt failed
     
     # Returns book with collection id from collection_id
     def get_book_from_collection(self, collection_id:int)->Book:
          for collection in self.collections:
               collection:Collection = collection
               if(collection.get_id()==collection_id):
                    return Book(collection.get_title(), collection.get_author(),
                         collection.get_id(),collection.get_genres(),
                         collection.get_published())
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
     def get_checkouts_for(self, user:User):
          pending = user.get_checked_out()
          return_list = []
          
          #loop to create a pending list
          for item in pending:
               book_id = item["book_id"]
               check_out = str(item["datetime"])
               book = self.get_book(book_id)
               return_list.append((book,check_out))
               
          return return_list
                  
               
     # Checks out a specific book present in the library
     def check_out(self, book:Book, user:User):
          book.set_unavailable()
          user.check_out(book)
     
     def check_out(self, book_id:int, user:User):
          pass #TODO
     
     #Class to define membership types
     class Membership:
          YEARLY_MEMBER = 'YEARLY'
          MONTHLY_MEMBER = 'MONTHLY'
          STUDENT_MEMBER = 'STUDENT'
          INVALID = 'INVALID'      #Expired membership
          