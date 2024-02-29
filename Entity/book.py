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
     
     def __init__(self,title:str, author:str, book_id:int,
                  publish_date:datetime, genre_list:list):
          self.title = title
          self.author = author
          self.id = book_id
          self.publish_date = publish_date
          self.status = BookStatus.AVAILABLE
          if self._validate_genre(genre_list):self.genre_list = genre_list
          
          
          
     #A method to be called when the book is withdrawn
     def check_out(self):
          self.status = BookStatus.NOT_AVAILABLE
          
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
          
          
class BookStatus:
     AVAILABLE = "AVAILABLE"
     NOT_AVAILABLE = "NOT_AVAILABLE"
     EXTINCT = "EXTINCT"
     
