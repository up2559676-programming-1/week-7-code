import time
from graphix import Text, Window, Circle, Point
from pract5 import draw_brown_eye, distance_between_points
from pract6 import calculate_grades


def hello_while():
    i = 0
    while i < 10:
        print("i is now", i)
        i = i + 1


def countdown():
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")


def mystery_loop():
    i = 1
    # Be careful! This loop will run forever!
    while i < 1000:
        print(i)
        i = i * 2


def add_up_numbers1():
    total = 0
    more_numbers = "y"
    while more_numbers == "y":
        number = int(input("Enter a number: "))
        total = total + number
        more_numbers = input("Any more numbers? (y/n) ")
    print("The total is", total)


def add_up_numbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)


def add_up_numbers3():
    total = 0
    n_str = input("Number (hit enter to stop): ")
    while n_str != "":
        number = int(n_str)
        total += number
        n_str = input("Number (hit enter to stop): ")
    print("The total is", total)


def add_up_numbers4():
    total = 0
    while True:
        n_str = input("Number (anything else to stop): ")
        if not n_str.isdigit():
            break  # Exit the loop if the input is not a number
        number = int(n_str)
        total += number
    print("The total is", total)


# Note: msg == "" needs to appear twice
def get_string1():
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg


def get_string2():
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg


def can_apply_for_job(degree, experience):
    if (degree == "1st" or degree == "2:1") and experience >= 1:
        return True
    elif degree == "2:2" and experience >= 2:
        return True
    else:
        return False


def can_vote1():
    age = int(input("How old are you? "))
    while age <= 18:
        print("Wait until you are 18!")
        age = int(input("How old are you? "))


def can_vote2():
    while True:
        age = int(input("How old are you? "))
        if age > 18:
            break
        print("Wait until you are 18!")


#  For question 2
def traffic_lights():
    win = Window()
    red = Circle(Point(100, 50), 20)
    red.fill_colour = "red"
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.fill_colour = "black"
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.fill_colour = "black"
    green.draw(win)
    while True:
        time.sleep(3)
        red.fill_colour = "black"
        amber.fill_colour = "yellow"

        time.sleep(3)
        amber.fill_colour = "black"
        green.fill_colour = "green"

        time.sleep(3)
        green.fill_colour = "black"
        red.fill_colour = "red"


def grade_coursework():
    def int_input() -> int:
        while True:
            try:
                return int(input("Enter coursework mark: "))
            except ValueError:
                pass

    mark = int_input()
    while 20 < mark < 0:
        mark = int_input()

    print(f"Coursework grade: {calculate_grades(mark)}")


def order_price():
    def product_input() -> tuple[float, float, str]:
        unit_price = float(input("Enter unit price £"))
        quantity = float(input("Enter the quantity: "))
        is_more = input("Enter 'y' if there are more products: ")

        return (unit_price, quantity, is_more)

    is_more = "y"
    price = 0.0
    while is_more == "y":
        (unit_price, quantity, is_more) = product_input()
        price += unit_price * quantity

    print(f"Total order price: {price:.2f}")


def clickable_eye():
    win = Window()
    draw_brown_eye(win, Point(200, 150), 100)

    label = Text(Point(350, 150), "")

    while True:
        pos = win.get_mouse()
        dist = distance_between_points(Point(200, 150), pos)


clickable_eye()


# For question 6
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


# Solutions to the programming exercises:


def get_name() -> str:
    while True:
        name = input("Enter name: ")
        if name.isalpha():
            return name
