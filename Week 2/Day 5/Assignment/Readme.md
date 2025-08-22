# Utils Package – CSV Parser & Word Counter  

This program contains two main functions:  

- **Parse feedback from a CSV file**  
- **Count the most common words in that feedback**  


## How it Works  
1. The program reads customer feedback from a CSV file (`feedback.csv`).  
2. The `csv_parser` module extracts the **feedback** column.  
3. The `word_counter` module cleans the text (removes punctuation, makes lowercase) and counts word frequency using `collections.Counter`.  
4. The `main.py` script puts everything together:  
   - Loads feedback from the CSV  
   - Counts words  
   - Prints the top 5 most common words  

