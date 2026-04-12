# 🏦 CLI Banking Management System

A real-world based command-line banking system built in Python where users can deposit, withdraw, and manage their bank accounts.

---

##  What is this project?

This is a terminal-based banking system that simulates real banking operations. Users can create savings or current accounts, perform transactions, check balances, and view transaction history. All data is saved to an external file so it persists between runs.

---

##  Features

- **Create Account** - Open a Savings or Current account with custom settings
- **Deposit & Withdraw** - Perform transactions with validation checks
- **Interest Rate** - Savings accounts support manually set interest rates
- **Overdraft Control** - Current accounts allow controlled over-withdrawal up to a set limit
- **Balance Check** - View current account balance anytime
- **Transaction History** - View all past deposits and withdrawals
- **Data Persistence** - All account data is saved and loaded from an external `.txt` file

---

##  OOP Concepts Used

| Concept | How it is used |
|---|---|
| **Encapsulation** | All attributes are private using `__` to prevent direct access |
| **Inheritance** | `SavingsAccount` and `CurrentAccount` inherit from base `Account` class |
| **Polymorphism** | Both subclasses override `withdraw()` with their own rules |
| **Abstraction** | `Bank` class manages accounts without knowing their internal details |

---

##  Project Structure

```
CLI_Banking_System/
│
├── bank.py          # Main program file
└── bank_data.txt    # Auto-generated data file (created on first run)
```

### Classes Overview

| Class | Description |
|---|---|
| `Account` | Base class — defines core banking attributes and methods |
| `SavingsAccount` | Inherits from Account — adds interest rate support |
| `CurrentAccount` | Inherits from Account — adds overdraft limit control |
| `Bank` | Manager class — handles all accounts, file saving and loading |

---

## How to Run

### Requirements
- Python 3.x installed
- VS Code (recommended)

### Steps

1. Clone or download the project
2. Open the project folder in VS Code
3. Open `bank.py`
4. Press `Ctrl + F5` to run without debugging

### Or run from terminal:
```bash
python bank.py
```

---

##  Menu Options

```
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. View Transaction History
6. Exit
```

---

##  Example Usage

```
Enter Choice: 1
Enter name: Alice
Enter initial balance: 5000
Enter type (savings/current): savings
Enter interest rate: 4
Account created: ACC1000

Enter Choice: 2
Enter account number: ACC1000
Enter amount: 2000
Deposited successfully!

Enter Choice: 4
Enter account number: ACC1000
Balance: 7000
```

---

##  Author

Built from scratch as a Python OOP learning project.  
Concepts practised: Classes, Inheritance, Encapsulation, Polymorphism, File Handling.
