run = True
while(run):
    choice = input("Enter Y to run Program and N to Quit :- ")
    if(choice == 'y' or choice == 'Y'):
        run = True
        num = int(input("Enter a Number to Find that It's Even or Odd :- "))
        if (num % 2 == 0):
            print("The Number",num,"is Even")
        else:
            print("The Number",num,"is Odd")

    elif(choice == 'n' or choice == 'N'):
        run = False
   
