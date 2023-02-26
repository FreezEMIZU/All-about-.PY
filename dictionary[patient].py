patient_data = {}

while True:
    name = input("Enter Patient's name: ").upper()
    if name in patient_data:
        print(f'{name} is {patient_data[name]} years old')
    else:
        patient_data[name] = input("Enter Patient's age: ")