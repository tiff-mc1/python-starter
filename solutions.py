import random
import sys
import datetime


def main():
    print("Solutions")


def ex1():
    sum = 0
    myList = []

    for x in range(0, 10):
        num = random.randint(0, 100)
        myList.append(num)
        sum += num
    print(f"random list: {myList}")
    print(f"sum = {sum}")


# problem 2
def ex2():
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    length = float(input("Enter length: "))

    print(f"Volume of the box equals {'%.2f'%(width * height * length)}")


def ex3():
    myList = []

    size = int(input("Enter the number of inputs: "))

    for i in range(0, size):
        num = int(input("Enter a number: "))
        myList.append(num)

    if myList[0] == myList[-1]:
        print("True")
    else:
        print("False")


def ex4():
    str = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    arr = str.split(" ")
    count = 0

    for s in arr:
        if s == "Python":
            count += 1

    print(count)


def ex5():
    myList = [1, 2, 3]
    mySet = {3, 4, 5}
    myListSet = mySet.union(set(myList))
    print(myListSet)


def ex6():
    myList = [11, 100, 101, 999, 1001]
    print(myList[::-1])


def ex7():
    num = random.randint(0, 100)

    if num < 10:
        print(f"{num}: BOO you loser!")
    elif num >= 10 and num < 50:
        print(f"{num}: Try again!")
    else:
        print(f"{num} You win!!")


def ex8():
    myList = [6, 2, 7, 3, 77, 7, 1]
    smallest = sys.maxsize

    for i in myList:
        if i < smallest:
            smallest = i

    print(smallest)


def ex9():
    str = "HELLO"
    print(str.isupper())


def ex10():
    str = input("please enter a word:").lower()
    vowels = 0
    consonants = 0

    for c in str:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            vowels += 1
        else:
            consonants += 1

    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")


def ex11():
    # get todays date
    today = datetime.datetime.now().date()

    myFile = open("output.txt", "w")
    myFile.write(f"Todays's date is: {str(today)}")
    myFile.close()


def ex12():
    while True:

        num = input("Enter an integer or 'quit' to exit: ")
        if num == 'quit':
            break

        isInt = True

        for c in num:
            if c == '.':
                isInt = False
                break

        if isInt:
            num = int(num)
            if num > 0:
                print(f"-{num}")
            elif num < 0:
                print(num - 2*num)
            else:
                print(f"The number is zero.")
        else:
            print("Only Integer Values allowed")


def ex13():
    while True:
        num1 = input("Enter integer or 'quit' to exit: ")
        num2 = input("Enter integer or 'quit' to exit: ")

        if num1 == "quit" or num2 == "quit":
            break
        else:
            print(f"Sum = {int(num1) + int(num2)}")


def ex14():
    while True:
        num1 = input("Enter num1 or 'quit' to exit: ")
        if num1 == 'quit':
            break
        num2 = input("Enter num2 or 'quit' to exit: ")
        if num2 == 'quit':
            break
        op = input("Enter operation(add, sub, mul, div): ")

        if op == 'quit':
            break
        elif op == "add":
            print(f"Sum = {float(num1) + float(num2)}")
        elif op == "sub":
            print(f"Sub = {float(num1) - float(num2)}")
        elif op == "mul":
            print(f"Mul = {float(num1) * float(num2)}")
        elif op == "div":
            try:
                print(f"Div = {float(num1)/float(num2)}")
            except ZeroDivisionError as e:
                print("Cannot divide by zero!")
        else:
            print("Enter Valid Input")


def ex15():
    myFile = open("ex15output.txt", "a")

    while True:
        num1 = input("Enter num1 or 'quit' to exit: ")
        if num1 == 'quit':
            break
        num2 = input("Enter num2 or 'quit' to exit: ")
        if num2 == 'quit':
            break
        op = input("Enter operation(add, sub, mul, div): ")
        res = 0

        if op == 'quit':
            break
        elif op == "add":
            res = float(num1) + float(num2)
            print(f"Sum = {res}")
        elif op == "sub":
            res = float(num1) - float(num2)
            print(f"Sub = {res}")
        elif op == "mul":
            res = float(num1) * float(num2)
            print(f"Mul = {res}")
        elif op == "div":
            try:
                res = float(num1)/float(num2)
                print(f"Div = {res}")
            except ZeroDivisionError as e:
                print("Cannot divide by zero!")
        else:
            print("Enter Valid Input")

        log = f"{str(datetime.datetime.now())} {num1} {op} {num2} = {res} \n"
        myFile.write(log)
    myFile.close()


def ex16():
    # Hashlib library is required to use SHA256
    mydict = {}
    while True:
        username = input("Enter a username or 'quit' to exit: ")
        if username == 'quit':
            break
        password = input("Enter a password or 'quit' to exit: ")
        if password == 'quit':
            break
        mydict[username] = hashlib.sha256(password.encode())

    for key in mydict:
        # hexdigest displays the hexadecimal value of the hash
        print(key, ": ", mydict[key].hexdigest())


def ex17():
    myDict = {}
    print("Enter 'quit' anytime in the program to exit!")

    while True:
        mode = input("Please enter mode: Add | Login: ")
        if mode == 'quit':
            break

        if mode == "add":
            username = input("Enter a username: ")
            if username == 'quit':
                break
            password = input("Enter a password: ")
            if password == 'quit':
                break
            myDict[username] = hashlib.sha256(password.encode())

        if mode == "login":
            username = input("Enter a username: ")
            if username == 'quit':
                break
            password = input("Enter a password: ")
            if password == 'quit':
                break
            # print(f"stored password:{myDict[username]}\nentered password: { hashlib.sha256(password.encode())}")
            if myDict[username].hexdigest() == hashlib.sha256(password.encode()).hexdigest():
                print("Password is correct")
            else:
                print("Password is incorrect")
    for key in myDict:
        # hexdigest displays the hexadecimal value of the hash
        print(key, ": ", myDict[key].hexdigest())


def ex18():
    num = random.randint(0, 100)

    while True:
        guess = int(input("Please enter a guess between 0 and 100: "))

        if (guess < num):
            print("Too low")
        elif (guess > num):
            print("Too high")
        else:
            print("You win!")
            break


if __name__ == "__main__":
    main()
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    # ex11()
    # ex12()
    # ex13()
    # ex14()
    # ex15()
    # ex16()
    # ex17()
    # ex18()
