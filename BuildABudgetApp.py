class Category:

    def __init__(self, name, ledger):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount,
        'description': description})
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            ledger.append({'amount': -amount,
        'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = self.deposit.amount - self.withdraw.amount
        return balance
    def transfer(self, amount, category_instance):
        if self.withdraw(amount, f"Transfer to {category_instance.name}"):
            category_instance.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    def check_funds(self, amount):
        if amount > self.get_balance():
            return True
        return False
def create_spend_chart(categories):
    print("")
