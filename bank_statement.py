#Bank Statement
class Account:
    def __init__(self,username,password,amount):
        self.username = username
        self.password = password
        self.amount = amount
    
    # def __repr__(self):
    #     return f"Account({self.username},{self.amount})"


class Banking:
    def __init__(self):
        self.accounts = []

    def create_account(self,username,password,amount):
        for i in self.accounts:
            if i.username == username:
                return "Username already exists"
        

        new = Account(username,password,amount)
        self.accounts.append(new)
        print("\n--------Account created successfully--------\n")
        print("\tAccount Name:     " + new.username )
        return "\tBalance:          " + str(new.amount)
        
                

    
    def get_account(self, username, password):
        for i in self.accounts:
            if i.username == username and i.password == password:
                return i
            
        return False
    
    def withdraw(self,username,password,amount):
        account = self.get_account(username,password)
        if account == False:
            return "Invalid Username/Password"
        
        if amount > account.amount:
            return "Insufficient funds"
        
        if amount > 0:
            account.amount -= amount
            return "\tWithdrawn:        " + str(amount) 
        else:
            return "Invalid amount"
        

    def deposit(self, username,password,amount):
        account = self.get_account(username,password)
        if account == False:
            return "Invalid Username/Password"
        
        if amount > 0:
            account.amount += amount
            return "\tDeposited:        " + str(amount) 
        else:
            return "Invalid Amount"

    def balance(self,username,password):
        account = self.get_account(username,password)
        if account == False:
            return "Invalid Username/Password"
        
        for i in self.accounts:
            if i.username == username and i.password == password:
                return "Balance in the account " + str(account.username) + " is " + str(account.amount)

        
BANK = Banking()

output = BANK.create_account(username = "Divyanshu", password = "abcytr24", amount = 100000)
print(output)

output = BANK.deposit("Divyanshu","abcytr24" , 2000)
print(output)

output = BANK.withdraw("Divyanshu","abcytr24",5000)
print(output)
print("-----------------------------------")

output = BANK.balance("Divyanshu","abcytr24")
print(output)


output = BANK.create_account(username = "Divyanshu Soni", password = "abcygege4", amount = 10445500)
print(output)

output = BANK.deposit("Divyanshu Soni","abcygege4" , 232000)
print(output)

output = BANK.withdraw("Divyanshu Soni","abcygege4",5675000)
print(output)
print()

output = BANK.balance("Divyanshu Soni","abcygege4")
print(output)





            
            

    
