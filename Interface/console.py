from art import tprint
import art
from Management.library import LibraryManager
from Entity.user import User

class ConsoleRunner():
     
     page_titles = {
          "index":"| --- Navigate --- |",
          "main":"| Welcome - to - Library - Management | ",
          "login":"| ----\t\t Login \t\t---- |"
     }
     
     def __init__(self, library:LibraryManager) -> None:
          self.library = library
          self.session = None
          
     def start(self):
          self.print_divider(190)
          tprint(ConsoleRunner.page_titles["main"])
          self.print_divider(190)
          while(True):
               print("Option:")
               self.render_options(["Login","Register"])
               self.print_divider(190)
               print("Your Choice: ", end="")
               option = input()
               if(option=='1'):
                    self.render_login()
                    break
               elif(option=='2'):
                    self.render_register()
                    
     def render_login(self):
          self.print_divider(100)
          tprint(ConsoleRunner.page_titles["login"])
          self.print_divider(100)
          print("Username: ",end="")
          username = input()
          print("Password: ",end="")
          password = input()
          self.print_divider(110)
          
          user_auth = self.library.authenticate(username,password)
          
          #If user obejct is returned, the user exists
          if(user_auth is not None):
               ''' Dev
               self.open_index(user_auth)
               self.session = user_auth
               
               '''
          self.open_index()   
          
          # TODO
          
     def render_register(self):
          # TODO
          pass
     
     def render_index(self):
          inp = ''      
          tprint(ConsoleRunner.page_titles["index"])
          
          
          while(True):
               self.print_divider(110)
               self.render_options(["Profile", "Browse Books", "Check Out",
                    "Check in", "Logout"])
               self.print_divider(110)
               print("Your Choice: ", end='')
               inp = self.listen_input()
               if(inp == '1' or inp == '2' or inp == '3' or 
                inp == '4' or inp == '5'):
                    break
               self.print_divider(110)
               print("Invalid Option")
          if(inp=='1'):
               self.render_profile()
             
     def render_profile(self):
          tprint()
     
     #custom function to listen to an input
     def listen_input(self):
          #Exits the application
          inp = input()
          if(inp.lower()=='z'):
               exit()
          return inp
               
     # method to render the passed list of strings as options
     def render_options(self, options:list):
          for i in range(len(options)):
               print(f'{i+1}. {options[i]}')
          print("(Enter 'z' to exit the application)")
          
     def print_divider(self, count:int):
          print("*"*count)