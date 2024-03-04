from Entity.user import User
from Entity.user import Membership
from Entity.library import Library
from Entity.book import Book
from Entity.book import Collection
from Entity.admin import Admin
from Management.admin import Administration

class LibraryManager(Administration):
     
     '''A class that contains functions to carry out library functionality at the top level,
     extends the Library class'''
     def __init__(self) -> None:
          super().__init__()
          
     # authenticates the user based on username and password credentials
     def authenticate(self,username:str, password:str)->User:
          '''authenticates the user based on username and password credentials'''
          
          username_a = None
          
          #Linear searching users in the list of user registered
          for user in self.registered_users:
               user:User = (user)
               if(user.get_username()==username):
                    print("Successfully Logged In.")
                    username_a = user.get_username()
                    break
          #The username exists if passed check
          if username_a is not None:
               #extracting user from the dictionary
               if password==user.password:
                    self.validate_membership(user=user)
                    return user    #valid auth
          return None    #invalid auth
     

     #registers a passed user
     def register(self, user:User):
          '''registers a passed user'''
          
          u_id = len(self.registered_users)+1
          register_user = User(user.get_username(), user.get_password(),
               user.get_email(),u_id,user.get_membership(),
               user.get_registered_date()
          )
          self.registered_users.append(register_user)
     
     # A method to renew the membership of the user
     def renew_membership(self, user:User, type:str):
          '''method to renew the membership of the user'''
          
          user_l = self.get_user(user.username)
          if(type.upper()=="STUDENT"):
               user_l.set_renewal(Membership.STUDENT_MEMBER)
          elif(type.upper()=="YEARLY"):
               user_l.set_renewal(Membership.YEARLY_MEMBER)
          else:
               user_l.set_renewal(Membership.MONTHLY_MEMBER)
     
          return user_l.get_membership()
     
     # checks of the passed username is unique by searching the registered user list
     def username_is_valid(self, username:str)->bool:
          '''checks of the passed username is unique by searching the registered user list'''
          # linear searches the registered user list
          for user in self.registered_users:
               user:User = user
               if(user.get_username()==username):
                    return False
           
          # linear searches the registered admins  
          for admin in self.registered_admins:
               admin:Admin = admin
               if(admin.get_username()==username) :
                    return False
               
          return True
     
     # A method to return a base user
     def create_user_prof(self, username:str, password:str,
               membership_type:str,email:str):
          '''A method to return a base user'''
          return User(username, password,email,0, membership_type)
     
        
     # A method to check out from collection id
     def check_out(self, book:Book, user:User)->Book:
          '''
          returns 
          ((None, False))-> User membership is invalid
          ((bk , True))-> Book returned with true membership status
          ((None, True))-> No book found but membership status is valid
          '''
          
          collection_id = book.get_id()
          if(user.get_membership()==Membership.INVALID):
               return (None, False)
          collection = self.get_collection(collection_id)
          available = collection.get_avaliable()
          if(available>0):
               bk = collection.withdraw_book()
               user.check_out(bk)
               return (bk , True)
          return (None, True)
               

     def check_in(self, book_id:int,user:User):
          '''
          A method to check in the book based on the book id
          **bool
          >True:The book has been checked_out
          >False:The book does not exist in user's checked out list
          '''
          
          check_outs = user.get_checked_out()
     
          # A linear search to check if the book exists in the list of checked out books
          for book in check_outs:
               book:Book = book
               if(book["book_id"]==book_id):
                    break
          else:
               return False
               
          user.check_in(self.get_book(book_id))
          return True
          
          
     def get_all(self, entry:str)->tuple:
          
          '''
          Returns tuple 
          **(bool, list or Book)
          >(True, Book)
          >(False, list)
          '''
          
          b_id = None    #Book by collection id
          b_name = None  #Book by name List
          
          if(entry.isdigit()):
               num = int(entry)
               b_id = self.get_book_from_collection(num)
               
          b_name = self.get_books(entry)     #returns a book object with collection id
          
          if(len(b_name)==0 and (b_id is not None)):
               return (True, b_id)
          elif(len(b_name)==1 and (b_id is None)):
               return (True, b_name[0])
          elif(len(b_name)>1 and (b_id is None)):
               return (False, b_name)
          elif(len(b_name)>=1 and (b_id is not None)):
               b_name.append(b_id)
               return (False, b_name)
          else:
               return (False, None)
               
               
     def register_admin(self, admin:Admin):
          '''A method to register admin'''
          self.registered_admins.append(admin)
