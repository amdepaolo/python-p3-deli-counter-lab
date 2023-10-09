def line(deli_line):
    if len(deli_line) == 0:
        print("The line is currently empty.")
    else:
        sentence = "The line is currently:"
        for index, name in enumerate(deli_line):
            sentence+= f" {index + 1}. {name}"
        print(sentence)

def take_a_number(deli_line, name):
    deli_line.append(name)
    print(f"Welcome, {name}. You are number {len(deli_line)} in line.")

def now_serving(deli_line):
    if len( deli_line) == 0:
        print("There is nobody waiting to be served!")
    else:
        current_customer = deli_line.pop(0)
        print(f"Currently serving {current_customer}.")

