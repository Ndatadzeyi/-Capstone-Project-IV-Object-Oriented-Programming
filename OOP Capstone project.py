#inventory.py

"""
This program is a shoe inventory management system.

It allows users to:

* Capture new shoes
* View all shoes
* Re-stock shoes
* Search for a shoe
* Calculate the value per item
* Find the shoe with the highest quantity
* Exit the program
"""
import csv
from tabulate import tabulate

"""
The Shoe class represents a shoe in the inventory.

It has the following attributes:

* country: The country where the shoe was made
* code: The shoe's code
* product: The shoe's name
* cost: The shoe's cost
* quantity: The number of shoes in stock
"""

"""
    Initialize a new Shoe object.

    Args:
        country: The country where the shoe was made
        code: The shoe's code
        product: The shoe's name
        cost: The shoe's cost
        quantity: The number of shoes in stock
"""
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'{self.product} ({self.country}) - {self.quantity} units available'

"""
The read_shoes_data() function reads shoe data from a CSV file.

Args:
    file_path: The path to the CSV file

Returns:
    A list of Shoe objects
"""
    
def read_shoes_data(file_path):
    shoes_list = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                country = row[0]
                code = row[1]
                product = row[2]
                cost = float(row[3])
                quantity = int(row[4])
                shoes_list.append(Shoe(country, code, product, cost, quantity))
            except:
                print(f'Error reading row: {",".join(row)}')
    return shoes_list

"""
The capture_shoes() function captures new shoe data from the user.

Args:
    shoes_list: A list of Shoe objects
"""

def capture_shoes(shoes_list):
    country = input('\nEnter the country: ')
    code = input('\nEnter the code: ')
    product = input('\nEnter the product name: ')
    cost = float(input('\nEnter the cost: '))
    quantity = int(input('\nEnter the quantity: '))
    shoes_list.append(Shoe(country, code, product, cost, quantity))

"""
The view_all() function displays all of the shoes in the inventory.

Args:
    shoes_list: A list of Shoe objects
"""
    
def view_all(shoes_list):
    header = ['Country', 'Code', 'Product', 'Cost', 'Quantity']
    data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoes_list]
    print(tabulate(data, headers=header))

"""
The re_stock() function re-stocks the shoe with the lowest quantity.

Args:
    shoes_list: A list of Shoe objects
"""
    
def re_stock(shoes_list):
    lowest_qty_shoe = min(shoes_list, key=lambda shoe: shoe.quantity)
    print(f'The shoe with the lowest quantity is: {lowest_qty_shoe}')
    add_quantity = input('Do you want to add quantity for this shoe? (y/n): ').lower()
    if add_quantity == 'y':
        new_quantity = int(input('Enter the new quantity: '))
        lowest_qty_shoe.quantity += new_quantity
        with open('inventory.txt', 'w') as file:
            writer = csv.writer(file)
            for shoe in shoes_list:
                writer.writerow([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])

"""This function searches for a shoe in the inventory.

    Get the shoe code from the user.
 

    Find all shoes with the specified code.


    If no shoes were found, print a message.
  

    Otherwise, print the information for each shoe.
   """
# This function searches for a shoe in the inventory.
def search_shoe(shoes_list):
    # Get the shoe code from the user.
    code = input('Enter the shoe code: ')

    # Find all shoes with the specified code.
    found_shoes = [shoe for shoe in shoes_list if shoe.code == code]

    # If no shoes were found, print a message.
    if not found_shoes:
        print(f'No shoes found with code {code}')

    # Otherwise, print the information for each shoe.
    else:
        for shoe in found_shoes:
            print(shoe)
"""
This function calculates the value of each item in the inventory.
Create a header for the table.
Create a list of data for the table.
Print the table.
"""
  
    
def value_per_item(shoes_list):
    header = ['Product', 'Value']
    data = [[shoe.product, shoe.cost * shoe.quantity] for shoe in shoes_list]
    print(tabulate(data, headers=header))

"""  
This function finds the shoe with the highest quantity in the inventory.
Find the shoe with the highest quantity.
Print the information for the shoe with the highest quantity.
"""
    
def highest_qty(shoes_list):
    highest_qty_shoe = max(shoes_list, key=lambda shoe: shoe.quantity)
    print(f'The shoe with the highest quantity is: {highest_qty_shoe.product} ({highest_qty_shoe.country}) - {highest_qty_shoe.quantity} units available')
    
"""
This function is the main entry point for the program.
Read the data from the inventory file.
Start a loop that will continue until the user wants to exit.
"""
def main():
    shoes_list = read_shoes_data('inventory.txt')
    while True:
        print('\nInventory Management System')
        print('1. Capture shoes')
        print('2. View all shoes')
        print('3. Re-stock')
        print('4. Search for a shoe')
        print('5. Value per item')
        print('6. Highest quantity')
        print('7. Exit')
        choice = int(input('\nEnter your choice: \n'))
        if choice == 1:
            capture_shoes(shoes_list)
        elif choice == 2:
            view_all(shoes_list)
        elif choice == 3:
            re_stock(shoes_list)
        elif choice == 4:
            search_shoe(shoes_list)
        elif choice == 5:
            value_per_item(shoes_list)
        elif choice == 6:
            highest_qty(shoes_list)
        elif choice == 7:
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()