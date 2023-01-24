price_child = float(input("What is the price of a child's meal?"))
price_aduld = float(input("What is the price of an adult's meal?"))
children = int(input("How many children are there?"))
adults = int(input("How many adults are there?"))
sale_rate = float (input("What is the sales tax rate?"))
soma1 = children * price_child
soma2 = adults * price_aduld
subtotal = soma1 + soma2
sale_tax = subtotal * sale_rate / 100
total = subtotal + sale_tax
print()
print(f"Subtotal: ${round(subtotal,2)}")
print(f"Sale tax: ${round(sale_tax,2)}")
print(f"total: ${round(total,2)}")
print()
payment_amount = int(input("What is the payment amount?"))
change = payment_amount - total
print(f"Change: ${round(change,2)}")
