"""
Book shop project that manages inbound, outbound of books including shelfing, checkout, etc
"""

class book:

    def __init__(self, b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price):
        """
        This class is used to create book objects
            :param b_isbn: Integer - Unique book identification number
            :param b_name: String - Name of the book
            :param b_lang: String - Language of book
            :param b_origin: String - Origin of publisher
            :param b_authors: List - Author/s of book
            :param b_version: String - Version of book
            :param b_price: Float - Value of 1 book in INR
        """
        self.b_isbn = b_isbn  # Number which is unique
        self.b_name = b_name  # String
        self.b_lang = b_lang  # String
        self.b_origin = b_origin  # String
        self.b_authors = b_authors  # List
        self.b_version = b_version  # String
        self.b_price = b_price  # Float
