


# NAME = "SMARTKELVIN"
# print(NAME.lower())
# print(NAME.count('N'))
# print(NAME*3)


# string
# first_name  = "bro"
# last_name = "bob"
# full_name = first_name   + last_name
# print("smart"+last_name)

#  int
# age = 21
# age += 3
# print("your age is :" + str(age))

#  float
# height = 250.7
# print(" your height is :" + str(height )+ 'cm') 
# print(type(height))

# boolean
# human = 'True'
# # print(human)
# print( 'are you a human :' + str(human ))

# mulitiple assignments
# name = "bob"
# age = 31
# attractive = True
# name, age,attrgetter = "bob" , 21 , True,
# print(name)
# print(age)
# print(attractive)
 
#  input

# name = input ("what is your name")
# age = int (input("how old are you"))
# height = float (input("how tall are you"))
# print ("hello" + name )
# print("you are " + str(age)+ "years old")
# print("you are" + str(height)+"cm tall")

#  import math

# pi = 3.14
# x = 3
# y =5
# z = 15
# print (round (pi))
# print(abs(pi))
# print(math.sqrt(500))
# print (max(x, y, z))
# print (min(x, y, z))

#  slicing creat a subsrting by extracing element from another string
# [start: stop : step]


# from audioop import reverse
# name = "smart kelvin"
# first_name = name[6:9]
# first_name = name[1:5]
# first_name = name[5:]
# reverse_name = name [::-7]
# print(first_name)

# if, elif, else statement
# age = int(input('how old are you '))

# if age >= 21: 
#     print('you are an adult')
# elif  age == 100 :
#     print('you are too old')
    
# else:
#     print("you are a baby")

# logical operator2

# # while loop = a statement that will exacute its block of code as long as its condition remains true
#     print('i am downing in the ocean)')

# name = None

# while not name:
#     name = input('ENTER YOUT NAME')
# #     print("hello" + name)

#  for loop  = a statement that excutute its block of code a limited ampout of time

# for i in range(10) :
#  print (i + 1)

# for i in range(60,79) :
#     print(i + 1)
# for i in range(60,79,2) :
#     print(i)


# import time
# for secodes in range(5,0,-1):
#     print(secodes)
#     time.sleep(2)
#     print("happy new year")


# while loop = unlimited
# for loop = limited

# nested loop = it is having a loop inside inside a loop

# rows = int(input("how many colowms?"))
# columns = int(input("how manty columns ?"))
# symbols = input("enter a sysmbolsto use")

# for I in range (rows):
#     for j in range (columns):
#         print(symbols,end="")
#         print()



# break = used to terminate the loop
# Continue =KIPS TO THE NEXT ITARATION OF THE LOOP
# pass = PASS A LOOP 

# from re import I


# for i in range(1,21):
#     if i ==10:
#         pass
#     else:
#         print(i)

# list = used to store mulitiple items in a variable
# house = ["pizza","orange","spaetr","fidelet"]
# print(house[3])

# # house.pop()
# # house.sort()
# house.remove("pizza")

# for x in house:
#     print(x)


# set = collection which is unordered,unindexed,and no duplicate values 
#     color = {"white","black","red","green","yellow","blue",}

# color.remove("white")
# color.add('green')
#  for x in color:
#     print(x)


# dictionary = a changeable,unordred collections of unique key values pairs 
# state_capitals = {
#     'Arkansas': 'Little Rock',
#     'Colorado': 'Denver',
#     'California': 'Sacramento',
#     'Georgia': 'Atlanta'
# }
# print(state_capitals['California'])

# function =  a fuction is block of code which exacuted only when it is called

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus


# # def tail(filename, n=10):
#     with open(filename, "r") as f:
#     	lines = f.readlines()
#     for line in 
#         print(line)

# function calls 
# 
# next fuction = function call inside other function call
# num = input("enter a whole positive number")
# num = float(num) 
# num = abs(num)
# num = round (num)
# print(num)
#  print(round(abs(float(input("enter a whole positive number")))))

# *args =  parameter thst will pack all argument into a tuple usefulso that a function can accept a varying amount of argument

# def add(*sugar):
#     sum = 0
#     sugar= list(sugar)
#     sugar[0] = 0
#     for i in sugar:
#         sum += i
# print(add(1,2,3,4,5,6,))

# tuples
# x = ("apple", "banana", "cherry")
# #display x:
# print(x)
# #display the data type of x:
# print(type(x))

# x = memoryview(bytes(5))
# #display x:
# print(x)
# #display the data type of x:
# print(type(x))


# str.format()
# animal = "cow"
# item ="moon"
# print("the " +animal+" jumped over the "+item)

# import random
# x = random.randint(1,6)
# y = random.randint()
# print(y)

# from random import random

# from random import random


# cards = [1,2,3,4,5,6,7,8,9,'k', 'o', 'o', 'o', 'o', 'o', ]
# random.shuffle(cards)
# print(cards)

# help('modules')


# rock paper and scissor
# import random

# while True:
#     choices = ["rock","paper","scissors"]

#     computer = random.choice(choices)
#     player = None

#     while player not in choices:
#         player = input("rock, paper, or scissors?: ").lower()

#     if player == computer:
#         print("computer: ",computer)
#         print("player: ",player)
#         print("Tie!")

#     elif player == "rock":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     elif player == "scissors":
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     elif player == "paper":
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     play_again = input("Play again? (yes/no): ").lower()

#     if play_again != "yes":
#         break

# print("Bye!")


# phython quiz game
# -------------------------
# def new_game():

#     guesses = []
#     correct_guesses = 0
#     question_num = 1

#     for key in questions:
#         print("-------------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("Enter (A, B, C, or D): ")
#         guess = guess.upper()
#         guesses.append(guess)

#         correct_guesses += check_answer(questions.get(key), guess)
#         question_num += 1

#     display_score(correct_guesses, guesses)

# # # -------------------------
# def check_answer(answer, guess):

