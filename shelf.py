# import statements
from Book import book


class shelf:
    # Required variables
    shelves = {}  # Key : shelfname(String), Value: [list of book objects]

    def create_book(self, b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price):
        dict_key = str.upper(b_name[:2])
        if len(self.shelves.keys()) == 0:                   # If the self.shelves is empty
            btemp = book(b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price)
            self.shelves[str.upper(dict_key)] = [btemp]
            print(len(self.shelves.keys()))
        else:
            btemp = book(b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price)
            print(dict_key not in self.shelves.keys())
            if dict_key not in self.shelves.keys():
                self.shelves[str.upper(dict_key)] = [btemp]
            else:
                self.shelves.get(dict_key).append(btemp)

    def get_books(self):
        print("\nPrinting all books\n" + "*" * 18)
        shelves = self.shelves.keys()
        for shelf in shelves:
            print("shelf --> "+shelf)
            for book in self.shelves.get(shelf):
                print(book.b_name, book.b_isbn )


shelf().create_book(11111111, "Linux Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
shelf().create_book(22222222, "Windows Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
shelf().create_book(22222222, "Windows Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
shelf().create_book(33333333, "Python", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
shelf().create_book(22222222, "Pi Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
shelf().create_book(44444444, "Windows Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
shelf().get_books()
