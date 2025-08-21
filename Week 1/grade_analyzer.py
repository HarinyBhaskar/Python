import os                 
import statistics                       
import time               

print("="*50)             
print("   Welcome to the Grade Analyzer!   ")  
print("="*50)             


script_dir = os.path.dirname(os.path.abspath(__file__))  

while True:               
    filename_input = input("Enter the filename (default: scores.txt): ").strip()  
    if filename_input == "":            
        filename = "scores.txt"          
    else:                                
        filename = filename_input        

    if not os.path.isabs(filename):      
        filename = os.path.join(script_dir, filename)  

    # Check file existence
    if not os.path.exists(filename):     
        print(f" File '{filename}' not found. Please try again.\n")  
        continue                         
   
    students = []                       
    scores = []                          
    with open(filename, "r") as file:    
        for line in file:                
            name, score = line.strip().split(",")  
            students.append(name.strip())         
            scores.append(int(score.strip()))      

    # --- Statistics ---
    total_students = len(scores)        
    total_score = sum(scores)             
    avg_score = total_score / total_students  
    median_score = statistics.median(scores)  
    std_dev = statistics.stdev(scores) if len(scores) > 1 else 0 
    highest_score = max(scores)           
    lowest_score = min(scores)            
    # Find toppers and lowest scorers
    toppers = [students[i] for i, s in enumerate(scores) if s == highest_score]  
    lowest_scorers = [students[i] for i, s in enumerate(scores) if s == lowest_score]  

    # Pass/fail (>=40 pass)
    passed = sum(1 for s in scores if s >= 40) 
    failed = total_students - passed           
    above_avg = sum(1 for s in scores if s > avg_score) 
    below_avg = total_students - above_avg     

    # Grade distribution
    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}  # Data structures: dictionary
    for s in scores:                
        if s >= 90:                  
            grades["A"] += 1
        elif s >= 75:
            grades["B"] += 1
        elif s >= 60:
            grades["C"] += 1
        elif s >= 40:
            grades["D"] += 1
        else:
            grades["F"] += 1

    # --- Output ---
    print("\n--- Grade Analyzer Report ---")  # I/O: output
    print(f"Total Students       : {total_students}")  # I/O
    print(f"Total Score          : {total_score}")     # I/O
    print(f"Average Score        : {avg_score:.2f}")   # I/O
    print(f"Median Score         : {median_score}")    # I/O
    print(f"Standard Deviation   : {std_dev:.2f}")     # I/O
    print(f"Highest Score        : {highest_score}")   # I/O
    print(f"Lowest Score         : {lowest_score}\n")  # I/O

    print("Topper(s):")             
    for name in toppers:            
        print(f" - {name} ({highest_score})")  

    print("\nLowest Scorer(s):")   
    for name in lowest_scorers:     
        print(f" - {name} ({lowest_score})")  

    print(f"\nPassed               : {passed}")        
    print(f"Failed               : {failed}")          
    print(f"Above Average        : {above_avg}")       
    print(f"Below Average        : {below_avg}")       

    print("\nGrade Distribution:")  
    for grade, count in grades.items():  
        print(f" {grade}: {count}")      

    # --- Leaderboard ---
    leaderboard = sorted(zip(students, scores), key=lambda x: (-x[1], x[0])) 
    print("\nLeaderboard:")         
    for rank, (name, score) in enumerate(leaderboard, start=1):  
        print(f"{rank}. {name} - {score}")  
    if highest_score == 100:       
        print("Outstanding! We have a perfect scorer!")  
    elif highest_score >= 90:
        print("Great work by the topper! Aim for 100 next time!")  
    else:
        print("Let's push harder for even higher scores next time!")  

    if failed > 0:                  
        print(f"{failed} student(s) need more support. Let’s encourage and guide them!")  # I/O
    else:
        print("Fantastic! Everyone passed!") 

    if avg_score >= 75:           
        print("Class performance is excellent overall!") 
    elif avg_score >= 50:
        print("Class is doing okay, but there's room for improvement.") 
    else:
        print("We need to focus on improving class performance.") 

    again = input("\nDo you want to analyze another file? (y/n): ").strip().lower() 
    if again != 'y':                
        print("\nThank you for using Grade Analyzer. !")  # I/O
        time.sleep(1)               
        break                    
