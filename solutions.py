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
    ex11()
