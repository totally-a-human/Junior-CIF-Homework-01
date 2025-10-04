print("Welcome to our Lily's Cat Café! \n ------------------------------- \n ----Here's our menu!---- ")
menu=["1. Iced Coffee" , "2. Iced Latte" , "3. Iced Matcha Latte", "4. Iced Macchiato", "5. Cold Brew Coffee" , "6.Hot Tea" , "7. Black Coffee" , "8. Latte" , "9.Matcha Latte"]

print("Welcome to our Lily's Cat Café! \n ------------------------------- \n ----Here's our menu!---- ")
menu=["1. Iced Coffee" , "2. Iced Latte" , "3. Iced Matcha Latte", "4. Iced Macchiato", "5. Cold Brew Coffee" , "6.Hot Tea" , "7. Black Coffee" , "8. Latte" , "9. Matcha Latte" , "10. Mocha" , "11. Hot Chocolate"]
print(menu)
costs=["1. - $3.00" , "2. - $3.50" , "3. - $3.50" , "4. - $3.50" , "5. - $2.50" , "6. - $1.00" , "7. - $1.50" , "8. - $2.00" , "9. - $2.00" , "10. - $2.00" , "11. - $1.50"]
print(costs)
costs=["3.00" , "3.50" , "3.50" , "3.50" , "2.50" , "1.00" , "1.50" , "2.00" , "2.00" , "2.00" , "1.50"]

print("----------------------------------------------------------------------------------------------------------------------------")
coupon=input("Before we start, do you have a coupon you wish to use? \nOh? Your new? Well, we offer a 10% discount to new shoppers! The code is 'ILOVECATS'")
if coupon == "ILOVECATS":
    coupon=0.9
else:
    coupon=1
print("----------------------------------------------------------------------------------------------------------------------------")

answer="yes"

total=0
    
while answer == "yes":
    item=input("Which item on the menu would you like to buy? Please put in that number")
    qty=int(input("How much would you like to buy?"))
    item=int(item)
    price=float(costs[item])
    subtotal=(price*qty*coupon)
    print("Thank you for buying from Lily's Cat café!\n,your total is", subtotal ,"!")
    total=total+subtotal
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("you just ordered",qty,"of ",item,"your subtotal is",subtotal)
    answer=input("Would you like to add anything else? \n(Yes|No)")
    print("Your total is",total)

print("----------------------------------------------------------------------------------------------------------------------------")
payment=input("How would you like to pay?")
if payment == "credit" or "debit" or "cash":
    payment=("Your payment is valid!")
else: ("Sorry your payment is invalid")
print(payment)
print("----------------------------------------------------------------------------------------------------------------------------")
print("--Thank you for shopping with us!--")
