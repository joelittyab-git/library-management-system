from art import tprint
import art
from Management.library import LibraryManager
from Entity.user import User

class ConsoleRunner():
     def __init__(self, library:LibraryManager) -> None:
          self.library = library
          
     def start(self):
          print("*"*190)
          tprint("| Welcome - to - Library - Management | ")
          print("*"*190)
          while(True):
               print("Option:")
               print("1.Login")
               print("2.Register")
               print("*"*190)
               print("Your Choice: ", end="")
               option = input()
               if(option=='1'):
                    self.prompt_login()
                    break
               elif(option=='2'):
                    self.prompt_register()
                    
     def prompt_login(self):
          print("*"*100)
          tprint("| ----\t\t Login \t\t---- |")
          print("*"*100)
          print("Username: ",end="")
          username = input()
          print("Password: ",end="")
          password = input()
          
          user_auth = self.library.authenticate(username,password)
          
          #If user obejct is returned, the user exists
          if(user_auth is not None):
               self.open_index(user_auth)
          
     def prompt_register(self):
          pass
     
     def open_index(self, user_authenticated:User):
          pass