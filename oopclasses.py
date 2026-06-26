class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance
        
    def deposit(self, amount):
        self.balance += amount
        print("Deposited", amount, "New balance is", self.balance)

    def withdraw(self, amount):
        if self.balance > 0 and self.balance >= amount: 
            self.balance -= amount
            print("Withdrew", amount, "New balance is", self.balance)
        else:
            print("Insufficient funds. Cannot withdraw.")
    def get_balance(self):
        return self.balance


   
# 1. Create an instance (a real account)
# We pass "Alice" and 100 to the __init__ method
my_account = BankAccount("Alice", 1)

# 2. Call the methods using the "dot" notation
my_account.deposit(50)    
my_account.withdraw(70)   

# 3. Access the data
# We store the return value of get_balance() in a variable
current_money = my_account.get_balance()

print("Final balance for", my_account.owner, "is:", current_money)