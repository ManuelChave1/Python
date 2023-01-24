friends = ["Luc", "Kristi", "Rex",]
tips = [12.25, 13.95, 8.50]

running_total = 0

for tips_amount in tips: 
    running_total += tips_amount
print(f"The total is {running_total:.2f}")