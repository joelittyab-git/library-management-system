from art import tprint
from Management.library import LibraryManager
from Entity.book import Collection
from Entity.user import User
from Entity.book import Book
from Entity.user import Membership

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
          # self.session = User('1', '1',
          #                     "email",1000,"MONTHLY",datetime(2021,2,2))
          self.session:User = None
          
          book = Book("Cannon vol1","Joel1", 122,[Book.Genre.ADULT, Book.Genre.ADVENTURE], datetime.now())
          book2 = Book("Joel's Cannon vol2","Joel2", 123,[Book.Genre.COMEDY], datetime.now())
          book3 = Book("Joel's Cannon vols 3","Joel3", 124,[Book.Genre.FICTION, Book.Genre.ROMANCE], datetime.now())
          book4 = Book("1","Joel4", 124,[Book.Genre.HORROR, Book.Genre.HISTORICAL], datetime.now())
          
          self.library.add_collection(book,4)
          self.library.add_collection(book2,3)
          self.library.add_collection(book3,5)
          self.library.add_collection(book4,1)
          
          
          user = User('1','1','email@gmail.com',1000, "MONTHLY", datetime(2021,2,2))
          self.library.register(user)
          
          print(self.library.get_books_data())

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
     # A method to render the login page             
     def render_login(self):
          self.print_divider(200)
          title = ConsoleRunner.page_titles["login"]
          tprint(f"{title:^130}")
          self.print_divider(200)
          print("Username: ",end="")
          username = input().strip()
          print("Password: ",end="")
          password = input().strip()
          self.print_divider(200)
          
          user_auth = self.library.authenticate(username,password)    #user authentication
          admin_auth = self.library.authenticate_admin(username, password)     #admin authentication
          #If user obejct is returned, the user exists
          if(user_auth is not None):
               self.session = user_auth
               # book1_t = self.library.get_book(102)    #TODO:DEV
               # book3_t = self.library.get_book(101)    #TODO:DEV
               # book2_t = self.library.get_book(300)    #TODO:DEV
               # self.session.check_out(book1_t, book2_t, book3_t) #TODO:DEV
               return self.render_index()
          elif(admin_auth is not None):
               self.session = admin_auth
               return self.render_admin_page() 
          print("Invalid username or password")
          return self.start()
     
     def render_admin_page(self):
          self.print_divider(236)
          tprint(f"|{'Administration':^160}|")
          self.print_divider(236)
          
          print("Choose an option:")
          self.render_options(["Add Book", "Show Users", "Go Back"])
          self.print_divider(236)
          print("Your Choice: ", end='')
          op = self.listen_input()
          self.print_divider(236)
          if(op=='1'):
               self.render_add_book()
          
     def render_users(self):
          users = self.library.get_users()
          
          print("-"*142)
          print(f"|{'User Id':^8}|{'USERNAME':^30}|{'EMAIL':^30}|{'MEMBERSHIP':^40}|{'EXPIRY':^40}")
          print("-"*142)
          
          for user in users:
               user:User = user
               print(f"|{str(user.get_id()):^8}|{user.get_username():^30}|{user.get_email():^30}|{user.get_membership():^40}|{str(user.get_membership_expiry()):^40}")
          print("-"*142)
          
          return self.render_admin_page()
               
     def render_add_book(self):
          title = input("Title: ")
          author = input("Author: ")
          while(True):
               day = input("Day: ")
               month = input("Month: ")
               year = input("Year: ")
               try:
                    date = datetime(year, month, day)
               except Exception as e:
                    print("Enter valid date..")
                    pass
               else:
                    break
          copies = input("No. of copies: ")
          print("Enter the genres: (press e to exit the loop)")
          genre_list = []
          while(True):
               g = input()
               if(g=='e'):break
               val = self.library.valid_genre(g)
               if(val is not None):genre_list.append(val)
                                   
          book = Book(title,author,0,genre_list, date)
          self.library.add_collection(book,copies)

     # A method to render the registration page  
     def render_register(self):
          self.print_divider(200)
          tprint(f"{'Registration':^130}")
          self.print_divider(200)
          print("(Enter 'b' to cancel registration)")
          
          username = ''
          password = ''
          
          #prompting username and validating it
          while(True):
               print("Username: ", end="")
               username = self.listen_input()
               if(username.strip()=='b'):
                    return self.render_login()
               valid = self.library.username_is_valid(username)
               if(valid is True):
                    break
               print("This username is already taken, please enter another")
          
          # prompting password and confirming it
          while(True):
               print("Password: ", end="")
               password = self.listen_input()
               if(password.strip()=='b'):
                    return self.render_login()
               print("Confirm Password: ", end="")
               c_password = self.listen_input()
               if(c_password.strip()=='b'):
                    return self.render_login()
              
               if(password == c_password):
                    break
               
          print("Email: ", end="") 
          
          email = self.listen_input()
          if(email.strip()=='b'):return self.render_login()
          user_r  = self.library.create_user_prof(username, password,
                    Membership.INVALID,email)     #creating a sample user 
          self.library.register(user_r)      #registerting the user to the library
          self.print_divider(200)
          print("Successfull registration!!")
          print("To create a membership, navigate Profile > Settings > Membership")
          self.print_divider(200)
          return self.render_login()
          
     # renders main page
     def render_index(self):
          inp = ''      
          title = ConsoleRunner.page_titles["index"]
          self.print_divider(200)
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
               return self.render_profile()
          elif(inp=='2'):
               return self.render_browse()
          elif(inp=='3'):
               return self.render_checkout()
          elif(inp=='4'):
               return self.render_checkin()
          else:
               return self.logout()
          
     # A method to render the checkout page  
     def render_checkout(self):
          self.print_divider(190)
          tprint(f"|{'Check-Out':^130}|")
          self.print_divider(190)
          print("(Enter 'b' to go back)")
          print("Enter a collection id or title: ", end='')
          inp = self.listen_input()
          if(inp=='b'):
               self.render_index()
          tp = self.library.get_all(inp)
          self.print_divider(190)
          # if only one book is returned
          if(tp[0]==True):
               book:Book = tp[1]
               
               print("-"*142)  
               print(f"|{'Col. No.':^8}|{'Title':^30}|{'Author':^30}|{'Genre':^60}|")
               print("-"*142)
               print(f"|{str(book.get_id()):^8}|{book.get_title():^30}|{book.get_author():^30}|{str(book.get_genres()):^60}|")               
               print("-"*142)
               print("Confirm:")
               self.render_options(["YES","NO"])
               self.print_divider(190)
               print("Your option: ", end='')
               op = self.listen_input()
               self.print_divider(190)
               if(op=='1'):
                    bk = self.library.check_out(book, self.session)
                    self.print_checkout_details(bk)

          # if multiple books are returned
          elif(tp[0]==False and tp[1] is not None):
               print("-"*142)  
               print(f"|{'Col. No.':^8}|{'Title':^30}|{'Author':^30}|{'Genre':^60}|")
               print("-"*142)  
               for book in tp[1]:
                    print(f"|{int(book.get_id()):^8}|{book.get_title():^30}|{book.get_author():^30}|{str(book.get_genres()):^60}|")
               self.print_divider(190)
               print("Enter the collection no.: ",end='')
               number = int(self.listen_input())
               bk = self.library.check_out(Book("","",number,[]), self.session)
               self.print_checkout_details(bk)
          
          # No book exists
          else:
               print("Sorry no book like that exists...")
          
               
          return self.render_checkout()
     
     # A method to render the check in page
     def render_checkin(self):
          # printing the title
          self.print_divider(190)
          tprint(f"|{'Check-In':^130}|")
          self.print_divider(190)
          print("Enter 'b' to go back...")
          
          while(True):
               self.print_pending()
               self.print_divider(190)
               book_no = self.listen_input()
               if(book_no=='b'):return self.render_index()
               self.print_divider(130)
               confirm = self.library.check_in(book_no, self.session)
               
               if(confirm):
                    print(f"The book with number {book_no} has been successfully returned..")
               else:
                    print(f"This book does not exists")
          
     # A method to render the profile options of the user      
     def render_profile(self):
          option = ''
          
          self.print_divider(200)
          title = f"| Welcome  back {self.session.get_username()} |"
          tprint(f"{title:^130}")
          
          while(True):
               self.print_divider(200)
               self.render_options([
                    "Go Back",
                    "History",
                    "Pending Returns",
                    'Membership',
                    "Logout"
               ])
               self.print_divider(200)
               print("Your Choice: ", end="")
               option = self.listen_input()
               self.print_divider(200)
               
               if(self.check_option_validity(6,option)):
                    break
               print("Invalid Option")
               
          if(option=='1'):
               return self.render_index()
          elif(option=='2'):
               return self.render_history()
          elif(option=='3'):
               return self.render_pending_returns()
          elif(option=='4'):
               return self.render_membership()
          else:
               return self.logout()

     # A method to render the brose page
     def render_browse(self):
          self.print_divider(200)
          tprint(f"|{'Browse Games':^130}|")
          self.print_divider(200)
          
          print("Search By:")
          self.render_options(["Genre", "Title"])
          self.print_divider(200)
          print("Your Choice: ", end='')
          op = self.listen_input()
          self.print_divider(200)
          
          if(op=='b'):
               return self.render_index()
          elif(op=='1'):
               return self.render_genre_browse()
          else:
               return self.render_title_browse()
          
     # A method to render the page to brose books by genre 
     def render_genre_browse(self):
          print('FICTION\nBIOGRAPHY\nCOMEDY\nHISTORICAL\nROMANCE\nDRAMA\nTHRILLER\nKIDS\nHORROR\nCRIME\nSCIENCE_AND_TECHNOLOGY\nADVENTURE\nSPIRITUAL\nADULT\nMAGAZINE\nTRAVEL\nART')
          self.print_divider(200)
          print("Enter your genre type: ", end='')
          genre = self.listen_input()
          if(genre=='b'):
               return self.render_browse()
          self.print_divider(200)
          li = self.library.filter_genre(genre)
          
          if(len(li)>0) :
               print("-"*162)  
               print(f"|{'No.':^6}|{'Title':^30}|{'Author':^30}|{'Genre':^60}|{'Date and Time' :^30}|")
               print("-"*162)
               
               for collection in li:
                    collection:Collection = collection
                    print(f"|{collection.get_id():^6}|{collection.get_title():^30}|{collection.get_author():^30}|{str(collection.get_genres()):^60}|{str(collection.get_published()) :^30}|")
               print("-"*162)
          else:
               print("No books with that genre found...")
          return self.render_browse()

     # A method to render the page to browse books by title
     def render_title_browse(self):
          self.print_divider(200)
          print("Enter the title: ", end='')
          title = self.listen_input()
          if(title=='b'):
               return self.render_browse()
          
          self.print_divider(200)
          li = self.library.filter_substring(title)
          
          
          if(len(li)>0):
               print("-"*162)  
               print(f"|{'No.':^6}|{'Title':^30}|{'Author':^30}|{'Genre':^60}|{'Date and Time' :^30}|")
               print("-"*162)
               for collection in li:
                    collection:Collection = collection
                    print(f"|{collection.get_id():^6}|{collection.get_title():^30}|{collection.get_author():^30}|{str(collection.get_genres()):^60}|{str(collection.get_published()) :^30}|")
               print("-"*162)
          else:
               print*"Sorry nothing found..."
          
          return self.render_browse()
          
     # A method to render the history of the user
     def render_history(self):
          history = self.library.get_history_for(self.session)   #[(<Book>, checkedout:str),...]
          tprint(self.page_titles["history"])
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
          
          return self.render_profile()
     
     # A method to show pending returns
     def render_pending_returns(self):
          self.print_divider(200)
          tprint(f"{'Check Outs':^100}")
          self.print_divider(200)
          
          self.print_pending()
          return self.render_profile()
          
          
     # A method to render the page that displays membership details
     def render_membership(self):
          self.print_divider(115)
          tprint("|Membership-Details|")
          self.print_divider(115)
          dmy = self.session.get_membership_expiry()
          print(f"Membership Type: {self.session.get_membership()}")
          if dmy is not None:
               print(f"Membership Exipry: {dmy[0]}-{dmy[1]}-{dmy[2]}")
               self.render_profile()
               return
          else:
               print(f"YOUR MEMBERSHIP HAS ALREADY EXPIRED PLEASE RENEW IT.")
               
               self.print_divider(115)
               print("Do you want to renew it?")
               self.render_options(["YES","NO"])
               self.print_divider(115)
               
               print("Your Choice: ", end='')
               op = self.listen_input()
               if(op=='2'):
                    return self.render_profile()
               elif(op=='1'):
                    return self.render_renewal()
               return
          
     # A method to logout the user
     def logout(self):
          self.print_divider(200)
          
          while(True):
               print("Are you sure you want to logout?")
               self.render_options(["YES", "NO"])
               self.print_divider(200)
               print("Your Choice: ", end='')
               inp = self.listen_input()
               self.print_divider(200)
               
               if(inp=='1'):
                    self.session = None
                    print("Successfully logged out!")
                    return self.start()
               elif(inp=='2'):
                    return self.render_index()
               else:
                    print("Enter a valid option")
          
     # A page to renew membership
     def render_renewal(self):
          self.print_divider(200)
          tprint(f"|{'RENEW':^130}|")
          self.print_divider(200)
          print("Select a plan:")
          
          options = ["YEARLY","MONTHLY","STUDENT", "GO BACK"]
          self.render_options(options)
          self.print_divider(200)
          print("Your Choice: ", end="")
          op = self.listen_input()
          self.print_divider(200)
          
          if(op=='1' or op=='2' or op=='3'):
               r = self.library.renew_membership(self.session, options[int(op)-1])
               print(f"Successfully renewed for {r} membership")     
          return self.render_profile()
          
          
                    
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
          except Exception as e:
               return False
          if(not(var>=1 and var<=count)):
               return False
          return True
     
     # A method to print the details of the book passed
     def print_checkout_details(self, bk:Book)->bool:
          if(bk[0] is not None):
               bk:Book = bk[0]
               print(f"Successfully checked out {bk.get_title()} written by {bk.get_author()}")
               print("Book Id: ", bk.get_id())
               print("Title: ", bk.get_title())
               print("Author: ", bk.get_author())
               print("Genres: ", bk.get_genres())
               print("Published Date: ",bk.get_published().date())
               return True
          elif(bk[1]==True):
               print("Sorry but that book is currently unavailable.")
               return False
          else:
               print("YOU CANNOT CHECKOUT BOOKS SINCE YOUR MEMBERSHIP IS EXPIRED, PLEASE RENEW IT!!")
          
     # A method to print the pending check outs of the current user in session   
     def print_pending(self):
          check_outs = self.library.get_checkouts_for(self.session)
          print("-"*162)
          print(f"|{'No.':<6}|{'Title':<30}|{'Author':<30}|{'Genre':<60}|{'Date and Time' :<30}|")
          print("-"*162)
          
          for i in range(len(check_outs)):
               data = check_outs[i]
               book:Book = data[0]
               date_time = data[1]
               print(f"|{book.get_id():<6}", end="")
               print(f"|{book.get_title() :<30}", end="")
               print(f"|{book.get_author() :<30}", end="")
               print(f"|{str(book.get_genres()) :<60}", end="")
               print(f"|{date_time:<30}|")
          print("-"*162)