from Entity.user import User
from Entity.library import Library

class LibraryManager(Library):
     def __init__(self) -> None:
          super().__init__()
          
     # authenticates the user based on username and password credentials
     def authenticate(self,username:str, password:str)->User:
          username = None
          
          #Linear searching users in the list of user registered
          for user in self.registered_users:
               user = User(user)
               if(user.get_username()==username):
                    username = user.get_username()
                    break
          #The username exists if passed check
          if username is not None:
               #extracting user from the dictionary
               user = User(self.registered_users[user])
               if password==user.password:
                    self.validate_membership(user=user)
                    return user    #valid auth
          return None    #invalid auth