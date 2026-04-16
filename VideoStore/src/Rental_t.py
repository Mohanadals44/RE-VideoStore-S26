"""
Rental_t.py

Test program for class Rental.

"""

import unittest
from Rental import Rental
from Movie import Movie

class TestRental(unittest.TestCase):

    def test_get_movie(self):
        movie = Movie("A", Movie.REGULAR)
        rental = Rental(movie, 3)
        self.assertIs(rental.get_movie(), movie)
        self.assertEqual(rental.get_movie().get_title(), "A")
        self.assertEqual(rental.get_movie().get_price_code(), Movie.REGULAR)

    def test_get_days_rented(self):
        movie = Movie("A", Movie.REGULAR)
        rental = Rental(movie, 5)
        self.assertEqual(rental.get_days_rented(), 5)

    def test_get_days_rented_one_day(self):
        movie = Movie("A", Movie.REGULAR)
        rental = Rental(movie, 1)
        self.assertEqual(rental.get_days_rented(), 1)

    # --- REGULAR charge tests ---

    def test_charge_regular_one_day(self):
        rental = Rental(Movie("A", Movie.REGULAR), 1)
        self.assertEqual(rental.get_charge(), 2)

    def test_charge_regular_two_days(self):
        rental = Rental(Movie("A", Movie.REGULAR), 2)
        self.assertEqual(rental.get_charge(), 2)

    def test_charge_regular_three_days(self):
        rental = Rental(Movie("A", Movie.REGULAR), 3)
        self.assertEqual(rental.get_charge(), 3.5)

    def test_charge_regular_five_days(self):
        rental = Rental(Movie("A", Movie.REGULAR), 5)
        self.assertEqual(rental.get_charge(), 6.5)

    # --- NEW_RELEASE charge tests ---

    def test_charge_new_release_one_day(self):
        rental = Rental(Movie("A", Movie.NEW_RELEASE), 1)
        self.assertEqual(rental.get_charge(), 3)

    def test_charge_new_release_two_days(self):
        rental = Rental(Movie("A", Movie.NEW_RELEASE), 2)
        self.assertEqual(rental.get_charge(), 6)

    def test_charge_new_release_five_days(self):
        rental = Rental(Movie("A", Movie.NEW_RELEASE), 5)
        self.assertEqual(rental.get_charge(), 15)

    # --- CHILDRENS charge tests ---

    def test_charge_childrens_one_day(self):
        rental = Rental(Movie("A", Movie.CHILDRENS), 1)
        self.assertEqual(rental.get_charge(), 1.5)

    def test_charge_childrens_three_days(self):
        rental = Rental(Movie("A", Movie.CHILDRENS), 3)
        self.assertEqual(rental.get_charge(), 1.5)

    def test_charge_childrens_four_days(self):
        rental = Rental(Movie("A", Movie.CHILDRENS), 4)
        self.assertEqual(rental.get_charge(), 3.0)

    def test_charge_childrens_six_days(self):
        rental = Rental(Movie("A", Movie.CHILDRENS), 6)
        self.assertEqual(rental.get_charge(), 6.0)


if __name__ == "__main__":
    unittest.main()
