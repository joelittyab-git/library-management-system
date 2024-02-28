from Entity.user import User
from Entity.user import Membership
from Entity.book import Book
from datetime import datetime
from Interface.console import ConsoleRunner
user = User("joeittab","joeittab@gmail.com", 1000, Membership.YEARLY_MEMBER)
book = Book("Joel's Cannon","Joel", 122, datetime.now(),[])

user.check_out(book)
print(user.checked_out)
user.check_in(book)
print(user.checked_out)


obj = getattr(Book.Genre, "HORROR1")
print(obj)

application = ConsoleRunner()
application.start()