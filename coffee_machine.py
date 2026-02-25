import menu 

 

money = 0 

def report() :
    
    print(f"water: {menu.resources["water"]}ml")
    print(f"milk: {menu.resources["milk"]}ml")
    print(f"coffee: {menu.resources["coffee"]}g")
    print(f"money: {money}")
    

# def check_resources(order):
#     for item in menu.MENU :
#         if order == "espresso":
#             for ingredient in menu.MENU[es]
def check_resources(order):
    need_resources = False
    for item in menu.MENU :
        if order == item :
            # print(f"so you want a {item}")
            for ingredient in menu.MENU[item]["ingredients"]:
                # print(menu.MENU[item]["ingredients"][ingredient])
                if menu.MENU[item]["ingredients"][ingredient] > menu.resources[ingredient]:
                    print(f"you don't have enough {ingredient}")
                    need_resources = True;
    return need_resources         

def process_coins():
   print("enter your money in quarters, dimes, nickels, and pennies: ")
   quarters = input("how many quartes?: ")
   dimes = input("how many dimes?: ")
   nickles = input("how many nickles?: ")
   pennies =  input("how many pennies?: ")
   print(quarters,dimes,nickles,pennies)
   
def use_machine():
    user_input  = input("what would you like? (espresso/capuccino/latte): ").lower()
    if user_input == "report":
        report()
    elif user_input == "off":
        return
    else:
        check_resources(order = user_input)
        process_coins()
        #see how you can print True or False from need_resources without having to see the print ouput of the function 
        # print(f"need resources = {check_resources(order = user_input)}")
    use_machine()





use_machine()
