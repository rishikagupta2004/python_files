# # Choose your own adventure
# name = input("Type your name: ")
# print(f"Welcome {name.title()} to this adventure!")

# answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ")

# if answer.lower() == "left":
#     answer = input("You came to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across: ")

#     if answer.lower() == "swim":
#         print("You swam across and were eaten by an alligator.")
#     elif answer.lower() == "walk":
#         print("You walk for many miles, ran out of water and you lost the game.")
#     else:
#         print("Not a valid option. You lose.")  

# elif answer.lower() == "right":
#     answer = input("You came to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
#     if answer.lower() == "back":
#         print("You go back and you lose.")

#     elif answer.lower() == "cross":
#         answer = input("You cross the bridge and met a stranger. Do you talk to them (yes/no)? ")

#         if answer.lower() == "yes":
#             print("You talk to the stranger and the stranger gave you the treasure map. You won!")
#         elif answer.lower() == "no":
#             print("You ignored the stranger and the stranger gets upset and shoot you. And you die!")
#         else:
#             print("Not a valid option. You lose.")
    
#     else:
#         print("Not a valid option. You lose.")
# else:
#     print("Not a valid option. You lose.")

# print(f"Thanks for playing! {name.title()}")


# from color_print import format_text

# # color_print("Hello", "green") # Color print is not avaible
# # or
# s = format_text("Hello", "red")
# print(s)

# import color_print
# print(dir(color_print))

# name = 12
# print(dir(name))

# from color_print import info, success, error, warning, debug

# info("Hello")       # general info (usually blue)
# success("Hello")    # success message (green)
# error("Hello")      # error message (red)
# warning("Hello")    # warning (yellow)
# debug("Hello")      # debug message

# import math 

# print(dir(math))

# a = math.sin(90)

# print(math.sin.__doc__)

# pip install pandas numpy matplotlib seaborn scikit-learn

#number=5
# for i in range(number):
#     # print(i, end=" ")
#     print(i)

# range(n) -> 0 till n-1
# range(start, end) -> range(2, 5) -> 2, 3, 4
# range(s, e, step) -> range(3, 11, 2) -> 3, 5, 7, 9

age=17

match age:
    case a if a < 13:
        print("Child")
    case a if 13 <= a < 20:
        print("Teenager")
    case a if a >= 20:
        print("Adult")
        