#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG!")
#         return 0

# # # -------------------------
# def display_score(correct_guesses, guesses):
#     print("-------------------------")
#     print("RESULTS")
#     print("-------------------------")

#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()

#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()

#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is: "+str(score)+"%")

# # -------------------------
# def play_again():

#     response = input("Do you want to play again? (yes or no): ")
#     response = response.upper()

#     if response == "YES":
#         return True
#     else:
#         return False
# -------------------------


# questions = {
#  "Who created Python?: ": "A",
#  "What year was Python created?: ": "B",
#  "Python is tributed to which comedy group?: ": "C",
#  "Is the Earth round?: ": "A"
# }

# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#           ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

# new_game()

# while play_again():
#     new_game()

# print("Byeeeeee!")

# object
# car_1 = Car("Chevy","Corvette",2021,"blue")
# car_2 = Car("Ford","Mustang",2022,"red")

# car_1.drive()
# car_2.stop()
# #------------------------------------------------------------------
# class Car:

#     def __init__(self,make,model,year,color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color

#     def drive(self):
#         print("This "+self.model+" is driving")

#     def stop(self):
#         print("This "+self.model+" is stopped")
# #------------------------------------------------------------------

#python #class #variables




#---------------------------------------------------------------------fro
#  from  car import car

# car_1 = Car("Chevy","Corvette",2021,"blue")
# car_2 = Car("Ford","Mustang",2022,"red")

# #Car.wheels = 2

# print(car_1.wheels)
# print(car_2.wheels)
#---------------------------------------------------------------------
# class Car:

#     wheels = 4 #class variable

    # def __init__(self,make,model,year,color):
        # self.make = make    #instance variable
        # self.model = model  #instance variable
        # self.year = year    #instance variable
        # self.color = color  #instance variable







#python #inheritance #tutorial

# class Animal:

#     alive = True

#     def eat(self):
#         print("This animal is eating")

#     def sleep(self):
#         print("This animal is sleeping")

# class Rabbit(Animal):

#     def run(self):
#         print("This rabbit is running")

# class Fish(Animal):

#     def swim(self):
#         print("This fish is swimming")

# class Hawk(Animal):

#     def fly(self):
#         print("This hawk is flying")

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# # print(rabbit.alive)
# # fish.eat()
# # hawk.sleep()

# rabbit.run()
# fish.swim()
# hawk.fly()

# mutiple inhertances 

# class Organism:
    
#     alive = True

# class Animal(Organism):

#     def eat(self):
#         print("This animal is eating")

# class Dog(Animal):

#     def bark(self):
#         print("This dog is barking")


# dog = Dog()
# print(dog.alive)    # inherited from the Organism class
# dog.eat()           # inherited from the Animal class
# dog.bark()          # defined in Dog class

#python #method #override

# class Animal:

#     def eat(self):
#         print("This animal is eating")

# class Rabbit(Animal):

#     def eat(self):
#         print("This rabbit is eating a carrot")


# rabbit = Rabbit()
# rabbit.eat()


# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

# class Car:

#     def turn_on(self):
#         print("You start the engine")
#         return self

#     def drive(self):
#         print("You drive the car")
#         return self

#     def brake(self):
#         print("You step on the brakes")
#         return self

#     def turn_off(self):
#         print("You turn off the engine")
#         return self

# car = Car()

# car.turn_on().drive()
# car.brake().turn_off()
# car.turn_on().drive().brake().turn_off()


# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()

#python #super #super()

# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

# class Square(Rectangle):

#     def __init__(self, length, width):
#         super().__init__(length,width)

#     def area(self):
#         return self.length*self.width

# class Cube(Rectangle):

#     def __init__(self, length, width, height):
#         super().__init__(length,width)
#         self.height = height

#     def volume(self):
#         return self.length*self.width*self.height


# square = Square(3, 3)
# cube = Cube(3, 3, 3)

# print(square.area())
# print(cube.volume())

 #python #abstract #classes

#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation.

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):

#     def go(self):
#         print("You drive the car")

#     def stop(self):
#         print("This car is stopped")

# class Motorcycle(Vehicle):

#     def go(self):
#         print("You ride the motorcycle")

#     def stop(self):
#         print("This motorcycle is stopped")


# #vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()

# #vehicle.go()
# car.go()
# motorcycle.go()

# #vehicle.stop()
# car.stop()
# motorcycle.stop()




#python #objects #arguments

# class Car:

#     color = None

# class Motorcycle:

#     color = None

# def change_color(vehicle,color):

#     vehicle.color = color


# car_1 = Car()
# car_2 = Car()
# car_3 = Car()

# bike_1 = Motorcycle()

# change_color(car_1,"red")
# change_color(car_2,"white")

# change_color(car_3,"blue")
# change_color(bike_1,"black")

# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)



#python #duck #typing

# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

# class Duck:

#     def walk(self):
#         print("This duck is walking")

#     def talk(self):
#         print("This duck is qwuacking")

# class Chicken:

#     def walk(self):
#         print("This chicken is walking")

#     def talk(self):
#         print("This chicken is clucking")

# class Person():

#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")


# duck = Duck()
# chicken = Chicken()
# person = Person()

# person.catch(chicken)




# python #walrus operator

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#      if food == "quit"
#           break
#   foods.append(food)

# foods = list()
# while (food := input("What food do you like?: ")) != "quit":
#     foods.append(food)



#python #function #variable

# def hello():
#     print("Hello")


# hi = hello
# hi()
# print (hi)

# say = print
# say("Whoa! I can't believe this works! :O")



#python #higher-order #functions

#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ----- 1. accepts a function as an argument ----- 
# def loud(text):
#    return text.upper()

# def quiet(text):
#    return text.lower()

# def hello(func):
#    text = func("Hello")
#    print(text)


# hello(loud)
# hello(quiet)

# ------------ 2. returns a function ------------- 
# def divisor(x):
#    def dividend(y):
#        return y / x
#    return dividend


