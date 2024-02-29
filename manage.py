from Entity.user import User
from Entity.user import Membership
from Entity.book import Book
from Management.library import LibraryManager
from datetime import datetime
from Interface.console import ConsoleRunner

user = User("joeittab","joeittab@gmail.com","", 1000, Membership.YEARLY_MEMBER)
book = Book("Joel's Cannon vol1","Joel1", 122, datetime.now(),[])
book2 = Book("Joel's Cannon vol2","Joel2", 123, datetime.now(),[])
book3 = Book("Joel's Cannon vols 3","Joel3", 123, datetime.now(),[])

# user.check_out(book)
# print(user.checked_out)
# user.check_in(book)
# print(user.checked_out)


# obj = getattr(Book.Genre, "HORROR1")
# print(obj)


application = ConsoleRunner(LibraryManager())
application.start()