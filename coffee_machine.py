import menu 

# print(menu.MENU["latte"])
# print(menu.resources)

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
    for item in menu.MENU :
        if order == item :
            print(f"so you want a {item}")
            for ingredient in menu.MENU[item]["ingredients"]:
                print(menu.MENU[item]["ingredients"][ingredient])
                if menu.MENU[item]["ingredients"][ingredient] > menu.resources[ingredient]:
                    print(f"you don't have enough {ingredient}")    
            else: 
                print(f"you have enough resources for a {item}")
            # think of where to return true so that this function can trigger the next one 
                 

def use_machine():
    user_input  = input("what would you like? ").lower()
    if user_input == "report":
        report()
    elif user_input == "off":
        return
    else:
        check_resources(order = user_input)
    use_machine()


use_machine()