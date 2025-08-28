# ATM Banking System (with Timed Decorator, Functools, and Logging)

##  Project Overview
This project simulates a simple **ATM Banking System** in Python.  
It demonstrates the use of:
- **Decorators** (`@timed` decorator to measure execution time of functions)  
- **functools.wraps** (to preserve function metadata when wrapping functions)  
- **Python Logging** (to log execution times and actions performed in the system)  

The program allows a user to:
- Check balance  
- Withdraw money  
- Deposit money  

Each operation is logged with execution time for monitoring and debugging purposes.

## Features
- `@timed` decorator to automatically log how long each ATM operation takes  
- User interactive menu-driven system  
- Logging of all critical actions and performance metrics  
- Simple simulation of real-world ATM functions  

## Technologies Used
- **Python 3.x**  
- **functools**  
- **logging**  
- **time**  

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/atm-system.git
   cd atm-system
