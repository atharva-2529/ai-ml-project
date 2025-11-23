
# Project Statement: Basic Flight Ticket Simulator

## Project Identification

| Field | Detail |
| :--- | :--- |
| **Project Name** | Basic CLI Flight Ticket Simulator |
| **Version** | 1.0 (Initial Script) |
| **Development Platform** | Python 3.x, Command Line Interface (CLI) |
| **Status** | Completed (Proof-of-Concept) |

---

## Project Scope and Purpose

The sole purpose of this script is to **simulate** a successful ticket booking experience through sequential user interaction in a terminal environment. It is intended strictly as an academic exercise to demonstrate proficiency in basic Python flow control and input/output handling.

### Inclusions
* Collects all basic required information for a ticket (Start, Destination, Date).
* Applies a simple conditional logic to determine the appropriate price range (Domestic vs. International).
* Uses the `random` module to provide variable price and seat data on each run.
* Prints a final, styled confirmation receipt.

### Exclusions 
* **No Inventory Management:** The system does not check seat availability; it always confirms the booking.
* **No Data Storage:** All information is lost upon program termination.
* **No Real-time Data:** Prices, routes, and seat numbers are randomly generated, not pulled from a real source.
* **No Error Handling:** The script does not gracefully handle invalid or unexpected user input.

---

##  Core Design Rationale

The design is **procedural** and relies on two parallel functions to handle the distinct price requirements of domestic versus international travel. This separation, although redundant, was chosen to make the core difference (pricing logic) immediately visible and isolated in the code. The use of the global `dist` variable for conditional execution minimizes complexity by avoiding function parameter passing in this basic structure.

##  Conclusion

The Basic CLI Flight Ticket Simulator successfully achieves its limited goal of demonstrating simple, functional user interaction and output generation using core Python syntax. It provides a solid  starting point for future expansion into a truly object-oriented and functional system.

The Basic CLI Flight Ticket Simulator successfully achieves its limited goal of demonstrating simple, functional user interaction and output generation using core Python syntax. It provides a solid, if basic, starting point for future expansion into a truly object-oriented and functional system.