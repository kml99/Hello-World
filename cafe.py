# Total Stock value in the cafe (Task 12) Practical Task 1
# written by K.M.Lambert
# January 2024
#
# setup a total stock variable.  create a list of items on the menu, create a dictionary containing the stock value per menu item.
# create a dictionary containing the price of each item on the menu
# take each item and calculate the stock value
# display the total stock value for the cafe

# setup varible, menu list and stock and price dictionary
total_stock = 0
menu_list = ('Burger', 'Hotdog', 'Milkshake', 'Nachos',)

stock_dict = {'Burger': 240.00,
            'Hotdog': 95.00,
            'Milkshake': 650.00,
            'Nachos': 40.00}

price_dict = {'Burger': 12.00,
            'Hotdog': 9.50,
            'Milkshake': 6.50,
            'Nachos': 8.00}

# setup for loop to calculate value per item and total stock value
for stock_item in menu_list:
    item_value = stock_dict[stock_item] * price_dict[stock_item]
    total_stock += item_value

# display the total stock value for the cafe
print(f"\nThe total stock value in the cafe is: £{total_stock:.2f}\n")


