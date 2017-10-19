# message = "hello world"
# print(message.lower())
# print(message.count("l"))
# print(message.find("ello"))
# new_message = message.replace("world", "universe")
# print(new_message)
# ##concat
# super_message = message + " " + new_message.upper()
# print(super_message)
#

##Scientific Notation Parser##
# from decimal import Decimal
# import random
#
# intro = input("print something here")
#
# def parser(outro):
#
#     if "e" in outro:
#         newoutro = float(outro)
#         nnewoutro = format(newoutro, '.2f')
#
#         return nnewoutro
#
#     else:
#         choice = input("do you want your answer in scientific notation? (y/n)")
#         if choice == 'y':
#             yesschoice = float(outro)
#             yeschoice = Decimal(yesschoice)
#             return format(yeschoice, '.2e')
#         else:
#             return outro
#
#
# print(parser(intro))

##Hexadecimal Parser##

# def hex_converter(somestring):
#
# 	for i in range(0, len(somestring), 2):
# 		complete = chr(int(somestring[i:i+2],16))
# 		complete = ''.join(complete)
#
# 	return complete

#print(hex_converter("437c2123"))
# #################################--LISTS, SETS, TUPLES, Dictionaries--##########################
# courses = ["history", "math", 'physics', 'compSci']
# courses_2 = ['art', 'education']
#
# courses.insert(0, "super")
# courses.append("superman")
# courses.extend(courses_2)   #add a list to another list
# print(courses)
#
# courses.remove("math")
# courses.pop()  # works like a stack so pops last element
# courses.sort(reverse=True)  # reverse sorting
# print(courses)
#
# courses_str = '- '.join(courses)    #DAMN useful to split lists
# new_list = courses_str.split("-")
# print(courses_str)
# print(new_list)
#
# #index, sum, enumerate (similar to index)
#
# ##sets don't have repeats or order
# courses_3 = {"history", "math", 'physics', 'CompSci', 'compSci'}
# courses_4 = {'history', 'math'}
# print(courses_3)
#
# print(courses_3.difference(courses_4)) # difference in elements in the lists
# print(courses_4.intersection(courses_3))
# print(courses_4.union(courses_3))
#
# ##dictionaries <key,value>
#
# student = {"name":'John', 'age':25, 'courses':['math', 'compsci']}
# print(student.get('name'))  #could also just use square brackets with key
# student['phone'] = '555-5555'
# student['name'] = 'jane'
# #update dictionary
# student.update({'name':'henry'})
# print(student)
#
# for i,j in student.values():
#     print(i)
#
# for i, j in student.items():
#     print(i,j)

################################--NUMBERS--########################################
# num = 3.14
# print(type(num))
# print(int(num))
# print(3//2) #floor

#################################--FUNCTIONS--#####################################

# def testingstuff(*args, **kwargs):
#     print(*args)
#     print(*kwargs)
#
# tester1 = ['house', 'mouse', 'goose']
# tester2 = {'little':12, "goose": "funny"}
#
# testingstuff(tester1, tester2)

# ################################--CLASSES--######################################
# total =10
#
# def multiple(num1, num2):
#     total= num1*num2
#     return total
# print(multiple(5,10))
# print(total)
#
# total = total + multiple(5,10)
# print(total)
# print(bool(6<3))
#
# arr = ["tiger", "baby", "lady"]
# print(arr)
#
#
# age = input("what is your age")
#
# print(age)
# if(age>"b"):
#     print("ok")
#
# age1 = [11,12,13,18,20]
# print (sum(age1,2))
# """
#
#
# class Students:
#
#     def __init__(self, name, age, fav):
#         self.name = name
#         self.age = age
#         self.fav = fav
#
#     def displayStudent(self):
#         return ("The Students name is " + self.fav)
#
#
# student1 = Students("Srikanth", 25,"11")
# student2 = Students("Raja", 25,"19")
# student3 = Students ("Sindhu", 19,30)
#
# print(student1.displayStudent())
# print(student2.displayStudent())
#
# print(hasattr(student1, "age"))
# setattr(student1, 'gender', "male")
# print(hasattr(student1, "gender"))
# print(hasattr(student2, "gender"))
#
# print(student1.gender)
#
#
#
#

