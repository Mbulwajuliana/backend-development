class BankAccount:

  def __init__(self, first_name, last_name,bank,phone_number):
    self.first_name=first_name
    self.last_name=last_name
    self.bank=bank
    self.balance=0
    self.withdrawals=[]
    self.deposits=[]
    self.phone_number=phone_number
    self.loans=0

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
  def withdrawal_statement(self):
    self.withdrawals=self.withdrawals.append(withdraw)
    return self.withdrawals
  def deposit_statement(self):
    self.deposits=self.deposits.append(deposit)
    return self.deposits  

  def give_loan(self,amount):
      print("Recieve a loan of {}".format(amount))
      self.loans=self.loans + amount
  def repay_loan(self,amount):
    self.repay=self.loan - amount
      print("Repayed a loan of {}".format(amount))



