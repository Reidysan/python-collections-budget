from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

spending_catergories = []
for expense in expenses.list:
    spending_catergories.append(expense.category)

spending_counter = collections.Counter(spending_catergories)

top5 = spending_counter.most_common(5)

catergories, count = zip(*top5)

fig, ax = plt.subplots()

ax.bar(catergories, count)
ax.set_title("# of Purchases by Category")

plt.show()
