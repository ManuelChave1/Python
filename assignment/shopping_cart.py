cart = {} 
print("Welcome to the Shopping Cart Program!")
 
while True:
    print()
    print ("Please select one of the following:")
    print ("1. Add item ")
    print ("2. View cart ")
    print ("3. Remove Item ")
    print ("4. compute total")
    print ("5. Quit")
  
    select = int(input(" Please enter an action: "))
 
    if select == 1:
        item = input(" What item would you like to add?  ")
        price = float(input("What is the price of the item? "))
        cart [item] = price
        print(f"'{item}' has been added to the cart.")
 
    if select == 2:
        print("The contents of the shopping card are:")
        for item in cart:
            print(f"  {item} - ${cart [item]:.2f}")
 
    if select == 3:
        leave_the_program = input("Which item would you like to remove?  ")
        cart.pop(leave_the_program)
        print("Item removed")

    if select == 4:
        total = 0
        for item in cart:
            total += cart [item]
        print(f"The total price of the items in the shopping cart is: ${total:.2f} !")
 
    if select == 5:
        print ("Thank you. Goodbye!")
        break
    