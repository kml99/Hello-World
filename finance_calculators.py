# Finance calculators, select between investment and bond. (Task 05) Capstone Project
# written by K.M.Lambert
# December 2023
#
# Write a program that will allow the user to select between the interest on an investment and the interest on a bond 
# display the selection criteria investment or bond with an explanation as to what each option will do
# the user may use different variations of the word "bond" or "Invesment" all variations should be recognised as valid entries. 
# Generate an error message for any invalid input
# if investment is selected do the following
# ask user for the amount of money that is being deposited
# the user must enter the interest rate (as a percentage).  only the number should be entered not a %
# the user must enter the number of years they plan to invest
# ask the user if they want "simple" or "compound" interest and store it as a variable
# perform calculations based on either "simple" or "compount" selection
# Display to the user the amount that they will receive after the given period at the specified interest rate.
#
# If the user selects "bond"
# Ask the user to input present value of house
# ask the user for the interest rate
# ask the user for the number of months they plan to take the to repay the bond
# calculate the amount of money that the user will have to repay each month
# Display the answer
#

# open library math
import math

# start loop to check for bond or investment
while True:

# Display messages for selection criteria such as Investment or Bond    
    print("\nInvestment - to calculate the amount of interest you'll earn on your Investment")
    print("\nBond       - to calculate the amount you'll have to pay on a Home Loan.\n")

    user_select = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Ensure that user input is set to lowercase and is clean
    user_select = user_select.lower()
    user_select = user_select.strip()

# bond has been selected        
# ask for user input for house value, interest rate and years to repay bond
    if (user_select == "bond"):
        bond_amount = int(input("\nEnter the present value of the house: "))
        bond_annual_rate = int(input("\nWhat is the interest rate? "))
        bond_noyears = int(input("\nHow many years to repay bond? "))
        
# work out monthly interest rate and total payments
        bond_monthly_rate = (bond_annual_rate / 100) / 12
        total_payments = bond_noyears * 12
        
# calculate the amount to be repaid per month and display the amount to the user
        bond_repayment = (bond_amount * bond_monthly_rate) / (1 - (1 + bond_monthly_rate) ** -total_payments)
        print(f"\nMonthly Repayment Amount: £{bond_repayment:.2f}\n")
        break

# investment has been selected
# user input for amount being deposited, interest rate, number of years
    elif (user_select == "investment"):
        invest_amount = int(input("\nEnter the amount of money you will be depositing: "))
        invest_rate = int(input("\nWhat is the interest rate? "))
        invest_noyears = int(input("\nHow many years? "))
        
# ask user if they want simple or compound interest
        invest_interest = input("\nDo you want 'simple' or 'compound' interest? ")
        
# Ensure that user input is set to lowercase and is clean       
        invest_interest = invest_interest.lower()
        invest_interest = invest_interest.strip()
        invest_percentage = invest_rate / 100
        
# simple interest calculation 
        if invest_interest == "simple":
            simple_answer = invest_amount * (1 + invest_percentage * invest_noyears)
            print(f"\nSimple interest:  £{simple_answer:.2f}\n")
            print()
            break
        
# compound interest calculation
        elif invest_interest == "compound":
            compound_answer = invest_amount * math.pow(1 + invest_percentage, invest_noyears)
            print(f"\nTotal amount after compound interest:  £{compound_answer:.2f}\n")
            print()
            break
        else:
            print("\nYou need to enter either 'bond' or 'investment' to continue.\n")

