#Bank Statement
class Account:
    def __init__(self,username,password,amount):
        self.username = username
        self.password = password
        self.amount = amount
    
    def __repr__(self):
        return f"Account({self.username},{self.amount})"


class Banking:
    def __init__(self):
        self.accounts = []

    def create_account(self,username,password,amount):
        for i in self.accounts:
            if i.username == username:
                return "Username already exists"
        

        new = Account(username,password,amount)
        self.accounts.append(new)
        return "Account created successfully"

    
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
            return "Withdrawn " + str(amount) + " Sucessfully"
        else:
            return "Invalid amount"
        

    def deposit(self, username,password,amount):
        account = self.get_account(username,password)
        if account == False:
            return "Invalid Username/Password"
        
        if amount > 0:
            account.amount += amount
            return "Deposited " + str(amount) +  " Successfully" + " to the account " + str(account.username)
        else:
            return "Invalid Amount"
        
BANK = Banking()

output = BANK.create_account(username = "Divyanshu", password = "abcytr24", amount = 100000)
print(output)

output = BANK.deposit(username = "Divyanshu", password = "abcytr24" , amount = 2000)
print(output)

output = BANK.withdraw(username = "Divyanshu", password = "abcytr24", amount = 5000)
print(output)




            
            

    
