def budget():
    i = int(input("what is the total amount of your monthly income? "))
    e = int(input("what is the total amount of your monthly expenses? "))
    b = i - e
    print("Your monthly disposable income is $", b)

def interest():
    r = float(input("What is your monthly interest rate? "))
    p = float(input("What is the total amount of your loan? "))
    n = int(input("what is the loan term length in months: (if you know the number in years, multiply that by 12 and enter): "))

    c = ((r*p)/(1-pow((1+r), -n)))
    print("Your monthly mortgage payment will be $", c )
    print("Would you like to know how much interest you will pay in total for this loan?")
    print("1. Yes")
    print("2. No")
    s = input("Please select a number from the menu: ")
    selection = int(s)
    print("Thank you for your selection")
    if selection == 1:
        i = ((c*n) - p)
        print(c)
        print(n)
        print(c*n)
        print(p)
        print("You will pay $",i ," over the life of this loan")
    if selection == 2:
        return 0



print("What finances calculation would you like to use?")
print("1. Monthly Budget")
print("2. Monthly Mortgage")
s = input("Please select a number from the menu: ")
selection = int(s)
print("Thank you for your selection")

if selection == 1:
    budget()
elif selection == 2:
    interest()