#  Travel Itinerary Flattener

This mini-project demonstrates how to build a **Travel Itinerary Processor** in Python.  
It showcases **Comprehensions, Iterators, Generators, User Input**, and **Logging (debug, info, warning, error, critical)** in one program.


##  Features
- Accepts **user input** for destinations and activities (with optional nested sub-activities).  
- **Generator (`flatten`)** → Recursively extracts all activities from a nested travel plan.  
- **Custom Iterator (`Itinerary`)** → Iterates through activities step by step.  
- **Comprehension** → Flattens the plan into a simple list in one line.  
- **Logging** → Tracks execution:
  - `DEBUG`: Expansion of nested lists & yielded values.  
  - `INFO`: Completed iteration over activities.  
  - `WARNING`: Invalid user inputs (e.g., zero destinations).  
  - `ERROR`: Value errors during input.  
  - `CRITICAL`: Unexpected crashes.


## 🛠 How It Works
1. User enters the number of destinations.  
2. For each destination, user provides activities (`,` separated; use `;` to group sub-activities).  
3. The program:
   - Flattens the nested itinerary using a **generator**.  
   - Iterates through activities using a **custom iterator**.  
   - Builds a flat list using **list comprehension**.  
4. Logs are stored in `itinerary.log`.



##  Example Run
```text
Enter number of destinations: 2
Destination 1: Delhi
Activities in Delhi (',' sep, ';' for sub): Sightseeing;India Gate, Red Fort
Destination 2: Goa
Activities in Goa (',' sep, ';' for sub): Beach;Baga, Calangute, Adventure;Scuba Diving
