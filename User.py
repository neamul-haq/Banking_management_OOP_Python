class User:
    def __init__(self,email, password) -> None:
        self.email = email
        self.password = password
        self.bank_money = 0
        self.loan_amount = 0
        self.transaction_history = []
    
    def create_account(self, bank):
        bank.add_user(self)
        
    def deposit(self, amount, bank):
        self.bank_money += amount
        bank.add_money(amount)
        self.transaction_history.append(f'deposit {amount} TK')
        
    
    def withdraw(self, amount, bank):
        if amount>self.bank_money:
            print('Sorry! You dont have enough money')
        else:
            ok = bank.remove_money(amount)
            if ok:
                self.bank_money -= amount
                self.transaction_history.append(f'Withdraw {amount} TK')
                
    def my_balance(self):
        print(f'Your bank balace is {self.bank_money}')
    
    def transfer(self, receiver, amount):
        
        if amount > self.bank_money:
            print('You dont have enough money to transfer')
        else:
            self.bank_money -= amount
            receiver.bank_money += amount
            self.transaction_history.append(f'Transfer {amount} TK')
            print(f'Your {amount} tk transfer successful')
        
    
    def show_transaction_history(self):
        print('-----Transaction History ------')
        for history in self.transaction_history:
            print(history)
    
    def take_loan(self, amount, bank):
        if bank.get_loan_feature == False:
            print('Sorry! Bank is not interested to loan')
            return
        elif self.loan_amount:
            print('Sorry you still have loan')
            return
        if amount > 2*self.bank_money:
            print('Sorry! You are not eligible for this Loan')
        elif amount > bank.get_current_amount:
            print('Bank doesnt have enough money')
        else:
            ok = bank.remove_money(amount)
            if ok:
                self.loan_amount += amount
                print('your loan request granted successfully!')
                bank.loan_amount_calculate(amount)
                self.transaction_history.append(f'Take loan {amount} TK')
                
                
    def __repr__(self) -> str:
        print(f'User: {self.email}')
        print(f'Users bank money: {self.bank_money}')
        print(f'Users loan amount: {self.loan_amount}')
        self.show_transaction_history()
        return ''

    
    