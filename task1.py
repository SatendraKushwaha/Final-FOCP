#program to display random passwords
import random

#initilize variables
vegetables = ["Carrot", "Potato", "Onion", "Cabbage", "Garlic"]
color = ["Red", "Pink", "White", "Yellow", "Black"]
places = ["Kathmandu", "India", "China", "England", "America"]

try:
    #ask user to enter the number
    num = int(input("Please enter a number! How many password do you want?"))
except:
    print("Please enter the number.")
    exit()
    
    #if else condition to satisfy the condition
if num>24 or num<=0:
    print("Sorry! Please enter the number between 0 to 24")
else:
    #created the empty list
    password = []
    #for loop to generate the passwords
    for i in range (num):
        a = random.choice(vegetables)
        b = random.choice(color)
        c = random.choice(places)
#concatenate the strings
        print('{} --> {}'.format(i + 1, a+b+c))      