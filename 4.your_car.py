# Your car story
# pending to fix, and "bye" L55

print('\nYou bought a car. \nType "help" to help yourself with the car.\n')

b = True

while b == True:
    c = True
    while c == True:
        a = input("Input: " ).lower()
        if a == "run":
            print("Car is running.")
        elif a == "break":
            print("Car has stopped.")
        elif a == "throw":
            print("You have thrown away your car.")
            c = False
        elif a == "help":
            print('''Type:         
help  --> Shows you what you can do with your car.
run   --> Your car will run.
break --> Your car will stop
throw --> You throw your car 
''')
        else:
            print("Invalid input, spell properly")
    else:
        tri = 0
        limit = 6
        while tri < limit:
            a = input("Input: ").lower()
            if tri == 0:
                print("You have thrown away your car.")
                tri += 1
            elif tri == 1:
                print("You have no more car.")
                tri += 1
            elif tri == 2:
                print("No more.")
                tri += 1
            elif tri == 3:
                print("Type more no use.")
                tri += 1
            elif tri == 4:
                print("You really need a car?")
                tri += 1
            else:
                tri += 1

        else:
            print('Buy new car? \nType "take my money" to buy new car')
            while True:
                a = input("Input: ").lower()
                if "take my money" and "bye" in a:
                    print("Type properly")
                elif "take my money" in a:
                    print("You got a new car! YAY")
                    print('\nYou bought a car. \nType "help" to help yourself with the car.\n')
                    c = True
                    break
                elif "bye" in a:
                    b = False
                    break
                else:
                    print('Type "take my money" or BYE')