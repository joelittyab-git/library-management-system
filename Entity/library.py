from Entity.user import User
from Entity.book import Collection
from datetime import datetime

class Library(object):
     
     def __init__(self) -> None:
          self.registered_users = []
          self.registered_admins = []
          self.collections = []
          self.config = {}  
     
     def filter_book(self, name:str):
          books = []
          
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
          '''
          {
               '<collection_id>':{
                    title:...,
                    genre:[...],
                    author...,
                    published:...,
                    available:...
                    
               }
          }
          '''
          books = {}
          
          for collection in self.collections:
               collection = Collection(collection)
               books[collection.id] = {
                    'title':collection.get_title(),
                    'genre':collection.get_genres(),
                    'author':collection.get_author(),
                    'published':collection.get_published(),
                    'available':collection.get_published()
               }
               
          return books
          
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
     
     # method to return the collection by its id
     def get_collection(self, collection_id:int)->Collection:
          # linear searches the collection by its id
          for col in self.collections:
               col = Collection(col)
               if(col.id==collection_id):
                    return col
               
          return None    #returns none if no collection is found
          
     #Class to define membership types
     class Membership:
          YEARLY_MEMBER = 'YEARLY'
          MONTHLY_MEMBER = 'MONTHLY'
          STUDENT_MEMBER = 'STUDENT'
          INVALID = 'INVALID'      #Expired membership
          