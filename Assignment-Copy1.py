#!/usr/bin/env python
# coding: utf-8

# In[12]:


def customer(choice):
    if choice == 1:
        groc = {
            1: {'Name': 'rice', 'Quantity': '200 kg', 'price': 20},
            2: {'Name': 'spices', 'Quantity': '20 kg', 'price': 50},
            3: {'Name': 'salt', 'Quantity': '2 kg', 'price': 30},  
            4: {'Name': 'sugar', 'Quantity': '5 kg', 'price': 40}  
        }
        print("Groceries selected")
        for item in groc.values():
            print(f"Name: {item['Name']}, Quantity: {item['Quantity']}, Price: {item['price']}")
    elif choice == 2:
        softdrinks={
            1: {'Name': '7up', 'Quantity': '20 liters', 'price': 25},
            2: {'Name': 'mirinda', 'Quantity': '20 liters', 'price': 30},
            3: {'Name': 'mountain dew', 'Quantity': '2 liters', 'price': 15},
            4: {'Name': 'sprite', 'Quantity': '5 liters', 'price': 20}
        }
        print("Soft Drinks selected")
        for item in softdrinks.values():
            print(f"Name: {item['Name']}, Quantity: {item['Quantity']}, Price: {item['price']}")
    elif choice == 3:
        snacks={
            1: {'Name': 'potato chips', 'Quantity': '200 g', 'price': 10},
            2: {'Name': 'chocolate bar', 'Quantity': '100 g', 'price': 15},
            3: {'Name': 'pretzels', 'Quantity': '150 g', 'price': 20},
            4: {'Name': 'popcorn', 'Quantity': '250 g', 'price': 25}
        }
        print("Snacks selected")
        for item in snacks.values():
            print(f"Name: {item['Name']}, Quantity: {item['Quantity']}, Price: {item['price']}")
    elif choice == 4:
        fruits = {
            1: {'Name': 'apple', 'Quantity': '1 kg', 'price': 50},
            2: {'Name': 'banana', 'Quantity': '1 dozen', 'price': 30},
            3: {'Name': 'orange', 'Quantity': '1 dozen', 'price': 40},
            4: {'Name': 'grapes', 'Quantity': '500 g', 'price': 60}
        }
        print("Fruits selected")
        for item in fruits.values():
            print(f"Name: {item['Name']}, Quantity: {item['Quantity']}, Price: {item['price']}")
    else:
        print("Invalid choice")

# Example usage:
user_choice = int(input("Please select a category:\n1. Groceries\n2. Soft Drinks\n3. Snacks\n4. Fruits\n"))
customer(user_choice)


# In[ ]:




