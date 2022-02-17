from tkinter import font
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("_mpl-gallery")

invoices = open("CupcakeInvoices.csv")

totals = {
    "Chocolate": 0,
    "Vanilla": 0,
    "Strawberry": 0
}

for invoice in invoices:
    line = invoice.split(",")
    totals[line[2]] += float(line[3]) * float(line[4])
print(totals)

# Close your open file.
invoices.close()

fig, ax = plt.subplots()

# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

x_pos = np.arange(len(totals))
ax.bar(x_pos, totals.values(), color=[(.42, .25, .15 ,1), 'beige', 'pink'], edgecolor="black")
ax.set_xticks(x_pos, labels=totals.keys())
ax.set_ylim(0, 450)
ax.set_yticks(np.arange(0, 450, 50))

font1 = {'family': 'sans-serif', 'color': 'black', 'size': 18}

ax.set_title("Cupcake Sales", fontdict = font1)
ax.set_xlabel('Flavor', fontdict = font1)
ax.set_ylabel('Sales ($)', fontdict = font1)
    
plt.tight_layout()
plt.show()