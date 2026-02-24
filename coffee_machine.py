import menu 

# print(menu.MENU["latte"])
# print(menu.resources)

def use_machine():
    user_input  = input("what would you like? ").lower()
    if user_input == "report":
        print("make a function that prints the report and put it here")
    elif user_input == "off":
        return
    use_machine()
use_machine()