# divide = divisor(2)
# print(divide(10))






#python #lambda #function

# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

# double = lambda x: x * 2
# print(double(1))

# multiply = lambda x, y: x * y
# print(multiply(1,2))

# add = lambda x, y, z: x + y + z
# print(add(1,2,3))

# full_name = lambda first_name, last_name: first_name+" "+last_name
# print(full_name("Bro","Code"))




#python #sorting #sort
# -------------------------------------------------------------------
# sort() method   = used with lists
# sort() function = used with iterables

# students = (("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick","D", 36),
#             ("Spongebob","B", 20),
#             ("Mr.Krabs","C", 78))

# grade = lambda grades:grades[1]
# # students.sort(key=age)                     # sorts current list
# sorted_students = sorted(students,key=grade) # sorts and creates a new list

# for i in sorted_students:
#     print(i)



# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

# store = [("shirt",20.00),
#          ("pants",25.00),
#          ("jacket",50.00),
#          ("socks",10.00)]

# to_euros = lambda data: (data[0],data[1]*0.82)
# # to_dollars = lambda data: (data[0],data[1]/0.82)

# store_euros = list(map(to_euros, store))

# for i in store_euros:
#     print(i)



#python #filter #function

# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true

#               filter(function, iterable)


#python #reduce #function

# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

# import functools

# letters = ["H","E","L","L","O"]
# word = functools.reduce(lambda x, y,:x + y,letters)
# print(word)

# import functools


# factorial = [5,4,3,2,1]
# result =  functools.reduce(lambda x, y,:x * y,factorial)
# print(result)



#python #list #comprehension

# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
# squares = []                # create an empty list
# for i in range(1,11):       # create a for loop
#     squares.append(i * i)    # define what each loop iteration should do
# print(squares)

# # create a list AND defines what each loop iteration should do
# squares = [i * i for i in range(1,11)]
# print(squares)




#python #dictionary #comprehension

# -------------------------------------------------------------------------
# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)

# -------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# -----


#python #zip #function

# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")
# login_dates = ["1/1/2021","1/2/2021","1/3/2021"]

# # --------------------------------------
# users = list(zip(usernames,passwords))

# for i in users:
#     print(i)

# --------------------------------------
# users = dict(zip(usernames,passwords))

# for key,value in users.items():
#     print(key+" : "+value)

# --------------------------------------
# users = zip(usernames,passwords,login_dates)

# for i in users:
#     print(i)




    

#python #name #main

# ***********************************
# if __name__ == '__main__'
# ***********************************

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the __name__ variable a value of '__main__' if it's
#  the initial module being run

# def main():
#     print("Hello!")


# if __name__ == '__main__':
#     main()


#python #time #module

# ***************************************************************************
# import time
# # ***************************************************************************
# print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
# #                                        epoch = when your computer thinks time began (reference point)
# print(time.time())      # return current seconds since epoch
# print(time.ctime(time.time())) # will get current time

# ***************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# ***************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)




#python #threading #multithreading

# ******************************************************
# Python threading tutorial
# ******************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

# import threading
# import time


# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")


# def drink_coffee():
#     time.sleep(4)
#     print("You drank coffee")


# def study():
#     time.sleep(5)
#     print("You finish studying")


# x = threading.Thread(target=eat_breakfast, args=())
# x.start()

# y = threading.Thread(target=drink_coffee, args=())
# y.start()

# z = threading.Thread(target=study, args=())
# z.start()

# x.join()
# y.join()
# z.join()

# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())
 
 
 
 
 
 #python #daemon #threads

# ************************************************************
# Python daemon threads
# ************************************************************

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

# import threading
# import time


# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for: ", count, "seconds")


# x = threading.Thread(target=timer, daemon=True)
# x.start()

# x.setDaemon(True)
# print(x.isDaemon())

# answer = input("Do you wish to exit?")



# ***********************************
# Python multiprocessing
# ***********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)
# ***********************************




#Python #tkinter #GUI #tutorial #beginners

# from tkinter import *

# window = Tk() #instantiate an instance of a window
# window.geometry("420x420")
# window.title("smart kelvin first GUI program")

# # icon = PhotoImage(file='logo.png')
# # window.iconphoto(True,icon)
# window.config(background="#5cfcff")

# window.mainloop() #place window on computer screen, listen for events





#Python #label #labels #tkinter #GUI #code #example #tutorial for #beginners

# from tkinter import *

# # label = an area widget that holds text and/or an image within a window

# window = Tk()

# photo = PhotoImage(file='person.png')

# label = Label(window,
#               text="bro, do you even code?",
#               font=('Arial',40,'bold'),
#               fg='#00FF00',
#               bg='black',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#             #   image=photo,
#               compound='bottom')
# label.pack()
# #label.place(x=0,y=0)

# window.mainloop()




#Python #tkinter #button #buttons #GUI #tutorial #beginners #code

# from tkinter import *

# # button = you click it, then it does stuff

# count = 0

# def click():
#     global count
#     count+=1
#     print(count)

# window = Tk()

# photo = PhotoImage(file='like.png')

# button = Button(window,
#                 text="click me!",
#                 command=click,
#                 font=("Comic Sans",30),
#                 fg="#00FF00",
#                 bg="black",
#                 activeforeground="#00FF00",
#                 activebackground="black",
#                 state=ACTIVE,
#                 image=photo,
#                 compound='bottom')
# button.pack()

# window.mainloop()





#Python #entry #box #widget #tkinter #GUI #code #example #tutorial #beginners

# from tkinter import *

# #entry widget = textbox that accepts a single line of user input

# def submit():
#     username = entry.get()
#     print("Hello "+username)

# def delete():
#     entry.delete(0,END)

# def backspace():
#     entry.delete(len(entry.get())-1, END)

# window = Tk()

# entry = Entry(window,
#               font=("Arial",50),
#               fg="#00FF00",
#               bg="black")

