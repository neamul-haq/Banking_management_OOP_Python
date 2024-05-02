from Bank import Bank
from User import User
from Admin import Admin

def main():
    dbbl = Bank('dbbl')
    neam = User('neam12@gmail.com', 12345)
    nil = User('nil2@gmail.com', 1245)
    neam.create_account(dbbl)
    nil.create_account(dbbl)
    neam.deposit(5000,dbbl)
    neam.withdraw(2000, dbbl)
    neam.my_balance()
    neam.transfer(nil, 2500)
    # neam.take_loan(1200, dbbl)
    # neam.take_loan(800, dbbl)
    # neam.deposit(5000,dbbl)
    # neam.take_loan(800, dbbl)
    neam.transfer(nil,4000)
    
    admin = Admin('rokibul@gmail.com',456677)
    admin.create_account(dbbl)
    admin.total_bank_balance()
    admin.total_bank_loan()
    admin.loan_feature(False)
    print(dbbl.get_loan_feature)
    neam.take_loan(200,dbbl)
    
    print(neam)
    print(nil)
    print(dbbl)

if __name__ == '__main__':
    main()