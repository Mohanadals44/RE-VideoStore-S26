# Rental.py

# Include necessary dependencies

from Movie import Movie

class Rental:
    def __init__(self, movie, days_rented):
        """
        Constructor for Rental class.

        :param movie: Movie object representing the rented movie.
        :param days_rented: Integer representing the number of days the movie is rented.
        """
        self._movie = movie
        self._days = days_rented

    def get_days_rented(self):
        """
        Get the number of days the movie is rented.

        :return: Integer representing the number of days rented.
        """
        return self._days

    def get_movie(self):
        """
        Get the movie object that is rented.

        :return: Movie object representing the rented movie.
        """
        return self._movie

    def get_charge(self):
        """
        Calculate the rental charge by delegating to the movie's charge calculation.

        :return: Float representing the rental charge.
        """
        return self.get_movie().get_charge(self.get_days_rented())

    def get_frequent_renter_points(self):
        """
        Calculate frequent renter points for this rental.

        :return: Integer representing the frequent renter points earned.
        """
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE and self.get_days_rented() > 1:
            return 2
        return 1
