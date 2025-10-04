print("Welcome to our Lily's Cat Café! \n ------------------------------- ")

time=int(input("We charge $10 per hour for your stay, how long would you like to stay?"))
total=(time*10)
print("Great! Your current total is",total,"what drinks would you like to purchase?\n -------Here's our menu!------- ")

menu=["Iced Coffee" , "Iced Latte" , "Iced Matcha Latte", "Iced Macchiato", "Cold Brew Coffee" , "Hot Tea" , "Black Coffee" , "Latte" , "Matcha Latte" , "Mocha" , "Hot Chocolate"]
costs=["3" , "3.5" , "3.5" , "3.5" , "2.5" , "1.0" , "1.5" , "2.0" , "2" , "1" , "1.5"]

y=0
for i in menu: 
    print(y+1,".",menu[y],"-",costs[y])
    y+=1

print("----------------------------------------------------------------------------------------------------------------------------")
coupon=input("Before we start, do you have a coupon you wish to use? \nOh? Your new? Well, we offer a 10% discount to new shoppers! The code is 'ILOVECATS'")
if coupon == "ILOVECATS":
    coupon=0.9
else:
    coupon=1
print("----------------------------------------------------------------------------------------------------------------------------")

answer="yes"

    
while answer == "yes":
    item=input("Which item on the menu would you like to buy? Please put in that number")
    qty=int(input("How much would you like to buy?"))
    item=int(item)
    price=float(costs[item])
    subtotal=(price*qty*coupon)
    print("Thank you for buying from Lily's Cat café!\n,your total is", subtotal ,"!")
    total=total+subtotal
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("you just ordered",qty,"of ",menu[item-1],"your subtotal is",subtotal)
    answer=input("Would you like to add anything else? \n(Yes|No)")
    print("Your total is",total)

print("----------------------------------------------------------------------------------------------------------------------------")
payment=input("How would you like to pay?")
if payment == "credit" or "credit card" or "debit" or "debit card" or "cash":
    payment=("Your payment is valid!")
else: ("Sorry your payment is invalid")
print(payment)
print("----------------------------------------------------------------------------------------------------------------------------")
print("--Thank you for shopping with us!--")
