# VideoStore Functional Requirements

## 1. Movie Management

- **FR-1.1**: A movie shall have a title (string) and a price category.
- **FR-1.2**: The system shall support three price categories: Regular (0), New Release (1), and Children's (2).
- **FR-1.3**: A movie's price category may be changed after creation.
- **FR-1.4**: An invalid price category shall raise an error.

## 2. Customer Management

- **FR-2.1**: A customer shall be created with a name.
- **FR-2.2**: The system shall allow retrieval of the customer's name.

## 3. Rental Management

- **FR-3.1**: A rental shall associate one movie with a number of days rented.
- **FR-3.2**: A customer may have zero or more rentals.
- **FR-3.3**: Rentals shall be added to a customer one at a time.

## 4. Charge Calculation

- **FR-4.1 (Regular)**: A regular movie costs $2.00 for the first 2 days. Each additional day beyond 2 costs $1.50.
- **FR-4.2 (New Release)**: A new release movie costs $3.00 per day for any number of days.
- **FR-4.3 (Children's)**: A children's movie costs $1.50 for the first 3 days. Each additional day beyond 3 costs $1.50.
- **FR-4.4**: The total charge for a customer is the sum of charges across all their rentals.

## 5. Frequent Renter Points

- **FR-5.1**: Each rental earns the customer 1 frequent renter point.
- **FR-5.2**: A new release movie rented for more than 1 day earns 1 bonus point (2 points total).
- **FR-5.3**: The total frequent renter points for a customer is the sum of points across all their rentals.

## 6. Statement Output

- **FR-6.1**: The statement shall begin with the line: `Rental Record for <customer name>`
- **FR-6.2**: Each rental shall be listed on its own line in the format: `\t<movie title>\t<charge>`
- **FR-6.3**: Charges shall be formatted to remove trailing zeros (e.g., `2` not `2.00`, `3.5` not `3.50`).
- **FR-6.4**: The statement shall include a line: `Amount owed is: <total charge>`
- **FR-6.5**: The statement shall include a line: `You earned: <points> frequent renter points`
- **FR-6.6**: A customer with no rentals shall show a total of 0 and 0 frequent renter points.
