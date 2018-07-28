
# import statements
from Book import book

class shelf:

    # Required variables
    shelves = {}        # Key : shelfname(String), Value: [list of book objects]


    def create_book(self, b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price):

        # If the shelves is empty
        if len(self.shelves.keys()) == 0 or str.upper(b_name) not in self.shelves.keys():
            btemp = book(b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price)
            self.shelves[str.upper(b_name[:2])] = [btemp]
        else:
            # if not empty, find the key, get the
            # For this iterate through the shelves, find the shelf, add it to the keys list
            for i in self.shelves.keys():
                # get the shelf values as list
                temp_list = self.shelves.get(i)


    def get_books(self):
        print("Printing all books\n" + "*"*18)
        for key in self.shelves.keys():
            book = self.shelves.get(key)
            print(book[0].b_name)



shelf().create_book(11111111, "Linux Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
shelf().create_book(22222222, "Linux Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
shelf().create_book(33333333, "Python", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
shelf().create_book(22222222, "Linux Admin", "English", "India", ["Rebello Williams"], "0.1a", 3050.00)
shelf().get_books()