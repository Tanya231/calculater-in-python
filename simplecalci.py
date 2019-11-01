print("Simple calculater ")
print("\n 1 - Addition \n 2 - Subtraction \n 3 - Multipication \n 4 -Division  ")
calci = int(input("Please enter any one choice "))

if calci == 1 :

    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    addition = a+b
    print("Addition = ",addition)

elif calci == 2 :
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    div = a-b
    print("Division = ",div)
elif calci == 3 :
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    mul = a*b
    print("Multipication = ",mul)
elif calci == 4 :
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    div = a/b
    print("Division0 = ",div)

else: print("You are enter wrong choice ")