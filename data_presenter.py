invoices = open("CupcakeInvoices.csv")

# Open the CupcakeInvoices.csv.

# Loop through all the data and print each row.

# Loop through all the data and print the type of cupcakes purchased.
# for invoice in invoices:
#     print(invoice)
#     print(invoice.split(",")[2])

# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

# for invoice in invoices:
#     print(invoice.split(",")[4])

# Loop through all the data, and print out the total for all invoices combined.

total = 0
for invoice in invoices:
    total += float(invoice.split(",")[3])
print(total)

# Close your open file.

invoices.close()
