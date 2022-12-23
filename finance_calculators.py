#This is a program which allows a user to access either an investment calculator or a home loan repayment calculator
#Import math to use power function
import math

#Create list with the two finance calulator options: 'investment' or 'bond', and loop until one of the options in the list is inputted
correct_options = ["investment","bond"]
while True:
    choice = input('''Choose either 'investment' or 'bond' from the menu below to proceed:
    \ninvestment - to calculate the amount of interest you'll earn on your investment
    \nbond - to calculate the amount you'll have to pay on a home loan''').lower()
    if choice in correct_options:
        break

#If the user inputs investment, ask for deposit, interest rate, how many years of investing and whether this is simple or compound interest 
if choice == "investment":
    deposit = int(input("Please input the amount of money you are depositing:"))
    interest_rate = int(input("Please input your interest rate as a percentage:"))
    years = int(input("Please enter how many years you plan on investing:"))
    interest = (input("Do you want 'simple' or 'compound' interest?")).lower()
    r = interest_rate/100

    #If the interest is simple, calculate and print the total amount the user will get back after the given period
    if interest == 'simple':
        total_amount = deposit * (1 + r * years)
        print(f"After {years} years, your investment of £{deposit:.2f} will be worth £{total_amount:.2f}.")
    
    #If the interest is compound, calculate and print the total amount the user will get back after the given period
    if interest == 'compound':
        total_amount = deposit * math.pow((1 + r), years)
        print(f"After {years} years, your investment of £{deposit:.2f} will be worth £{total_amount:.2f}.")

#If the user inputs bond, ask for current house value, interest rate, and how many months of repayment and then calculate how much the user will pay back per month
if choice == "bond":
    house_value = int(input("Please enter the value of the house:"))
    interest_rate = int(input("Please enter the annual interest rate:"))
    months = int(input("Please enter how many months you plan to repay the bond:"))
    i = (interest_rate/100)/12
    total_amount = (i*house_value)/(1 - (math.pow((1+i),(-months))))
    print(f"You will have to repay £{total_amount:.2f} each month.")
    
    