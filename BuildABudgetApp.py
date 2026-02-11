class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount,
        'description': description})
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount,
        'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        
        return False
    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
    
    # 2. Format the Ledger Items
        items = ""
        for entry in self.ledger:
        # Slice description to 23 chars and left-align
            desc = f"{entry['description'][:23]:23}"
        # Format amount to 2 decimal places and right-align in 7 chars
            amt = f"{entry['amount']:>7.2f}"
        
            items += f"{desc}{amt}\n"
    
    # 3. Add the Total Line
        total = f"Total: {self.get_balance():.2f}"
    
        return title + items + total
def create_spend_chart(categories):
    # title = f"Percentage spent by category"

    spent_amounts = []
    for cat in categories:
        spent = sum(abs(item["amount"]) for item in cat.ledger if item["amount"] < 0)
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)
    
    # Calculate percentages rounded down to nearest 10
    # Use (spent / total) * 100
    percentages = [int((amount / total_spent) * 100 // 10) * 10 for amount in spent_amounts]

    # 2. Build the chart top-down
    res = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "| "
        for p in percentages:
            if p >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    # 3. Add horizontal line
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 4. Build vertical names
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name for cat in categories]
    
    for i in range(max_len):
        res += "     "
        for name in names:
            if i < len(name):
                res += name[i] + "  "
            else:
                res += "   "
        if i < max_len - 1:
            res += "\n"
            
    return res
