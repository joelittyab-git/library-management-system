from Entity.user import User
from Entity.user import Membership
from Entity.library import Library
from Entity.book import Book

class LibraryManager(Library):
     def __init__(self) -> None:
          super().__init__()
          
     # authenticates the user based on username and password credentials
     def authenticate(self,username:str, password:str)->User:
          username_a = None
          
          #Linear searching users in the list of user registered
          for user in self.registered_users:
               user:User = (user)
               if(user.get_username()==username):
                    print("correct username")
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
          u_id = len(self.registered_users)+1
          register_user = User(user.get_username(), user.get_password(),
               user.get_email(),u_id,user.get_membership(),
               user.get_registered_date()
          )
          self.registered_users.append(register_user)
     
     # A method to renew the membership of the user
     def renew_membership(self, user:User, type:str):
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
          # linear searches the registered user list
          for user in self.registered_users:
               user:User = user
               if(user.get_username()==username):
                    return False
               
          return True
     
     # A method to return a base user
     def create_user_prof(self, username:str, password:str,
               membership_type:str,email:str):
          return User(username, password,email,0, membership_type)
     
     # def check_out(self, entry:str , user: User):
          
     #      b_id = None
     #      b_name = None
          
     #      if(entry.isdigit()):
     #           num = int(entry)
     #           b_id = self.get_book(num)
          
     #      b_name_list = self.get_books(entry)
          
     #      if(len(b_name_list)==0 and b_id is not None):
     #           return super().
          

     '''
     Returns tuple 
     **(bool, list or Book)
     >(True, Book)
     >(False, list)
     '''
     def get_all(self, entry:str)->tuple:
          b_id = None    #Book by id (only 1)
          b_name = None  #Book by name List
          
          if(entry.isdigit()):
               num = int(entry)
               b_id = self.get_book(num)
               
          b_name = self.get_books(entry)
          
          
          if(len(b_name)==0 and (b_id is not None)):
               return (True, b_id)
          elif(len(b_name)==1 and (b_id is None)):
               return (True, b_name[0])
          elif(len(b_name)>1 and (b_id is None)):
               return (False, b_name)
          elif(len(b_name)>1 and (b_id is not None)):
               return (False, b_name.append(b_id))
          else:
               return (False, None)
               
     def withdraw_book(self, book:Book):
          # TODO:Implementations
          pass