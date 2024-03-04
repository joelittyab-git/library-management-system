from Entity.library import Library
from Entity.admin import Admin

class Administration(Library):
     
     def __init__(self) -> None:
          super().__init__()
          
     def authenticate_admin(self, username:str, password:str)->Admin:
          '''
          A method to authenticate admins based on username and password
          '''
          
          for admin in self.registered_admins:
               admin:Admin = admin
               if(admin.get_password()==password and 
                  admin.get_username()==username):
                    return admin
          else:
               return None
          