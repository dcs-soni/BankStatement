#Bank Statement
class Account:
    def __init__(self,username,password,amount):
        self.username = username
        self.password = password
        self.amount = amount
    
    def __repr__(self):
        return f"Account({self.username},{self.amount})"


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self,username,password,amount):
        for i in self.accounts:
            if i.username == username:
                return "Username already exists"
        

        new = Account(username,password,amount)
        self.accounts.append(new)
        return "Account created successfully"

    
