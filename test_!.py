products = {
"Laptops": {"price £": 800, "quantity in stock ": 10},
"Phones": {"price £": 500, "quantity in stock": 15},
"Monitors": {"price £": 300, "quantity in stock": 10,},
}    
# Company's account balance
account_balance = 1000
# Recorded sales and purchases
sales = []
purchases = []



while True:
    #display commands 
    print("\n\nWelcome\nChose one of the following options\n")
    print("(1)balance")
    print("(2)sale")
    print("(3)purchase")
    print("(4)account")
    print("(5)list")
    print("(6)warehouse")
    print("(7)review")
    print("(8)end\n")
   #prompt for command
    user_input = input("Enter command :  ")
    if user_input == 'balance':
                print(f"Your curent balance is :{account_balance}")
                prtint_action = (input(f"Do you want to add or substract?: "))
                amount_of_money = float(input("Enter amount to add: "))
                if prtint_action == 'add':
                        account_balance = amount_of_money + account_balance
                        print(f"Your new Total balace is={account_balance}")
                        continue
                elif prtint_action == 'substract':
                        account_balance = amount_of_money - account_balance
                        print(f"Your new Total balace ={account_balance}")
                        continue
                elif account_balance <= 0:
                        print("Balance not enough add more!")
                        break

    elif user_input == "sale":
                for item, details in products.items():
                        print(f"\n{item.capitalize()}: ")
                        for detail, value in details.items():
                                print(f"- {detail.capitalize()}: {value}")
                print(input("\nEnter product name : "))
                quantity_bought = int(input("Enter quantity : "))
                items_bought = quantity_bought * details["price £"]

                print(f"\nYour order has ben placed\nTotal amount : {items_bought}£")
                if items_bought == account_balance:
                        print(f"\nYour order has ben placed\nTotal amount : {items_bought}")
                        continue
                elif items_bought > account_balance:
                        print("Not enough money!")
                        continue
                elif items_bought < details["quantity in stock"]:
                        print("Not enough items in stock")
                        continue