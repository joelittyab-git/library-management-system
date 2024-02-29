from art import tprint
import art
from Management.library import LibraryManager
from Entity.user import User
from Entity.book import Book
import time
#TODO:DEV
from datetime import datetime

class ConsoleRunner():
     
     page_titles = {
          "index":"| --- Navigate --- |",
          "main":"| Welcome - to - Library - Management | ",
          "login":"| ----\t\t Login \t\t---- |",
          "history":f"{'History':^100}"
     }
     
     def __init__(self, library:LibraryManager) -> None:
          self.library = library
          '''
          TODO:DEV
          '''
          self.session = User('username', 'kunnuthara',
                              "email",1000,"YEARLY",datetime.now())
          
          book = Book("Cannon vol1","Joel1", 122,[Book.Genre.ADULT, Book.Genre.ADVENTURE], datetime.now())
          book2 = Book("Joel's Cannon vol2","Joel2", 123,[Book.Genre.COMEDY], datetime.now())
          book3 = Book("Joel's Cannon vols 3","Joel3", 124,[Book.Genre.FICTION, Book.Genre.ROMANCE], datetime.now())
          
          self.library.add_collection(book,4)
          self.library.add_collection(book2,3)
          self.library.add_collection(book3,5)
          
          print(self.library.get_books_data())
          
          book1_t = self.library.get_book(102)
          book3_t = self.library.get_book(101)
          book2_t = self.library.get_book(300)
          
          
          self.session.check_out(book1_t, book2_t, book3_t)
          # print(self.session.get_history())
     def start(self):
          self.print_divider(210)
          tprint(ConsoleRunner.page_titles["main"])
          self.print_divider(210)
          while(True):
               print("Option:")
               self.render_options(["Login","Register"])
               self.print_divider(210)
               print("Your Choice: ", end="")
               option = self.listen_input()
               if(option=='1'):
                    self.render_login()
                    break
               elif(option=='2'):
                    self.render_register()
                    
     def render_login(self):
          self.print_divider(200)
          title = ConsoleRunner.page_titles["login"]
          tprint(f"{title:^130}")
          self.print_divider(200)
          print("Username: ",end="")
          username = input()
          print("Password: ",end="")
          password = input()
          self.print_divider(200)
          
          user_auth = self.library.authenticate(username,password)
          
          #If user obejct is returned, the user exists
          if(user_auth is not None):
               ''' Dev
               self.open_index(user_auth)
               self.session = user_auth
               
               '''
          self.render_index()   
          
          # TODO
          
     def render_register(self):
          # TODO
          pass
     
     def render_index(self):
          inp = ''      
          title = ConsoleRunner.page_titles["index"]
          tprint(f"{title:^130}")
          
          
          while(True):
               self.print_divider(200)
               self.render_options(["Profile", "Browse Books", "Check Out",
                    "Check in", "Logout"])
               self.print_divider(200)
               print("Your Choice: ", end='')
               inp = self.listen_input()
               if(self.check_option_validity(5,inp)):
                    break
               self.print_divider(200)
               print("Invalid Option")
          if(inp=='1'):
               self.render_profile()
             
     def render_profile(self):
          option = ''
          
          self.print_divider(200)
          title = f"|-Welcome-back-{self.session.get_username()}-|"
          tprint(f"{title}")
          
          while(True):
               self.print_divider(200)
               self.render_options([
                    "Settings",
                    "History",
                    "Pending Returns",
                    "Go Back",
                    "Logout"
               ])
               self.print_divider(200)
               print("Your Choice: ", end="")
               option = self.listen_input()
               self.print_divider(200)
               
               if(self.check_option_validity(5,option)):
                    break
               print("Invalid Option")
          
          if(option=='2'):
               self.render_history()
          elif(option=='3'):
               self.render_pending_returns()
     
     def render_history(self):
          history = self.library.get_history_for(self.session)   #[(<Book>, checkedout:str),...]
          tprint(self.page_titles("history"))
          # table for rendering history
          print("-"*162)  
          print(f"|{'No.':<6}|{'Title':<30}|{'Author':<30}|{'Genre':<60}|{'Date and Time' :<30}|")
          print("-"*162)
          
          for i in range(len(history)):
               data = history[i]
               book:Book = data[0]
               date_time = data[1]
               print(f"|{i+1:<6}", end="")
               print(f"|{book.get_title() :<30}", end="")
               print(f"|{book.get_author() :<30}", end="")
               print(f"|{str(book.get_genres()) :<60}", end="")
               print(f"|{date_time:<30}|")
               
          print("-"*162)
          
          self.render_profile()
        
     def render_pending_returns(self):
          tprint(f"{'History':^100}")
                    
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
       
     # method to print a divider in the console for the desired length
     def print_divider(self, count:int):
          print("*"*count)
     
     # method to check if the options choosen by the user is valid
     def check_option_validity(self,count:int, input:str):
          try:
               var = int(input)
          except TypeError as e:
               return False
          if(not(var>=1 and var<=count)):
               return False
          return True