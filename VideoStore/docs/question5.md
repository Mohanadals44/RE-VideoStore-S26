## Question 5
The method ```getCharge``` in class ```Rental``` accesses more information in class ```Movie``` than it does in class ```Rental```.  This is a classic symptom of a method that is in the wrong place.  Perform a _Move Method_ refactoring to move the functionality of the method ```getCharge``` into a new method of the same name in the class ```Movie```.  Leave the method ```getCharge``` in class ```Rental``` and have it call the new method in class ```Movie```.  It will be necessary to pass the number of days rented.

**Start Day/Time:**  April: 18 6:32pm 

**How did you decide whether the AI’s output was useful, accurate, or appropriate?**

I compared the original getCharge logic in Rental with the new getCharge method it created in Movie and confirmed it was the same pricing logic just moved over. I also checked that Rental.getCharge now just calls Movie.getCharge and passes the days rented. I ran all the tests to make sure the behavior stayed the same and they all passed.

**What changes did you make to the AI‑generated material? Be specific.**

I have not done any changes for the output

**I copied my AI-assisted chat log to ./docs/log5.txt**
[yes ] Yes [ ] No 

**Difficulty Level:**
[yes ] Easy  [ ] Avg  [ ] Difficult

**End Day/Time:** 
 April: 18 6:43pm 
