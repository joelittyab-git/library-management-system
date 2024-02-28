from Management.library import LibraryManager

class ConsoleRunner():
     def __init__(self, library:LibraryManager) -> None:
          self.library = library
          
          
     def start(self):
          print("*"*12)