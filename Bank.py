class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.__current_amount = 0
        self.__loan_amount = 0
        self.__loan_feature = True
        self.__users = {}
        self.__admins = {}
        
    def add_user(self, user):
        self.__users[user.email] = user.password
    
    def add_admin(self,admin):
        self.__admins[admin.email] = admin.password
        
    def add_money(self, amount):
        self.__current_amount += amount
        
    def remove_money(self, amount):
        if amount > self.__current_amount:
            print('sorry bank is bankrupt!')
            return False
        else:
            self.__current_amount -= amount
            return True
    @property  
    def get_current_amount(self):
        return self.__current_amount
    
    def loan_amount_calculate(self,amount):
        self.__loan_amount += amount
    
    def get_loan_amount(self):
        return self.__loan_amount
    
    @property
    def get_loan_feature(self):
        return self.__loan_feature
    
    @get_loan_feature.setter
    def set_loan_feature(self, possible):
        self.__loan_feature = possible
        
    def __repr__(self) -> str:
        print(f'----Bank name: {self.name}---')
        print(f'Bank current amount : {self.__current_amount}')
        print(f'Bank loan amount : {self.__loan_amount}')
        print(f'Bank loan feature : {self.__loan_feature}')
        print('-----users------')
        for user in self.__users:
            print(user)
        print('-----Admins------')
        for admin in self.__admins:
            print(admin)
        return ''
        