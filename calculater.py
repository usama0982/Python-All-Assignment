
val1=int(input("Enter number"))
val2=int(input("Enter number"))
operator = input("Enter operater")

if operator == "+":
    val = val1 + val2
    print(val,"answer")
    
elif  operator == "-":
    val = val1 - val2
    print(val,"answer")   

    
elif  operator == "*":
    val = val1 * val2
    print(val,"answer")

    
elif  operator == "/":
    val = val1 / val2
    print(val,"answer")

elif  operator == "**":
    val = val1 ** val2
    print(val,"answer")

else:
    print("you choice invalid operator")
