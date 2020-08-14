#Bank Statement
class Account:
    def __init__(self,username,password,amount,accountId):
        self.username = username
        self.password = password
        self.amount = amount
        self.accountId = accountId
    
    # def __repr__(self):
    #     return f"Account({self.username},{self.amount})"


class Banking:
    def __init__(self):
        self.accounts = []

    def create_account(self,username,password,amount,accountId):
        for i in self.accounts:
            if i.username == username or i.accountId == accountId:
                return "Username already exists"
        

        new = Account(username,password,amount,accountId)
        self.accounts.append(new)
        print("\n--------Account created successfully--------\n")
        print("\tAccount Name:     " + new.username )
        print("\tAccount Id:       " + str(new.accountId))
        return "\tBalance:          " + str(new.amount)
        
                

    
    def get_account(self, username, password,accountId):
        for i in self.accounts:
            if i.username == username and i.password == password or i.accountId == accountId:
                return i
             
        return False
    
    def withdraw(self,username,password,amount,accountId):
        account = self.get_account(username,password,accountId)
        if account == False:
            return "Invalid Username/Password"
        
        if amount > account.amount:
            return "Insufficient funds"
        
        if amount > 0:
            account.amount -= amount
            return "\tWithdrawn:        " + str(amount) 
        else:
            return "Invalid amount"
        

    def deposit(self, username,password,amount,accountId):
        account = self.get_account(username,password,accountId)
        if account == False:
            return "Invalid Username/Password"
        
        if amount > 0:
            account.amount += amount
            return "\tDeposited:        " + str(amount) 
        else:
            return "Invalid Amount"

    def balance(self,username,password,accountId):
        account = self.get_account(username,password,accountId)
        if account == False:
            return "Invalid Username/Password"
        
        for i in self.accounts:
            if i.username == username and i.password == password:
                return "\tBalance:          " + str(account.amount)

        
BANK = Banking()

acc1 = BANK.create_account(username = "Divyanshu", password = "abcytr24", amount = 100000, accountId = 1234567)
print(acc1)

acc1 = BANK.deposit("Divyanshu","abcytr24" , 2000, 1234567)
print(acc1)

acc1 = BANK.withdraw("Divyanshu","abcytr24",5000, 1234567)
print(acc1)

print("-----------------------------------")
acc1 = BANK.balance("Divyanshu","abcytr24", 1234567)
print(acc1)
# -----------------------------------------------------------

acc2 = BANK.create_account(username = "Divyanshu Soni", password = "abcygege4", amount = 10445500, accountId = 234567)
print(acc2)

acc2 = BANK.deposit("Divyanshu Soni","abcygege4" , 232000, 234567)
print(acc2)

acc2 = BANK.withdraw("Divyanshu Soni","abcygege4",5675000, 234567)
print(acc2)
print("-----------------------------------")

acc2 = BANK.balance("Divyanshu Soni","abcygege4", 234567)
print(acc2)





            
            

    
