#Shabbar Sayed
#CS 175L
#restaurant.py

vegetarian = False
vegan = False
gluten_free = False

response = input('Is anyone in your party a vegetarian? ')
if response == 'yes':
    vegetarian = True
response = input('Is anyone in your party a vegan? ')
if response == 'yes':
    vegan = True
response = input('Is anyone in your party gluten free? ')
if response == 'yes':
    gluten_free = True

print('Here are you restaurant choices: ')
if not vegetarian and not vegan and not gluten_free:
    print("Joe's Gourmet Burgers")
if not vegan and not gluten_free:
    print("Mama's Fine Italian")
if not vegan:
    print("Main Street Pizza")

print('Corner Cafe')
print("Chef's Kitchen")

keep_going = input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end): ")

while keep_going =='yes':
    response = input('Is anyone in your party a vegetarian? ')
    if response == 'yes':
        vegetarian = True
    response = input('Is anyone in your party a vegan? ')
    if response == 'yes':
        vegan = True
    response = input('Is anyone in your party gluten free? ')
    if response == 'yes':
        gluten_free = True

        print('Here are you restaurant choices: ')
        if not vegetarian and not vegan and not gluten_free:
            print("Joe's Gourmet Burgers")
        if not vegan and not gluten_free:
            print("Mama's Fine Italian")
            if not vegan:
                print("Main Street Pizza")
    print('Corner Cafe')
    print("Chef's Kitchen")
    keep_going = input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end): ")
