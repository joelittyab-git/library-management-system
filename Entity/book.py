from datetime import datetime

class Book(object):
     '''
     :<str>:title -> stores the title of the book
     :<str>:author -> stores the name author of the book
     :<int>:id -> stores the id of the book
     :<datetime>:publish_date -> stores the date and time the book was published
     :<str:BookStatus>:status -> status of the book if it is available to lease
     :<list>:genre_list -> stores the list of genres of the book
     '''
     
     def __init__(self,title:str, author:str, book_id:int, genre_list:list,
                  publish_date:datetime = datetime.now()):
          self.title = title
          self.author = author
          self.id = book_id
          self.publish_date = publish_date
          self.status = BookStatus.AVAILABLE
          if self._validate_genre(genre_list)==True:
               self.genre_list = genre_list
          
          
          
     #A method to be called when the book is withdrawn
     def check_out(self):
          self.status = BookStatus.NOT_AVAILABLE
          
          
     def is_available(self)->bool:
          if(self.status==BookStatus.AVAILABLE):
               return True
          return False
          
     def set_availabale(self):
          self.status = BookStatus.AVAILABLE
     def set_unavailable(self):
          self.status = BookStatus.NOT_AVAILABLE
          
     def _validate_genre(self, genre_list:list)->bool:
          #validating genre list for valid genres
          for genre in genre_list:
               try:
                    obj = getattr(Book.Genre, str(genre).upper())     #gets the attribute of the passed class or raises an exception
               except AttributeError as e:
                    raise Exception("InvalidGenreError")
               
          return True
     
     def get_title(self)->str:
          return self.title
     def get_author(self)->str:
          return self.author
     def get_genres(self)->list:
          return self.genre_list
     def get_published(self)->datetime:
          return self.publish_date
     
     class Genre:
          FICTION = 'FICTION'
          BIOGRAPHY = 'BIOGRAPHY'
          COMEDY = 'COMEDY'
          HISTORICAL = 'HISTORICAL'
          ROMANCE = 'ROMANCE'
          THRILLER = 'THRILLER'
          KIDS = "KIDS"
          HORROR = 'HORROR'
          CRIME = 'CRIME'
          SCIENCE_AND_TECHNOLOGY = 'SCIENCE_AND_TECHNOLOGY'
          ADVENTURE = 'ADVENTURE'
          SPIRITUAL = 'SPIRITUAL'
          ADULT = 'ADULT'
          MAGAZINE = 'MAGAZINE'
          TRAVEL = 'TRAVEL'
          ART = 'ART'
          

class Collection(object):
     def __init__(self,book:Book, count:int, id:int) -> None:
          self.id = id
          self.books = []
          self.count = count
     
     def withdraw_book(self)->Book:
          for (book) in self.books:
               book = Book(book)
               if(book.is_available()):return book
          return None    #Returns none if no books are available
     
     def get_title(self):
          return Book(self.books[0]).get_title()
     def get_author(self)->str:
          return Book(self.books[0]).get_author()
     def get_genres(self)->list:
          return Book(self.books[0]).get_genres()
     def get_published(self)->datetime:
          return Book(self.books[0]).get_published()
     
     #returns the availble books in the current collection
     def get_avaliable(self)->int:
          a = 0
          for (book) in self.books:
               book = Book(book)
               if book.is_available():
                    a+=1
                    
          return a

class BookStatus:
     AVAILABLE = "AVAILABLE"
     NOT_AVAILABLE = "NOT_AVAILABLE"
     EXTINCT = "EXTINCT"
     