# #entry.insert(0,'Spongebob')
# #entry.config(show="*")
# #entry.config(state=DISABLED)

# entry.pack(side=LEFT)

# submit_button = Button(window,text="submit",command=submit)
# submit_button.pack(side=RIGHT)

# delete_button = Button(window,text="delete",command=delete)
# delete_button.pack(side=RIGHT)

# backspace_button = Button(window,text="backspace",command=backspace)
# backspace_button.pack(side=RIGHT)

# window.mainloop()




#Python #checkbox #checkbutton #tkinter #GUI #tutorial #beginners

# from tkinter import *

# def display():
#     if(x.get()==1):
#         print("You agree!")
#     else:
#         print("You don't agree :(")

# window = Tk()

# x = IntVar()

# python_photo = PhotoImage(file='Python.png')

# check_button = Checkbutton(window,
#                            text="I agree to something",
#                            variable=x,
#                            onvalue=1,
#                            offvalue=0,
#                            command=display,
#                            font=('Arial',20),
#                            fg='#00FF00',
#                            bg='black',
#                            activeforeground='#00FF00',
#                            activebackground='black',
#                            padx=25,
#                            pady=10,
#                            image=python_photo,
#                            compound='left')
# check_button.pack()


# window.mainloop()





# radio button = similar to checkbox, but you can only select one from a group
# from tkinter import *

# food = ["pizza","hamburger","hotdog"]

# def order():
#     if(x.get()==0):
#         print("You ordered pizza!")
#     elif(x.get()==1):
#         print("You ordered a hamburger!")
#     elif(x.get()==2):
#         print("You ordered a hotdog!")
#     else:
#         print("huh?")

# window = Tk()

# pizzaImage = PhotoImage(file='pizza.png')
# hamburgerImage = PhotoImage(file='hamburger.png')
# hotdogImage = PhotoImage(file='hotdog.png')
# foodImages = [pizzaImage,hamburgerImage,hotdogImage]

# x = IntVar()

# for index in range(len(food)):
#     radiobutton = Radiobutton(window,
#                               text=food[index], #adds text to radio buttons
#                               variable=x, #groups radiobuttons together if they share the same variable
#                               value=index, #assigns each radiobutton a different value
#                               padx = 25, #adds padding on x-axis
#                               font=("Impact",50),
#                               image = foodImages[index], #adds image to radiobutton
#                               compound = 'left', #adds image & text (left-side)
#                               #indicatoron=0, #eliminate circle indicators
#                               #width = 375, #sets width of radio buttons
#                               command=order #set command of radiobutton to function
#                               )
#     radiobutton.pack(anchor=W)
# window.mainloop()






# from tkinter import *

# def submit():
#     print("The temperature is: "+ str(scale.get())+ " degrees C")

# window = Tk()

# hotImage = PhotoImage(file='hot.png')
# hotLabel = Label(image=hotImage)
# hotLabel.pack()

# scale = Scale(window,
#               from_=100,
#               to=0,
#               length=600,
#               orient=VERTICAL, #orientation of scale
#               font = ('Consolas',20),
#               tickinterval = 10, #adds numeric indicators for value
#               #showvalue = 0, #hide current value
#               resolution = 5, #increment of slider
#               troughcolor = '#69EAFF',
#               fg = '#FF1C00',
#               bg = '#111111'

#               )
# scale.set(((scale['from']-scale['to'])/2)+scale['to']) #set current value of slider

# scale.pack()

# coldImage = PhotoImage(file='cold.png')
# coldLabel = Label(image=coldImage)
# coldLabel.pack()

# button = Button(window,text='submit',command=submit)
# button.pack()

# window.mainloop()




# listbox = A listing of selectable text items within it's own container

# def submit():

#     food = []

#     for index in listbox.curselection():
#         food.insert(index,listbox.get(index))

#     print("You have ordered: ")
#     for index in food:
#         print(index)

# def add():
#     listbox.insert(listbox.size(),entryBox.get())
#     listbox.config(height=listbox.size())

# def delete():
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)

#     listbox.config(height=listbox.size())

# from tkinter import *

# window = Tk()

# listbox = Listbox(window,
#                   bg="#f7ffde",
#                   font=("Constantia",35),
#                   width=12,
#                   selectmode=MULTIPLE)
# listbox.pack()

# listbox.insert(1,"pizza")
# listbox.insert(2,"pasta")
# listbox.insert(3,"garlic bread")
# listbox.insert(4,"soup")
# listbox.insert(5,"salad")

# listbox.config(height=listbox.size())

# entryBox = Entry(window)
# entryBox.pack()

# frame = Frame(window)
# frame.pack()

# submitButton = Button(frame,text="submit",command=submit)
# submitButton.pack(side=LEFT)

# addButton = Button(frame,text="add",command=add)
# addButton.pack(side=LEFT)

# deleteButton = Button(frame,text="delete",command=delete)
# deleteButton.pack(side=LEFT)

# window.mainloop()




#Python #GUI #messagebox #tkinter #tutorial #beginners

# from tkinter import *
# from tkinter import messagebox #import messagebox library

# def click():
#     messagebox.showinfo(title='This is an info message box',message='You are a person')
#     messagebox.showwarning(title='WARNING!',message='You have A VIRUS!!!!')
#     messagebox.showerror(title='ERROR!',message='something went wrong :(')

#     if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
#         print('You did a thing!')
#     else:
#         print('You canceled a thing! :(')

#     if messagebox.askretrycancel(title='ask ok cancel',message='Do you want retry the thing?'):
#         print('You retried a thing!')
#     else:
#         print('You canceled a thing! :(')

#     if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
#         print('I like cake too :)')
#     else:
#         print('Why do you not like cake? :(')

#     answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
#     if(answer == 'yes'):
#         print('I like pie too :)')
#     else:
#         print('Why do you not like pie? :(')

