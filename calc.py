print("Simple Calculator")

num_1 = int(input("Enter First Number : "))
num_2 = int(input("Enter Second Number : "))
 

choice = input("Select Operation :-> A for Addition, S for Subtraction, M for Multiplication, D for Division :  ")
if choice == 'A' or choice == 'a'  :
    print("The Addition of These Numbers : ", num_1+num_2)
elif choice == "S" or choice == 's' :
    print("The Subtraction of These Numbers :", num_1-num_2)
elif choice == "M" or choice == 'm' :
    print("The Multiplication of These Numbers :", num_1*num_2)
elif choice == "D" or choice == 'd' :
    print("The Division of These Numbers :", num_1//num_2)
else :
    print("Oops !!! You didin't choose correct option.")

