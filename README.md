# AMIT-Python-project

The project should achive this consepts :

1. Modularity The project is organized into several modules to handle different parts of the bank account management system : you can go ahead as the files which mentioned before

2. Encapsulation The project utilizes encapsulation to keep the account information private and to prevent unauthorized access. The properties of the Account class are declared as private and can only be accessed through public methods.

3. Inheritance The project utilizes inheritance to create specialized account types that inherit from a base Account class. The CheckingAccount and SavingsAccount classes inherit properties and methods from the Account class, and can also override and extend them as needed.

4. Polymorphism The project utilizes polymorphism to allow the Bank class to manage a collection of accounts of different types. The add_account() method can accept instances of Account, CheckingAccount, and SavingsAccount, and the search_accounts() method can return instances of any of these types.

5. Operator Overloading The project utilizes operator overloading to allow for mathematical operations to be performed on account balances. The **add**() and **sub**() methods are defined in the Account class to allow for addition and subtraction of account balances.
