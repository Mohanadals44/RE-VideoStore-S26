## Question 7
Now we need to make the changes that will use our new types for the method ```price_code``` in Movie.  Perform a type change.

Change the type of the variable ```price_code``` to ```Price```

Change the method ```setPriceCode``` to set the variable ```price_code``` to a new instance of the correct ```Price``` object using a switch or equivalent data structure in Python.

Change the method ```getPriceCode``` to call the method ```getPriceCode``` on the ```Price``` object and return that value.

**Start Day/Time:**  april 19 12:04 pm

**How did you decide whether the AI's output was useful, accurate, or appropriate?**

I looked at the updated setPriceCode and confirmed it maps each integer code to the correct Price subclass object. I also checked that getPriceCode now delegates to the Price object instead of returning the int directly. I ran all the tests and they passed which confirmed the type change did not break any existing behavior.

**What changes did you make to the AI‑generated material? Be specific.**

I did not make any changes to the generated code since the logic was correct

**I copied my AI-assisted chat log to ./docs/log7.txt**
[yes ] Yes [ ] No 

**Difficulty Level:**
[yes ] Easy  [ ] Avg  [ ] Difficult

**End Day/Time:** april 19 12:26 pm
