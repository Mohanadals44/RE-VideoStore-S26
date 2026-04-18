## Question 4
Loops that do more than one thing at a time are more difficult to comprehend and extend in the future.  The loop in method ```statement``` is performing multiple duties; including accumulating the total charge for all movies.  Perform a _Replace Temp with Query refactoring_ to eliminate the variable ```totalAmount``` by creating a private method ```getTotalCharge``` in class Customer.  Use a call to this new method where ```totalAmount``` is being output.

**Start Day/Time:**  April 17 11:40

**How did you decide whether the AI's output was useful, accurate, or appropriate?**

I verified that the new method correctly summed up charges by looping through all rentals and calling get each on each, which matches what the variable was doing before. I also ran all existing unit tests

**What changes did you make to the AI‑generated material? Be specific.**

I have not done any changes for the output

**I copied my AI-assisted chat log to ./docs/log4.txt**
[yes ] Yes [ ] No 

**Difficulty Level:**
[yes ] Easy  [ ] Avg  [ ] Difficult

**End Day/Time:** enter date and time here
 APR 17 11:54pm
