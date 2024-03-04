from Entity.user import User
from Entity.user import Membership
from Entity.library import Library
from Entity.book import Book
from Management.library import LibraryManager
from datetime import datetime
from Interface.console import ConsoleRunner

user = User("joeittab","joeittab@gmail.com","", 1000, Membership.YEARLY_MEMBER)
user2 = User("joeittab","joeittab@gmail.com","", 1001, Membership.YEARLY_MEMBER, datetime(2020,1,3))
book = Book("Joel's Cannon vol1","Joel1", 122,[], datetime.now())
book2 = Book("Joel's Cannon vol2","Joel2", 123,[], datetime.now())
book3 = Book("Joel's Cannon vols 3","Joel3", 123,[], datetime.now())
library = LibraryManager()
library.validate_membership(user)
library.validate_membership(user2)
print(user.get_membership())
print(user2.get_membership())
# user.check_out(book)
# print(user.checked_out)
# user.check_in(book)
# print(user.checked_out)


# obj = getattr(Book.Genre, "HORROR1")
# print(obj)



application = ConsoleRunner(LibraryManager())
# application.check_option_validity(10,"Joe")
# application.render_register()
# application.render_checkout()
# application.render_browse()
application.render_admin_page()
# application.start()