#############################--INHERITANCE--#######################################
# class Parent:
#
#         counter =10
#         def __init__(self):
#
#             print("class initialized")
#
#         def parentFunc(self):
#             print("parentFunc being called")
#
#         def setCounter(self, count):
#             Parent.counter = count
#
#         def showCounter(self):
#             print(str(Parent.counter))
#
#
# class Child(Parent):
#     # def __init__(self):
#     #     print("child class being initialized")
#
#     def childFunc(self):
#         print("childfunc being called")
#
#     def parentFunc(self):
#             print("parentFunc being called2")
#
#
# class AnotherChild(Child):
#     # def __init__(self):
#     #     print("anotherchild class being initialized")
#
#     def anotherChildFunction(self):
#         print("anotherchildfunc being called")
#
#
# c = Child()
# c.childFunc()
# c.parentFunc()
# d = AnotherChild()
# d.parentFunc()

#################################--FILES--######################################

# file1 = open("/Users/Srikanth/Desktop/testfile.txt","r")
# firstline = file1.readline()
# print(firstline)
# file1.close()
# f = open("/Users/Srikanth/Desktop/testfile.txt", "a") #append to the fild
# f.write("checking a new addition to the file")
# f.close()
# f = open("/Users/Srikanth/Desktop/testfile.txt", "r")
# print(f.read())
# f.seek(0,0) #reset the cursor to beginning
# print(f.read())

######################--FILES CONTINUED--################################

# with open('/Users/Srikanth/Desktop/testfile.txt', 'r') as f:
#     # for line in f:
#     #     print(line, end='')
#     f_contents = f.read(10)
#     while len(f_contents) >0:
#         print(f_contents, end='')
#         f_contents = f.read(10)
#
#
# with open('/Users/Srikanth/Desktop/testfile.txt', 'r') as fd:
#     with open("testfile2.txt", "w") as fs:
#         fs.write(fd.read())
#
# finaltext = open("testfile2.txt", 'r')
# for line in finaltext:
#     print(line, end="")

#########################--****MODULES*****--########################################

##Random
# import random
#
# computerrandom = random.randint(0,100)
# print(computerrandom)
# gues = input("Enter your guess number")
# guess = int(gues)
#
# if guess == computerrandom:
#         print("you guessed correctly -- congrate mate")
#
#
# while guess!=computerrandom:
#
#     if guess > computerrandom:
#         print("your guess is too high")
#         gues = input("Enter your guess number")
#         guess = int(gues)
#
#     elif guess < computerrandom:
#         print("your guess is too low")
#         gues = input("Enter your guess number")
#         guess = int(gues)
#
# if guess == computerrandom:
#     print("you guessed correctly -- congrats mate")

## RE module
# import re
#
# somestring = "The night was cold and dark"
# print(somestring[3:])
# print(re.search("night", somestring))
# m = re.search("night", somestring)
# start=m.start()
# end = m.end()
# print(somestring[start:end])

#############################--RANDOM CONTINUED--#################################
# import random
# food = ["raviolli", "pasta", "pizza", "cheesecake"]
#
# print(random.choice(food)) #random choice in the array
#
# print(random.shuffle(food))  #shuffle the array
# print(food)

###########################--System--#################################
# import sys
#
# inputstatement = sys.stdin.readline(10)  #input basically
# outstatement = sys.stdout.write("we are the coolest man") #basically print
#
# print(inputstatement)
# print(outstatement)


##########COOL THINGS WITH TIME

# import time
# print (time.time())
#
# def numbers(max):
#     time1=time.time()
#     for i in range (0, max):
#         print(i)
#     time2=time.time()
#     print(str(time2-time1) + " seconds")
#
# numbers(20)

############################--Beautiful Soup--#############################
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<html> <p> asadadafasdf <strong> Hello <a> Hello </html>", "html.parser")
# print(soup)
# print(soup.prettify())

#########################--INTRO TO GUI--####################################

# import turtle
#
# t=turtle.Pen()
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.reset()
#
#
# #octagon
#
# for i in range (0,8):
#     t.forward(50)
#     t.left(45)

