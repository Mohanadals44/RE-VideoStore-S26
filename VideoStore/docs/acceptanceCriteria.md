# VideoStore Acceptance Criteria

## 1. Movie Management

| ID | Criteria | Validating Test(s) |
|----|----------|---------------------|
| AC-1.1 | Creating a movie with a title and Regular price code stores both correctly. | `Movie_t.test_regular_movie` |
| AC-1.2 | Creating a movie with a title and New Release price code stores both correctly. | `Movie_t.test_new_release` |
| AC-1.3 | Creating a movie with a title and Children's price code stores both correctly. | `Movie_t.test_childrens` |
| AC-1.4 | A movie title containing spaces is stored and retrieved correctly. | `Movie_t.test_longer_title` |
| AC-1.5 | A movie's price category can be changed from New Release to Regular after creation. | `Movie_t.test_change_price` |

## 2. Customer Management

| ID | Criteria | Validating Test(s) |
|----|----------|---------------------|
| AC-2.1 | Creating a customer with a name stores and returns that name. | `Customer_t.test_no_rental` |

## 3. Rental Management

| ID | Criteria | Validating Test(s) |
|----|----------|---------------------|
| AC-3.1 | A rental stores and returns the associated movie object. | `Rental_t.test_get_movie` |
| AC-3.2 | A rental stores and returns the number of days rented. | `Rental_t.test_get_days_rented`, `Rental_t.test_get_days_rented_one_day` |
| AC-3.3 | A customer with zero rentals produces a valid statement. | `Customer_t.test_no_rental` |
| AC-3.4 | A customer can have one rental added and it appears in the statement. | `Customer_t.test_one_rental` |
| AC-3.5 | A customer can have multiple rentals added and all appear in the statement. | `Customer_t.test_two_rentals` |

## 4. Charge Calculation — Regular

| ID | Criteria | Validating Test(s) |
|----|----------|---------------------|
| AC-4.1 | Regular movie, 1 day: charge is $2. | `Rental_t.test_charge_regular_one_day` |
| AC-4.2 | Regular movie, 2 days (boundary): charge is $2. | `Rental_t.test_charge_regular_two_days` |
| AC-4.3 | Regular movie, 3 days (over threshold): charge is $3.50. | `Rental_t.test_charge_regular_three_days` |
| AC-4.4 | Regular movie, 5 days: charge is $6.50. | `Rental_t.test_charge_regular_five_days` |

## 5. Charge Calculation — New Release

| ID | Criteria | Validating Test(s) |
|----|----------|---------------------|
| AC-5.1 | New Release movie, 1 day: charge is $3. | `Rental_t.test_charge_new_release_one_day` |
| AC-5.2 | New Release movie, 2 days: charge is $6. | `Rental_t.test_charge_new_release_two_days` |
| AC-5.3 | New Release movie, 5 days: charge is $15. | `Rental_t.test_charge_new_release_five_days` |

## 6. Charge Calculation — Children's

| ID | Criteria | Validating Test(s) |
|----|----------|---------------------|
| AC-6.1 | Children's movie, 1 day: charge is $1.50. | `Rental_t.test_charge_childrens_one_day` |
| AC-6.2 | Children's movie, 3 days (boundary): charge is $1.50. | `Rental_t.test_charge_childrens_three_days` |
| AC-6.3 | Children's movie, 4 days (over threshold): charge is $3.00. | `Rental_t.test_charge_childrens_four_days` |
| AC-6.4 | Children's movie, 6 days: charge is $6.00. | `Rental_t.test_charge_childrens_six_days` |

## 7. Total Charge

| ID | Criteria | Validating Test(s) |
|----|----------|---------------------|
| AC-7.1 | Total charge for zero rentals is 0. | `Customer_t.test_no_rental` |
| AC-7.2 | Total charge for one Regular rental (1 day) is $2. | `Customer_t.test_one_rental` |
| AC-7.3 | Total charge for two rentals (Regular 10 days + Children's 5 days) is the sum of individual charges. | `Customer_t.test_two_rentals` |

## 8. Frequent Renter Points

| ID | Criteria | Validating Test(s) |
|----|----------|---------------------|
| AC-8.1 | Zero rentals earns 0 frequent renter points. | `Customer_t.test_no_rental` |
| AC-8.2 | One Regular rental earns 1 frequent renter point. | `Customer_t.test_one_rental` |
| AC-8.3 | A New Release rented for more than 1 day earns 2 points (1 base + 1 bonus). | `Customer_t.test_two_rentals` (indirectly via statement output) |
| AC-8.4 | Multiple rentals accumulate points correctly across all rentals. | `Customer_t.test_two_rentals` |

## 9. Statement Output Format

| ID | Criteria | Validating Test(s) |
|----|----------|---------------------|
| AC-9.1 | Statement begins with `Rental Record for <name>`. | `Customer_t.test_no_rental`, `Customer_t.test_one_rental` |
| AC-9.2 | Each rental is listed as `\t<title>\t<charge>` on its own line. | `Customer_t.test_one_rental`, `Customer_t.test_two_rentals` |
| AC-9.3 | Charges have trailing zeros removed (e.g., `2` not `2.00`). | `Customer_t.test_one_rental` |
| AC-9.4 | Statement includes `Amount owed is: <total>`. | `Customer_t.test_no_rental`, `Customer_t.test_one_rental`, `Customer_t.test_two_rentals` |
| AC-9.5 | Statement includes `You earned: <points> frequent renter points`. | `Customer_t.test_no_rental`, `Customer_t.test_one_rental`, `Customer_t.test_two_rentals` |
| AC-9.6 | No-rental statement shows total 0 and 0 points. | `Customer_t.test_no_rental` |
