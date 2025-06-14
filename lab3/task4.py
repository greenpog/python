class BankAccount:
    def __init__(self):
        self._balance=0 #приватный по соглашению
        self._transactions=[]
    
    def deposit(self, num):
        self._balance+=num
        self._transactions.append(num)

    def withdraw(self, num):
        if self._balance>=num:
            self._balance-=num
            self._transactions.append(num)
        else: print("Не хватает средств.")

    @property
    def balance(self):
        return self._balance
    
count=BankAccount()
print(count.balance)
count.deposit(15)
count.withdraw(20)
count.withdraw(10)
print(count.balance)