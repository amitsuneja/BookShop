# import statements
from Book import book


class Shelf:
    shelves = {}

    def create_book(self, b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price):
        dict_key = str.upper(b_name[:2])
        btemp: book = book(b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price)
        if dict_key not in self.shelves.keys() or len(self.shelves.keys()) == 0:
            self.shelves[str.upper(dict_key)] = [btemp]
        else:
            self.shelves.get(dict_key).append(btemp)

    def get_books(self):
        print("\nPrinting all books\n" + "*" * 18)
        shelves = self.shelves.keys()
        for tmp_shelf in shelves:
            print("tmp_shelf --> " + tmp_shelf)
            for tmp_book in self.shelves.get(tmp_shelf):
                print("\t" + tmp_book.b_name, tmp_book.b_isbn)

    def search_isbn(self, b_isbn):
        shelves = self.shelves.keys()
        for tmp_shelf in shelves:
            for tmp_book in self.shelves.get(tmp_shelf):
                if b_isbn is tmp_book.b_isbn:
                    # Print book details and exit
                    print("Book Name \t: {} {}\n"
                          "ISBN \t\t: {}\n"
                          "Location \t: {}\n"
                          "Language \t: {}\n"
                          "Pub Origin \t: {}\n"
                          "Authors \t: {}\n"
                          "Price \t\t: {}"
                          .format(tmp_book.b_name, tmp_book.b_version, tmp_book.b_isbn, tmp_shelf, tmp_book.b_lang,
                                  tmp_book.b_origin, tmp_book.b_authors, tmp_book.b_price))


Shelf().create_book(12093840, "Linux Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
Shelf().create_book(32984579, "Windows Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
Shelf().create_book(10938457, "Python", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
Shelf().create_book(10983530, "Pi Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
# shelf().get_books()
Shelf().search_isbn(12093840)