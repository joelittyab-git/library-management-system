from Management.library import LibraryManager
from Interface.console import ConsoleRunner
from Entity.admin import Admin

# object instantiation
manager:LibraryManager = LibraryManager()
application:ConsoleRunner = ConsoleRunner(manager)

#default admin
admin = Admin("admin", "Admin@123")
application.library.register_admin(admin)

application.start()

