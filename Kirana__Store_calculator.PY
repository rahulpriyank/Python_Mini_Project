print("*****Welcome To Jhaji Kirana Store*****")
sum = 0
while(True):
    userinput = input("Enter the price of item: \n")
    if (userinput!='print'):
        sum = sum + int(userinput)

    else:
        print("Thanks")
        print(f"Your total bill is {sum}")
        break