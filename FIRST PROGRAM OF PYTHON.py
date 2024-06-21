print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVIDE")
print("5. PERCENTAGE")

operat = input("ENTER THE OPERATION YOU WANT TO PERFORM : ")

if(operat == "1"):
    val1 = float(input("Enter the first value : "))
    val2 = float(input("Enter the second value : "))
    print("The addition is : ",val1 + val2)

elif(operat == "2"):
    val1 = float(input("Enter the first value : "))
    val2 = float(input("Enter the second value : "))
    print("The subtraction is : ", val1 - val2)

elif(operat == "3"):
    val1 = float(input("Enter the first value : "))
    val2 = float(input("Enter the second value : "))
    print("The multiplication is : ",val1 * val2)

elif(operat == "4"):
    val1 = float(input("Enter the first value : "))
    val2 = float(input("Enter the second value : "))
    print("The divide is : ",val1 / val2)

elif(operat == "5"):
    val1 = float(input("Enter the first value : "))
    val2 = float(input("Enter the second value : "))
    print("The percentage is : ",val1 / val2 * 100)

else:
    print("Invalid Operation") 