#     answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?',icon='question')
#     if(answer==True):
#         print("You like to code :)")
#     elif(answer==False):
#         print("Then why are you watching a video on coding?")
#     else:
#         print("You have dodged the question ")

# window = Tk()

# button = Button(window,command=click,text='click me')
# button.pack()

# window.mainloop()


#Python #Tkinter #colorchooser #GUI #tutorial #beginners

# from tkinter import *
# from tkinter import colorchooser

# def click():
#     color = colorchooser.askcolor()
#     colorHex = color[1]
#     window.config(bg=colorHex)

# window = Tk()
# window.geometry("420x420")
# button = Button(text='click me',command=click)
# button.pack()
# window.mainloop()


# text widget = functions like a text area, you can enter multiple lines of text
# from tkinter import *

# def submit():
#     input = text.get("1.0",END)
#     print(input)

# window = Tk()
# text = Text(window,
#             bg="light yellow",
#             font=("Ink Free",25),
#             height=8,
#             width=20,
#             padx=20,
#             pady=20,
#             fg="purple")
# text.pack()
# button = Button(window,text="submit",command=submit)
# button.pack()
# window.mainloop()



#Python #GUI #filedialog #tkinter #open #file #tutorial #beginners
# from tkinter import *
# from tkinter import filedialog

# def openFile():
#     filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
#                                           title="Open file okay?",
#                                           filetypes= (("text files","*.txt"),
#                                           ("all files","*.*")))
#     file = open(filepath,'r')
#     print(file.read())
#     file.close()

# window = Tk()
# button = Button(text="Open",command=openFile)
# button.pack()
# window.mainloop()





#Python #GUI #save #filedialog #tkinter #file #tutorial #beginners

# from tkinter import *
# from tkinter import filedialog

# def saveFile():
#     file = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
#                                     defaultextension='.txt',
#                                     filetypes=[
#                                         ("Text file",".txt"),
#                                         ("HTML file", ".html"),
#                                         ("All files", ".*"),
#                                     ])
#     if file is None:
#         return
#     filetext = str(text.get(1.0,END))
#     #filetext = input("Enter some text I guess: ") //use this if you want to use console window
#     file.write(filetext)
#     file.close()

# window = Tk()
# button = Button(text='save',command=saveFile)
# button.pack()
# text = Text(window)
# text.pack()
# window.mainloop()




#Python #menubar #menu #tkinter #GUI #tutorial #beginners

# from tkinter import *

# def openFile():
#     print("File has been opened!")
# def saveFile():
#     print("File has been saved!")
# def cut():
#     print("You cut some text!")
# def copy():
#     print("You copied some text!")
# def paste():
#     print("You pasted some text!")

# window = Tk()

# openImage = PhotoImage(file="file.png")
# saveImage = PhotoImage(file="save.png")
# exitImage = PhotoImage(file="exit.png")

# menubar = Menu(window)
# window.config(menu=menubar)

# fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="File",menu=fileMenu)
# fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
# fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
# fileMenu.add_separator()
# fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')

# editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
# menubar.add_cascade(label="Edit",menu=editMenu)
# editMenu.add_command(label="Cut",command=cut)
# editMenu.add_command(label="Copy",command=copy)
# editMenu.add_command(label="Paste",command=paste)

# window.mainloop()




# frame = a rectangular container to group and hold widgets

# from tkinter import *

# window = Tk()

# frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
# frame.pack()

# Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
# Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
# Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

# window.mainloop()


#Python #GUI #tabs #notebook #tkinter #GUI #tutorial #beginners

# from tkinter import *
# from tkinter import ttk

# window = Tk()

# notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

# tab1 = Frame(notebook) #new frame for tab 1
# tab2 = Frame(notebook) #new frame for tab 2

# notebook.add(tab1,text="Tab 1")
# notebook.add(tab2,text="Tab 2")
# notebook.pack(expand=True,fill="both")  #expand = expand to fill any space not otherwise used
#                                        #fill = fill space on x and y axis
# Label(tab1,text="Hello, this is tab#1",width=50,height=25).pack()
# Label(tab2,text="Goodbye, this is tab#2",width=50,height=25).pack()

# window.mainloop()




#Python #grid #tkinter #GUI #tutorial

# from tkinter import *

# #grid() = geometry manager that organizes widgets in a table-like structure in a parent widget

# window = Tk()

# titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

# firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
# firstNameEntry = Entry(window).grid(row=1,column=1)

# lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
# lastNameEntry = Entry(window).grid(row=2,column=1)

# emailLabel = Label(window,text="email: ",bg="blue").grid(row=3,column=0)
# emailEntry = Entry(window).grid(row=3,column=1)

# submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

# window.mainloop()



#Python #progress #bar #ProgressBar #tkinter #GUI #tutorial
# from tkinter import *
# from tkinter.ttk import *
# import time

# def start():
#     GB = 100
#     download = 0
#     speed = 1
#     while(download<GB):
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download+=speed
#         percent.set(str(int((download/GB)*100))+"%")
#         text.set(str(download)+"/"+str(GB)+" GB completed")
#         window.update_idletasks()

# window = Tk()

# percent = StringVar()
# text = StringVar()

# bar = Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)

# percentLabel = Label(window,textvariable=percent).pack()
# taskLabel = Label(window,textvariable=text).pack()

# button = Button(window,text="download",command=start).pack()

# window.mainloop()




#Python #2D #canvas #graphics #widget #tutorial #beginners
# canvas =  widget that is used to draw graphs, plots, images in a window

# from tkinter import *

# window = Tk()

# canvas = Canvas(window,height=500,width=500)
# canvas.create_line(0,0,500,500,fill="blue",width=5)
# canvas.create_line(0,500,500,0,fill="red",width=5)
# canvas.create_rectangle(50,50,250,250,fill="purple")
# points = [250,0,500,500,0,500]
# canvas.create_polygon(points,fill="yellow",outline="black",width=5)
# canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)
# canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
# canvas.create_oval(190,190,310,310,fill="white",width=10)

