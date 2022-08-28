import math
import datetime

# Exercise 1&2
def exercise_1_2():
    name = "Sid"
    dog_1 = "Knox"
    dog_2 = "Bella"
    print("My dog " + dog_1 + " is 19 years old")
    print("My dog " + dog_2 + " is 99 years old")


# Exercise 3
def exercise_3():
    noun = " dog"
    verb = " ate"
    adjective = " researched"
    adverb = " thoroughly"
    print("My" + noun + verb + " my" + adverb + adjective + " paper (again)!")


# Exercise 4
def exercise_4():
    noun_1 = "Dog "
    verb_1 = "ran "
    print(noun_1 + verb_1 + "away.")

    my_age = 16
    dog_age = 77
    print("In dog years, I’m older than my dog.")

    word = "abracadabra "
    print("Your double-word is " + (word * 2))


# Exercise 5
def exercise_5():
    noun = str(input("Give me a noun: "))
    verb = str(input("Give me a verb: "))
    adjective = str(input("Give me an adjective: "))
    adverb = str(input("Give me an adverb: "))
    print("My " + noun + " " + verb + " my " + adverb + " " + adjective + " paper (again)!")


# Exercise 6
def exercise_6_1():
    weight = int(input("Enter a weight: "))
    print("About " + str(round(weight / 2.2046, 3)) + "kg")


def exercise_6_2():
    length = int(input("Enter a length: "))
    width = int(input("Enter a width: "))
    print("The area is " + str(length * width) + " units squared")


def exercise_6_3():
    age = int(input("Enter your age: "))

    if 18 - age > 0:
        print("You have " + str(18 - age) + " years until graduation")
    elif 18 - age == 0:
        print("You are about to graduate")
    else:
        print("You graduated " + str(age - 18) + " years ago")


def exercise_6_4():
    grade = float(input("Enter a grade below 50% here: "))
    if 0 < grade < 50:
        print("Your new grade is " + str((grade + 100) / 2) + "%")
    else:
        print("That grade is not valid")
        exercise_6_4()


# Exercise_7
def exercise_7():
    meal_cost = float(input("How much does the meal cost?: "))
    tax = float(input("How much tax is there?: "))
    tip = float(input("How much is the tip?: "))
    tax_cost = meal_cost * tax / 100
    tip_cost = (tax_cost + meal_cost) * tip / 100
    total_cost = meal_cost + tax_cost + tip_cost
    print("The basic meal cost is about $" + str(round(meal_cost, 2)))
    print("The extra cost (tax+tip) is about $" + str(round(tax_cost + tip_cost, 2)))
    print("The total cost is about $" + str(round(total_cost, 2)))


# Exercise 9
def exercise_9_1():
    user_age = int(input("Enter your age: "))
    mother_age = int(input("Enter your mother's age: "))

    if mother_age - user_age > 0:
        print("Your mom was " + str(mother_age - user_age) + " when you were born")
    else:
        print("Invalid Age")
        exercise_9_1()


def exercise_9_2():
    number = int(input("Enter a number: "))
    print(str(number-2)+", "+str(number-1)+", "+str(number)+", "+str(number+1)+", "+str(number+2))


def exercise_9_3():
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter another number: "))
    number3 = float(input("Enter another number: "))
    print("The average of those numbers is "+str((number1+number2+number3)/3))


def exercise_9_4():
    number = float(input("Enter a number between 0 and 1: "))
    if 0 < number < 1:
        print("The number you entered is " + str(number) + ". \nThe output is " + str(number * 10))
        # print(f"The number you entered is {number}.\nThe output is {number * 10}")
    else:
        print("Invalid Answer")
        exercise_9_4()


def exercise_9_5_1():
    hour1 = float(input("Enter the first hour: "))
    minute1 = float(input("Enter the first minute: "))
    second1 = float(input("Enter the first seconds: "))
    hour2 = float(input("Enter the second hour: "))
    minute2 = float(input("Enter the second minute: "))
    second2 = float(input("Enter the second seconds: "))
    hour1 = hour1*3600
    minute1 = minute1*60
    hour2 = hour2*3600
    minute2 = minute2*60
    time1 = hour1+minute1+second1
    time2 = hour2+minute2+second2
    final_time = abs(time1-time2)
    print("The difference between those two times "+str(final_time)+" seconds")


def exercise_9_5_2():
    year1 = int(input("Enter the first year: "))
    month1 = int(input("Enter the first month: "))
    date1 = int(input("Enter the first date: "))
    hour1 = int(input("Enter the first hour: "))
    minute1 = int(input("Enter the first minute: "))
    second1 = int(input("Enter the first seconds: "))
    year2 = int(input("Enter the second year: "))
    month2 = int(input("Enter the second month: "))
    date2 = int(input("Enter the second date: "))
    hour2 = int(input("Enter the second hour: "))
    minute2 = int(input("Enter the second minute: "))
    second2 = int(input("Enter the second seconds: "))
    time1 = datetime.datetime(year1, month1, date1, hour1, minute1, second1)
    time2 = datetime.datetime(year2, month2, date2, hour2, minute2, second2)
    final_time = abs(time1-time2)
    print("The difference between those two times "+str(final_time))


# exercise_1_2()
# exercise_3()
# exercise_4()
# exercise_5()
# exercise_6_1()
# exercise_6_2()
# exercise_6_3()
# exercise_6_4()
# exercise_7()
# exercise_9_1()
# exercise_9_2()
# exercise_9_3()
# exercise_9_4()
# exercise_9_5_1()
# exercise_9_5_2()
