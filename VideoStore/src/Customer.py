# Customer.py

# Definition file for Customer class.

from typing import List
from Rental import Rental
from Movie import Movie

class Customer:
    def __init__(self, name: str):
        self.name = name
        self.rentals: List[Rental] = []

    def get_name(self) -> str:
        return self.name

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def _get_total_charge(self) -> float:
        total = 0.0
        for rental in self.rentals:
            total += rental.get_charge()
        return total

    def statement(self) -> str:
        result = f"Rental Record for {self.get_name()}\n"
        frequent_renter_points = 0

        for rental in self.rentals:
            frequent_renter_points += rental.get_frequent_renter_points()

            # Title of rental
            result += f"\t{rental.get_movie().get_title()}\t" + f"{rental.get_charge():.2f}".rstrip('0').rstrip('.') + "\n"

        # Total amount owed
        result += f"Amount owed is: {self._get_total_charge():.2f}".rstrip('0').rstrip('.') + "\n"

        # Frequent renter points earned
        result += f"You earned: {frequent_renter_points} frequent renter points\n"

        return result