# canvas.pack()

# window.mainloop()



#Python #key #bind #events #keyboard #tkinter #GUI #tutorial #beginners

# from tkinter import *

# def doSomething(event):
#     # print("You pressed: " + event.keysym)
#     label.config(text=event.keysym)

# window = Tk()

# window.bind("<Key>",doSomething)

# label = Label(window,font=("Helvetica",100))
# label.pack()

# window.mainloop()





#Python #mouse #event #bind #GUI #tkinter #tutorial #beginners

# from tkinter import *

# def doSomething(event):
#     print("Mouse coordinates: " + str(event.x)+","+str(event.y))

# window = Tk()

# window.bind("<Button-1>",doSomething) #left mouse click
# #window.bind("<Button-2>",doSomething) #scroll wheel
# #window.bind("<Button-3>",doSomething) #right mouse click
# #window.bind("<ButtonRelease>",doSomething)#mousebutton release
# #window.bind("<Enter>",doSomething) #enter the window
# #window.bind("<Leave>",doSomething) #leave the window
# #window.bind("<Motion>",doSomething) #Where the mouse moved
# window.mainloop()



#Python #drag #drop #GUI #tkinter #tutorial #beginners


# from tkinter import *

# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y

# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)

# window = Tk()

# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)

# label2 = Label(window,bg="blue",width=10,height=5)
# label2.place(x=100,y=100)

# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)

# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)

# window.mainloop()




#Python #move #images #widgets #keys #keyboard
#------------move widgets on window-------------
# from tkinter import *

# def move_up(event):
#    label.place(x=label.winfo_x(), y=label.winfo_y()-10)
# def move_down(event):
#    label.place(x=label.winfo_x(), y=label.winfo_y()+10)
# def move_left(event):
#    label.place(x=label.winfo_x()-10, y=label.winfo_y())
# def move_right(event):
#    label.place(x=label.winfo_x()+10, y=label.winfo_y())

# window = Tk()
# window.geometry("500x500")

# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)

# myimage = PhotoImage(file='racecar.png')
# label = Label(window,image=myimage)
# label.place(x=0,y=0)

# window.mainloop()

# #-------------move images on canvas-------------

# from tkinter import *

# def move_up(event):
#    canvas.move(myimage,0,-10)
# def move_down(event):
#    canvas.move(myimage,0,10)
# def move_left(event):
#    canvas.move(myimage,-10,0)
# def move_right(event):
#    canvas.move(myimage,10,0)

# window = Tk()

# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)

# canvas = Canvas(window,width=500,height=500)
# canvas.pack()

# photoimage = PhotoImage(file='racecar.png')
# myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

# window.mainloop()


# move image with keys
#------------move widgets on window-------------
# from tkinter import *

# def move_up(event):
#    label.place(x=label.winfo_x(), y=label.winfo_y()-10)
# def move_down(event):
#    label.place(x=label.winfo_x(), y=label.winfo_y()+10)
# def move_left(event):
#    label.place(x=label.winfo_x()-10, y=label.winfo_y())
# def move_right(event):
#    label.place(x=label.winfo_x()+10, y=label.winfo_y())

# window = Tk()
# window.geometry("500x500")

# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)
# window.bind("<Up>",move_up)
# window.bind("<Down>",move_down)
# window.bind("<Left>",move_left)
# window.bind("<Right>",move_right)

# myimage = PhotoImage(file='racecar.png')
# label = Label(window,image=myimage)
# label.place(x=0,y=0)

# window.mainloop()

#-------------move images on canvas-------------

# from tkinter import *

# def move_up(event):
#    canvas.move(myimage,0,-10)
# def move_down(event):
#    canvas.move(myimage,0,10)
# def move_left(event):
#    canvas.move(myimage,-10,0)
# def move_right(event):
#    canvas.move(myimage,10,0)

# window = Tk()

# window.bind("<w>",move_up)
# window.bind("<s>",move_down)
# window.bind("<a>",move_left)
# window.bind("<d>",move_right)

# canvas = Canvas(window,width=500,height=500)
# canvas.pack()

# photoimage = PhotoImage(file='racecar.png')
# myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

# window.mainloop()

# create 3d aniimation

# from tkinter import *
# import time

# WIDTH = 500
# HEIGHT = 500
# xVelocity = 1
# yVelocity = 1
# window = Tk()

# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# background_photo = PhotoImage(file='space.png')
# background = canvas.create_image(0,0,image=background_photo,anchor=NW)

# photo_image = PhotoImage(file='ufo.png')
# my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

# image_width = photo_image.width()
# image_height = photo_image.height()

# while True:
#     coordinates = canvas.coords(my_image)
#     print(coordinates)
#     if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#         xVelocity = -xVelocity
#     if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
#         yVelocity = -yVelocity
#     canvas.move(my_image,xVelocity,yVelocity)
#     window.update()
#     time.sleep(0.01)

# window.mainloop()


# mutiple Animation

# #*********************************************************
# from tkinter import *
# from Ball import *
# import time

# window = Tk()

# WIDTH = 500
# HEIGHT = 500

# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# volley_ball = Ball(canvas,0,0,100,1,1,"white")
# tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
# basket_ball = Ball(canvas,0,0,125,3,5,"orange")
# bowling_ball = Ball(canvas,0,0,75,2,1,"black")

# while True:
#     volley_ball.move()
#     tennis_ball.move()
#     basket_ball.move()
#     bowling_ball.move()
#     window.update()
#     time.sleep(0.01)

# window.mainloop()
# #*********************************************************
# class Ball:


#     def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
#         self.canvas = canvas
#         self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
#         self.xVelocity = xVelocity
#         self.yVelocity = yVelocity

#     def move(self):
#         coordinates = self.canvas.coords(self.image)

#         if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
#             self.xVelocity = -self.xVelocity
#         if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
#             self.yVelocity = -self.yVelocity

