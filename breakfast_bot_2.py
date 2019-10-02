import time

options = ['waffles','pancakes','yes','no']

def print_pause(string):
    print(string)
    time.sleep(1)

def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
            #break
        print_pause("Sorry, I don\'t understand.")

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def get_order():
    response = valid_input("Please place your order."
                           " Would you like waffles or pancakes?\n", options)
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")


def order_again():
    response = valid_input("Would you like to order again? Please enter Yes or No\n",options)
    if 'no' in response:
        print_pause("Ok, goodbye")
    elif 'yes' in response:
        print_pause('Very good. I am happy to take another order')
        get_order()
            #break
def order_breakfast():
    intro()
    get_order()
    order_again()

order_breakfast()
