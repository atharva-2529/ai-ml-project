# ai-ml-project

#  Basic CLI Flight Ticket Simulator

This is a minimal Python script designed to simulate the process of booking a flight ticket via the command-line interface (CLI). It serves as a simple demonstration of basic Python I/O, function definition, conditional logic, and the use of the `random` module.

##  Features

* **Trip Selection:** Allows the user to select between **Domestic** or **International** travel.
* **Input Collection:** Collects necessary ticket details (Start, Destination, Date, Seat Preference).
* **Price Simulation:** Generates a random ticket price, with a distinct, higher range for international flights.
* **Seat Simulation:** Generates a random seat number for the booked ticket.

##  Getting Started

### Prerequisites

You only need Python installed on your system.

```bash
python --version

Installation and Execution

    Save the Code: Save the provided Python code into a file named flightbooking.py.

    Run from CLI: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:

Bash

python flightbooking.py

    Follow Prompts: The program will prompt you to enter travel details sequentially.

Code Overview

The program relies on two primary functions, which contain highly redundant code, separated only by the simulated price range:

    domestic(): Generates prices between 3,000 and 10,000 INR.

    international(): Generates prices between 70,000 and 100,000 INR.

The script executes the appropriate function based on the initial user input.

Limitations & Future Work

This is a proof-of-concept and lacks any real-world functionality.
Limitation	Planned Improvement
Code Duplication	Refactor the redundant domestic and international functions into a single, cleaner function.
No Validation	Implement checks (e.g., using try/except) to ensure inputs like dates and preferences are valid.
No Inventory	Integrate an Object-Oriented structure to track available seats and prevent overbooking.
No Persistence	Implement saving the ticket details to a file (CSV or JSON) so the data is not lost when the script closes.