#         self.canvas.move(self.image,self.xVelocity,self.yVelocity)
# #*********************************************************

# Python clock program 🕒

# from tkinter import *
# from time import *

# def update():
#     time_string = strftime("%I:%M:%S %p")
#     time_label.config(text=time_string)

#     day_string = strftime("%A")
#     day_label.config(text=day_string)

#     date_string = strftime("%B %d, %Y")
#     date_label.config(text=date_string)

#     window.after(1000,update)


# window = Tk()

# time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
# time_label.pack()

# day_label = Label(window,font=("Ink Free",25,"bold"))
# day_label.pack()

# date_label = Label(window,font=("Ink Free",30))
# date_label.pack()

# update()

# window.mainloop()



# (If you have 2-Factor Authentication set up on your account, that may prevent you from logging in from an unknown device)
# **************************************************************
# Python email
# **************************************************************


# import smtplib

# sender = "sender@gmail.com"
# receiver = "receiver@gmail.com"
# password = "password123"
# subject = "Python email test"
# body = "I wrote an email! :D"

# # header
# message = f"""From: Snoop Dogg{sender}
# To: Nicholas Cage{receiver}
# Subject: {subject}\n
# {body}
# """

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()

# try:
#     server.login(sender,password)
#     print("Logged in...")
#     server.sendmail(sender, receiver, message)
#     print("Email has been sent!")

# except smtplib.SMTPAuthenticationError:
#     print("unable to sign in")

# # **************************************************************





# ***************************
# run .py file with cmd
# # ***************************
# # save file as .py (Python file)
# # go to command prompt
# # navigate to directory w/ your file: cd C:\Users\BroCode\Desktop
# # invoke python interpreter + script: python hello_world.py
# # ***************************

# print("Hello World!")

# name = input("What's your name?: ")

# print("Hello "+name)

# # ***************************







# **************************************************************
# Python pip
# **************************************************************
#       pip = package manager for packages and modules from Python Package Index
#
#       included for Python versions 3.4+
#       open command prompt
#
#       help:                                          pip
#       check:                                       pip --version
#       update:                                     pip install --upgrade pip
#       installed packages:                pip list
#       check outdated packages:    pip list --outdated
#       update a package:                  pip install "package name" --upgrade
#       install a package:                    pip install "package name"
#
# **************************************************************



# Python Calculator
# **************************************************************
# from tkinter import *

# def button_press(num):

#     global equation_text

#     equation_text = equation_text + str(num)

#     equation_label.set(equation_text)

# def equals():

#     global equation_text

#     try:

#         total = str(eval(equation_text))

#         equation_label.set(total)

#         equation_text = total

#     except SyntaxError:

#         equation_label.set("syntax error")

#         equation_text = ""

#     except ZeroDivisionError:

#         equation_label.set("arithmetic error")

#         equation_text = ""

# def clear():

#     global equation_text

#     equation_label.set("")

#     equation_text = ""


# window = Tk()
# window.title("Calculator program")
# window.geometry("500x500")

# equation_text = ""

# equation_label = StringVar()

# label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
# label.pack()

# frame = Frame(window)
# frame.pack()

# button1 = Button(frame, text=1, height=4, width=9, font=35,
#                  command=lambda: button_press(1))
# button1.grid(row=0, column=0)

# button2 = Button(frame, text=2, height=4, width=9, font=35,
#                  command=lambda: button_press(2))
# button2.grid(row=0, column=1)

# button3 = Button(frame, text=3, height=4, width=9, font=35,
#                  command=lambda: button_press(3))
# button3.grid(row=0, column=2)

# button4 = Button(frame, text=4, height=4, width=9, font=35,
#                  command=lambda: button_press(4))
# button4.grid(row=1, column=0)

# button5 = Button(frame, text=5, height=4, width=9, font=35,
#                  command=lambda: button_press(5))
# button5.grid(row=1, column=1)

# button6 = Button(frame, text=6, height=4, width=9, font=35,
#                  command=lambda: button_press(6))
# button6.grid(row=1, column=2)

# button7 = Button(frame, text=7, height=4, width=9, font=35,
#                  command=lambda: button_press(7))
# button7.grid(row=2, column=0)

# button8 = Button(frame, text=8, height=4, width=9, font=35,
#                  command=lambda: button_press(8))
# button8.grid(row=2, column=1)

# button9 = Button(frame, text=9, height=4, width=9, font=35,
#                  command=lambda: button_press(9))
# button9.grid(row=2, column=2)

# button0 = Button(frame, text=0, height=4, width=9, font=35,
#                  command=lambda: button_press(0))
# button0.grid(row=3, column=0)





# plus = Button(frame, text='+', height=4, width=9, font=35,
#                  command=lambda: button_press('+'))
# plus.grid(row=0, column=3)

# minus = Button(frame, text='-', height=4, width=9, font=35,
#                  command=lambda: button_press('-'))
# minus.grid(row=1, column=3)

# multiply = Button(frame, text='*', height=4, width=9, font=35,
#                  command=lambda: button_press('*'))
# multiply.grid(row=2, column=3)

# divide = Button(frame, text='/', height=4, width=9, font=35,
#                  command=lambda: button_press('/'))
# divide.grid(row=3, column=3)

# equal = Button(frame, text='=', height=4, width=9, font=35,
#                  command=equals)
# equal.grid(row=3, column=2)

# decimal = Button(frame, text='.', height=4, width=9, font=35,
#                  command=lambda: button_press('.'))
# decimal.grid(row=3, column=1)

# clear = Button(window, text='clear', height=4, width=12, font=35,
#                  command=clear)
# clear.pack()

# window.mainloop()



# # ************************************
# # Python Text Editor
# # ************************************
# import os
# from tkinter import *
# from tkinter import filedialog, colorchooser, font
# from tkinter.messagebox import *
# from tkinter.filedialog import *


