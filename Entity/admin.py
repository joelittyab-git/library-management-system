class Admin(object):
     
     '''A class that represents an admin in a library
     :<str>:username -> stores the username of the admin
     :<str>:password -> stores password of the admin
     '''
     def __init__(self,username:str, password:str) -> None:
          self.username = username
          self.password = password
          
     def get_username(self)->str:
          return self.username
     
     def get_password(self)->str:
          return self.password