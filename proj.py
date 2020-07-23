import module as m
def main():
    print("Welcome!")
    print("Here is our menu: ")
    print("1. Cauliflower Bruschetta")
    print("2. Mariachi™ Chicken")
    print("3. Hot Chicken")
    print("4. Pepperoni")
    print("5. Serious Cheese™")
    print("6. Ultimate 4 Cheese")
    print("7. The Works™")
    print("8. Founder's Favorite®")
    print("9. Classic Trio®")
    print("10. Very Vegy™")
    print("11. Serious Meat™")
    print("12. Hawaiian™")
    print("13. Margherita")
    print("14. Mariachi Beef®")
    choice=int(input("Enter your choice (1-14): "))
    size=str(input("Enter the size (small, medium, large): "))
    amount=int(input("Enter the amount: "))
    distance=int(input("Enter the distance (in miles): "))
    name=str(input("Enter your name: "))
    if(size=="small"):
        initial=6.19*amount
        price=m.price(initial,distance)
        coupons=m.coupons(price)
        print("Your total is: $",price)
        print("Congrats, you additionally received a",coupons)
    elif(size=="medium"):
        initial=14.59*amount
        price=m.price(initial,distance)
        coupons=m.coupons(price)
        print("Your total is: $",price)
        print("Congrats, you additionally received a",coupons)
    elif(size=="large"):
        initial=17.29*amount
        price=m.price(initial,distance)
        coupons=m.coupons(price)
        print("Your total is: $",price)
        print("Congrats, you additionally received a",coupons)
    else:
        print("Sorry, your information was not entered correctly. Your order will be restarted.")
        print("")
        main()
main()
def second():
    more=str(input("Would you like anything else? "))
    if(more=="yes"):
        main()
        second()
    elif(more=="no"):
        print("Thanks for ordering and have a nice day!")
    else:
        print("Please type 'yes' or 'no'.")
        print("")
        second()
second()
