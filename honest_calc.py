messages = {
    0: "Enter an equation",
    1: "Do you even know what numbers are? Stay focused!",
    2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    3: "Yeah... division by zero. Smart move...",
    4: "Do you want to store the result? (y / n):",
    5: "Do you want to continue calculations? (y / n):",
    6: " ... lazy",
    7: " ... very lazy",
    8: " ... very, very lazy",
    9: "You are",
    10: "Are you sure? It is only one digit! (y / n)",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
    12: "Last chance! Do you really want to embarrass yourself? (y / n)"
}


def is_one_digit(v):
    if -10 < v < 10 and v == int(v):
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += messages[7]
    if (v1 == 0 or v2 == 0) and (v3 in {"*", "+", "-"}):
        msg += messages[8]
    if msg:
        msg = messages[9] + msg
        print(msg)


def main():
    memory = 0
    continued = True
    while continued:
        print(messages[0])
        calc = input()
        x, oper, y = calc.split()
        if x == "M":
            x = memory
        if y == "M":
            y = memory

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(messages[1])
            continue

        if oper in {"+", "-", "*", "/"}:
            check(x, y, oper)
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/" and y != 0:
                result = x / y
            else:
                print(messages[3])
                continue
        else:
            print(messages[2])
            continue
        print(result)

        unsaved = True
        while unsaved:
            print(messages[4])
            answer = input()
            if answer == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while msg_index < 13:
                        print(messages[msg_index])
                        answer = input()
                        if answer == "y":
                            msg_index += 1
                        elif answer == "n":
                            unsaved = False
                            break
                    else:
                        memory = result
                        unsaved = False
                else:
                    memory = result
                    unsaved = False
            elif answer == "n":
                unsaved = False

        while True:
            print(messages[5])
            answer = input()
            if answer == "y":
                break
            elif answer == "n":
                continued = False
                break


if __name__ == "__main__":
    main()
