def kg_lb_convertor():
    try:
        amount = float(input("Input a number: "))
        unit = input("Type lb for pound, kg for kilogram: ").lower()
        if unit == "lb":
            result = amount * 0.454
            print(f'{amount} lb = {result} kg')
        elif unit == "kg":
            result = amount / 0.454
            print(str(amount) + " kg = " + str(result) + " lb")
        else:
            print('Type "lb" or "kg" only pls')
    except ValueError:
        print("Invalid input, please type a numerical number.")
    print(kg_lb_convertor())

print(kg_lb_convertor())
