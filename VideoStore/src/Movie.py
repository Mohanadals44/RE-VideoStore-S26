# Movie.py

# Class for Movie

from abc import ABC, abstractmethod


class Price(ABC):
    @abstractmethod
    def get_price_code(self):
        pass


class RegularPrice(Price):
    def get_price_code(self):
        return Movie.REGULAR


class NewReleasePrice(Price):
    def get_price_code(self):
        return Movie.NEW_RELEASE


class ChildrensPrice(Price):
    def get_price_code(self):
        return Movie.CHILDRENS


class Movie:
    # Class constants for price codes
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def __init__(self, title, price_code):
        """
        Constructor to initialize movie title and price code
        """
        self._title = title
        self.set_price_code(price_code)

    def get_title(self):
        """
        Getter for movie title
        """
        return self._title

    def get_price_code(self):
        """
        Getter for movie price code
        """
        return self._price.get_price_code()

    def set_price_code(self, price_code):
        """
        Setter for movie price code. Accepts an int and stores the corresponding Price object.
        """
        if price_code == Movie.REGULAR:
            self._price = RegularPrice()
        elif price_code == Movie.NEW_RELEASE:
            self._price = NewReleasePrice()
        elif price_code == Movie.CHILDRENS:
            self._price = ChildrensPrice()
        else:
            raise ValueError(f"Invalid price code: {price_code}")

    def get_charge(self, days_rented):
        """
        Calculate the rental charge based on this movie's price code and the number of days rented.

        :param days_rented: Integer representing the number of days rented.
        :return: Float representing the rental charge.
        """
        this_amount = 0

        price_code = self.get_price_code()

        if price_code == Movie.REGULAR:
            this_amount += 2
            if days_rented > 2:
                this_amount += (days_rented - 2) * 1.5
        elif price_code == Movie.NEW_RELEASE:
            this_amount += days_rented * 3
        elif price_code == Movie.CHILDRENS:
            this_amount += 1.5
            if days_rented > 3:
                this_amount += (days_rented - 3) * 1.5

        return this_amount

