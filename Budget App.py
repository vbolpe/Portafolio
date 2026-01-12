class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]              
            amount = f"{entry['amount']:.2f}"             
            items += f"{desc:<23}{amount:>7}\n"          
        total_line = f"Total: {self.get_balance():.2f}"
        return title + items + total_line
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

def create_spend_chart(categories):
    spent_per_category = []
    total_spent = 0

    for cat in categories:
        spent = 0
        for entry in cat.ledger:
            if entry["amount"] < 0:
                spent += -entry["amount"]  # convertir a positivo
        spent_per_category.append(spent)
        total_spent += spent
    percentages = []
    for spent in spent_per_category:
        pct = (spent / total_spent) * 100 if total_spent != 0 else 0
        pct_rounded = int(pct // 10) * 10
        percentages.append(pct_rounded)
    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for pct in percentages:
            chart += "o  " if pct >= level else "   "
        chart += "\n"
    chart += "    -" + "---" * len(categories) + "\n"
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += (name[i] + "  ") if i < len(name) else "   "
        chart += "\n"
    return chart.rstrip("\n")

def main():
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)
if __name__ == "__main__":
    main()
