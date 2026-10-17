class bankaccount:
    def __init__(self,account_holder,init_balance,deposit_amount,withdrawl_amount):
        self.account_holder=account_holder
        self.init_balance=init_balance
        self.deposit_amount=deposit_amount
        self.withdrawl_amount=withdrawl_amount

account_holder=input("enter name:")
init_balance=float(input("enter initial balance:"))
deposit_amount=float(input("enter deposit amount:"))
withdrawl_amount=float(input("enter withdrawl amount:"))

account_details=bankaccount(account_holder,init_balance,deposit_amount,withdrawl_amount)
final_balance=account_details.init_balance+account_details.deposit_amount-account_details.withdrawl_amount

print("\naccount holder:{}".format(account_details.account_holder))
print("final balance={}".format(final_balance))