# def change_color():
#     color = colorchooser.askcolor(title="pick a color...or else")
#     text_area.config(fg=color[1])


# def change_font(*args):
#     text_area.config(font=(font_name.get(), size_box.get()))


# def new_file():
#     window.title("Untitled")
#     text_area.delete(1.0, END)


# def open_file():
#     file = askopenfilename(defaultextension=".txt",
#                            file=[("All Files", "*.*"),
#                                  ("Text Documents", "*.txt")])

#     if file is None:
#         return

#     else:
#         try:
#             window.title(os.path.basename(file))
#             text_area.delete(1.0, END)

#             file = open(file, "r")

#             text_area.insert(1.0, file.read())

#         except Exception:
#             print("couldn't read file")

#         finally:
#             file.close()


# def save_file():
#     file = filedialog.asksaveasfilename(initialfile='unititled.txt',
#                                         defaultextension=".txt",
#                                         filetypes=[("All Files", "*.*"),
#                                                    ("Text Documents", "*.txt")])

#     if file is None:
#         return

#     else:
#         try:
#             window.title(os.path.basename(file))
#             file = open(file, "w")

#             file.write(text_area.get(1.0, END))

#         except Exception:
#             print("couldn't save file")

#         finally:
#             file.close()


# def cut():
#     text_area.event_generate("<<Cut>>")


# def copy():
#     text_area.event_generate("<<Copy>>")


# def paste():
#     text_area.event_generate("<<Paste>>")


# def about():
#     showinfo("About this program", "This is a program written by YOUUUUU!!!")


# def quit():
#     window.destroy()


# window = Tk()
# window.title("Text editor program")
# file = None

# window_width = 500
# window_height = 500
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# x = int((screen_width / 2) - (window_width / 2))
# y = int((screen_height / 2) - (window_height / 2))

# window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# font_name = StringVar(window)
# font_name.set("Arial")

# font_size = StringVar(window)
# font_size.set("25")

# text_area = Text(window, font=(font_name.get(), font_size.get()))

# scroll_bar = Scrollbar(text_area)
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)
# text_area.grid(sticky=N + E + S + W)
# scroll_bar.pack(side=RIGHT, fill=Y)
# text_area.config(yscrollcommand=scroll_bar.set)

# frame = Frame(window)
# frame.grid()

# color_button = Button(frame, text="color", command=change_color)
# color_button.grid(row=0, column=0)

# font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
# font_box.grid(row=0, column=1)

# size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
# size_box.grid(row=0, column=2)

# menu_bar = Menu(window)
# window.config(menu=menu_bar)

# file_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New", command=new_file)
# file_menu.add_command(label="Open", command=open_file)
# file_menu.add_command(label="Save", command=save_file)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=quit)

# edit_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Cut", command=cut)
# edit_menu.add_command(label="Copy", command=copy)
# edit_menu.add_command(label="Paste", command=paste)

# help_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Help", menu=help_menu)
# help_menu.add_command(label="About", command=about)

# window.mainloop()


# # Python Tic Tac Toe game
# # ******************************************************

# from tkinter import *
# import random

# def next_turn(row, column):

#     global player

#     if buttons[row][column]['text'] == "" and check_winner() is False:

#         if player == players[0]:

#             buttons[row][column]['text'] = player

#             if check_winner() is False:
#                 player = players[1]
#                 label.config(text=(players[1]+" turn"))

#             elif check_winner() is True:
#                 label.config(text=(players[0]+" wins"))

#             elif check_winner() == "Tie":
#                 label.config(text="Tie!")

#         else:

#             buttons[row][column]['text'] = player

#             if check_winner() is False:
#                 player = players[0]
#                 label.config(text=(players[0]+" turn"))

#             elif check_winner() is True:
#                 label.config(text=(players[1]+" wins"))

#             elif check_winner() == "Tie":
#                 label.config(text="Tie!")

# def check_winner():

#     for row in range(3):
#         if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
#             buttons[row][0].config(bg="green")
#             buttons[row][1].config(bg="green")
#             buttons[row][2].config(bg="green")
#             return True

#     for column in range(3):
#         if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
#             buttons[0][column].config(bg="green")
#             buttons[1][column].config(bg="green")
#             buttons[2][column].config(bg="green")
#             return True

#     if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
#         buttons[0][0].config(bg="green")
#         buttons[1][1].config(bg="green")
#         buttons[2][2].config(bg="green")
#         return True

#     elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
#         buttons[0][2].config(bg="green")
#         buttons[1][1].config(bg="green")
#         buttons[2][0].config(bg="green")
#         return True

#     elif empty_spaces() is False:

#         for row in range(3):
#             for column in range(3):
#                 buttons[row][column].config(bg="yellow")
#         return "Tie"

#     else:
#         return False


# def empty_spaces():

#     spaces = 9

#     for row in range(3):
#         for column in range(3):
#             if buttons[row][column]['text'] != "":
#                 spaces -= 1

#     if spaces == 0:
#         return False
#     else:
#         return True

# def new_game():

#     global player

#     player = random.choice(players)

#     label.config(text=player+" turn")

#     for row in range(3):
#         for column in range(3):
#             buttons[row][column].config(text="",bg="#F0F0F0")


# window = Tk()
# window.title("Tic-Tac-Toe")
# players = ["x","o"]
# player = random.choice(players)
# buttons = [[0,0,0],
#            [0,0,0],
#            [0,0,0]]

# label = Label(text=player + " turn", font=('consolas',40))
# label.pack(side="top")

# reset_button = Button(text="restart", font=('consolas',20), command=new_game)
# reset_button.pack(side="top")

# frame = Frame(window)
# frame.pack()

# for row in range(3):
#     for column in range(3):
#         buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
#                                       command= lambda row=row, column=column: next_turn(row,column))
#         buttons[row][column].grid(row=row,column=column)

# window.mainloop()



# Python Snake
# ************************************
from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")


window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()




































































































































