class BankAccount:

  def __init__(self, first_name, last_name,bank,phone_number):
    self.first_name=first_name
    self.last_name=last_name
    self.bank=bank
     self.phone_number=phone_number
    self.loans=0
    self.balance=0
    self.deposits=[]
    self.withdrawals=[]
    
   

  def account_name(self):
    name=("{} account for {} {}".format(
      self.bank, self.first_name, self.last_name))
    return name
  def deposit(self, amount):
    self.balance +=amount
    print("You have deposited {} to your account".format(amount))
  def withdraw(self, amount):
    self.balance -=amount
    print("A withdrawal of {} has been made from your account".format(amount))
    
  def get_balance(self):
    return "The balance for {} is {}".format(self.account_name(), self.balance)

  def show_withdrawal_statements(self):
    for withdrawal in self.withdrawals:
   print(withdrawal)

  def show_deposit_statement(self):
    for deposit in self.deposits
    print(deposits)

  def request_loan(self,amount):
    if amount <= 0:
      print("You cannot request a loan of that amount")
    else:
      self.loan = amount
      print("You have been given a loan of {}".format(amount))  

    
  def repay_loan(self,amount):
    if amount <= 0:
      print("You cannot repay with that amount")
    elif self.loan == 0:
      print("You don't have a loan at the amount")
    elif  amount > self.loan:
      print("Your loan is{}, please enter an amount that is less or equal".format(self.loan))
    else:
      self.loan -= amount
      print("You have repaid your loan with {}. Your loan balance is {}".format(amount,self.loan))     



