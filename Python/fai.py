# Brandon Torres
# (04) 
# 12/2023
# Lab 14(FINAL)

#This program should let the user enter any number of items into the program and then calculate and output the Subtotal, Tax (if CA), Shipping and Handling, and Total Due.

# Greet and tll the user what the program is used for

def Greetings(): 
    print('Hello User! This program will allow you to enter products to be shipped and calculates the subtotal, tax, shipping and handling, and the total due.')

def List():
    States =  ['AL', 'AK', 'AZ' , 'AR' , 'CA' , 'CO' , 'CT' , 'DE' , 'FL' , 'GA' , 'HI' , 'DI' , 'ID' , 'IL' , 'IN' , 'IA' , 'KS' , 'KY' , 'LA' , 'ME' , 'MD' , 'MA' , 'MI' , 'MN' , 'MS' , 'MO' , 'MT' , 'NE' , 'NV' , 'NH' , 'NJ' , 'NM' , 'NY' , 'NC' , 'ND' , 'OH' , 'OK' , 'OR' , 'PA' , 'RI' , 'SC' , 'SD' , 'TN' , 'TX' , 'UT' , 'VT' , 'VA' , 'WA' , 'WV' , 'WI' , 'WY']
    State = input("Enter the state abbreviation: ")
    while State not in States:
        State= input('INPUT ERROR- Please enter the 2 letter abbriviation of the state you are shipping to.')
    return State

def GetProductinfo():
    Product_info = []
    Loop=True
    while Loop:
        quantity = float(input("Enter quantity (enter 0 if done): "))
        if quantity == 0:
            break
        else:
            weight=float(input("Enter item weight: "))
            cost= float(input('Enter Item cost: '))
            Product_info.append((quantity, weight, cost))
    return Product_info

def Calculation(Product_infos):
    total_weight = 0
    total_cost = 0

    for mainIndex in range(len(Product_infos)):
        quantity, weight, cost = Product_infos[mainIndex]
        total_weight += quantity * weight
        total_cost += quantity * cost

    shipping = total_weight * 0.25

    if total_weight < 10:
        handling = 1
    elif 10 <= total_weight <= 100:
        handling = 3
    else:
        handling = 5

    Total_Shipping = shipping + handling

    return total_cost,Total_Shipping

def AskUser():
    print('Would you like to use this program again[y/n]')

    loop = True
    while loop:
        user_input = input().lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('Please enter y for "yes" or n for "no".')

# Main Program
Greetings()

stateMain = List()
productInfoListMain = GetProductinfo()
subTotalMain, totalShippingMain = Calculation(productInfoListMain)

if stateMain == 'CA':
    tax = subTotalMain * 0.08
else:
    tax = 0.00

# Display Subtotal, Tax, Shipping and Handling, and Total Due
print(format('Subtotal:', '<25'), format(subTotalMain, '>10,.2f'))
print(format('Tax:', '<25'), format(tax, '>10,.2f'))
print(format('Shipping and Handling:', '<25'), format(totalShippingMain, '>10,.2f'))

total_due = subTotalMain + tax + totalShippingMain
print(format('Total Due:', '<25'), format(total_due, '>10,.2f'))

if not AskUser():
    print("Have A Nice Day!")