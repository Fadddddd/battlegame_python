while True:
    print("1. Number one")
    print("2. Number two")
    print("3. Number three")
    option = input("pick an option:")
    if option == "1":
        print("You chose 1")
    elif option == "2":
        print("You chose 2")
    elif option == "3":
        print("Leaving the loop")
        break
    else:
        print("invalid command")
print("You have left the loop")
