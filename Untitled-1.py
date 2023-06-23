class BankAccount:
    def set_details(self,name,balance):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

p1 = BankAccount()
p2 = BankAccount()

p1.set_details('Cierra',500)
p1.display()
p1.withdraw(20)
p1.deposit(50)
p2.set_details('Person', 200)
p2.display()
p2.withdraw(20)
p2.deposit(50)

