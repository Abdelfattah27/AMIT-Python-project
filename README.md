# AMIT-Python-project

The bank project is an example of a software system designed to manage customers' bank accounts. The system is built using Python and uses various OOP concepts such as encapsulation, inheritance, polymorphism, and operator overloading to ensure code modularity, reusability, and flexibility.

The project consists of several classes, including the Account class, which serves as the parent class for various types of bank accounts such as checking, savings, and credit card accounts. Each account type inherits the common properties and behaviors of the Account class but also has unique features and methods specific to its type.

The project should achieve this conceptss :

1. Modularity The project is organized into several modules to handle different parts of the bank account management system

   - account.py: defines the Account class and its properties and methods.
   - checking_account.py: defines the CheckingAccount class which is a subclass of Account and has additional properties and methods specific to a checking account.
   - savings_account.py: defines the SavingsAccount class which is a subclass of Account and has additional properties and methods specific to a savings account.
   - bank.py: defines the Bank class which manages a collection of accounts, and provides methods to add, remove, and search for accounts, as well as to deposit, withdraw, and transfer funds between accounts.
   - view.py : defines all the ui the user see and handles all transactions made on the bank by customers such as CRUD operations on bank account

2. Encapsulation The project utilizes encapsulation to keep the account information private and to prevent unauthorized access. The properties of the Account class are declared as private and can only be accessed through public methods.

3. Inheritance The project utilizes inheritance to create specialized account types that inherit from a base Account class. The CheckingAccount and SavingsAccount classes inherit properties and methods from the Account class, and can also override and extend them as needed.

4. Polymorphism The project utilizes polymorphism to allow the Bank class to manage a collection of accounts of different types. The add_account() method can accept instances of Account, CheckingAccount, and SavingsAccount, and the search_accounts() method can return instances of any of these types.

5. Operator Overloading The project utilizes operator overloading to allow for mathematical operations to be performed on account balances. The **add**() and **sub**() methods are defined in the Account class to allow for addition and subtraction of account balances.
