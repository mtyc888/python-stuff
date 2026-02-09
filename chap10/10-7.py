
while True:
    try:
        input1 = input("Enter 1st number\n")
        input2 = input("Enter 2nd number\n")
        print(int(input1) + int(input2))
    except ValueError:
        print("Please, numbers only")