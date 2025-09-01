# Password Generator (Python)

A Python tool that uses the **standard library** (`itertools`, `string`, `logging`) to generate all possible passwords of a given length using **letters**, **digits**, or **both**.  
It is interactive (takes user input) and demonstrates efficient password generation without external dependencies.  


##  Features
-  User chooses **password length**  
-  User selects character set:  
  - Letters only (`a-z`, `A-Z`)  
  - Digits only (`0-9`)  
  - Letters + Digits (`a-z`, `A-Z`, `0-9`)  
-  Uses [`itertools.product`](https://docs.python.org/3/library/itertools.html) to generate combinations  
-  Efficient: does not store all passwords in memory  
-  Built-in **logging** to track progress  


