class Admin:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.bank = None
    
    def create_account(self, bank):
        self.bank = bank
        bank.add_admin(self)
    
    def total_bank_balance(self):
        current_amount = self.bank.get_current_amount
        print(f'Total balance of {self.bank.name} is {current_amount}')
    
    def total_bank_loan(self):
        print(f'Total loan amount of {self.bank.name} is {self.bank.get_loan_amount()}')
    
    def loan_feature(self, possible):
        self.bank.set_loan_feature = possible
    
    