# print('Hello')
# This is a test line
# print(2 + 2)

# a = None
# x = type(a)
# print(x)

# a = 10

# b = 20

# print(a + b)

# a = 'this is my bangladesh'

# b = 2025

# c =5

# print(a + str(b))

# print(b + c)

# a = input('Enter Your Age :')

# print('I Am ' + a + ' Years old')

# a = int(input('Enter A Number :'))
# b = input('Enter A Number :')

# print(a + int(b))

# x = type(a)

# print(x)

# '' "" ''' ''' """ """

# a = 'I love bangladesh'

# print(a[-10:1])

# x = a.upper()
# x = a.lower()
# x = a.capitalize() 
# x = a.title() 
# x = a.index('b')
# x = a.find('b')
# x = a.count('a')
# x = a.replace('bangladesh','India')
# print(a)
# # x = a.strip('-')


# print(len(a))
# # x = a.split()
# # print(x)
# y = "".join(a.split())
# print(y)
# print(len(y))

# print(a.swapcase())

# name = 'Rahim'

# age = 25

# subject = 'Python'

# a = 'Hi! I am {x}, I am {y} Years old, My subject is {z}'

# print(a.format(x = name,y = age,z = subject))



# Arithmatic Operators
# + - * / % ** //
# a = 350

# b = 20

# print(a % b)

# a = 44

# print(a % 2)

# print(8**4)

# print(97 // 2)

# Assugnment Operators
# = += -= *= /= %= **= //=  &= |= ^= >>= <<= :=
# a = 20
# a += 10 (a = a + 10)

# a = a + 10
# a -= 10
# print(a)

# Comparison Operators
# == != > < >= <=

# a = 10

# b = 10

# print(a <= b)

# Logical Operators
# and or not

# a = 10

# b = 20
# x = a > 15 or b < 5
# print(not(x))

# Identity Operators
# is is not
# a = 10
# b = 10

# print(a is not b)

# Membership Operator
# in not in

# a = "I Love Bangladesh"

# print("l" not in a)

# Bitwise Operators
# & | ^ ~ >> <<
#     8 4 2 1

# 0 = 0 0 0 0
# 1 = 0 0 0 1
# 2 = 0 0 1 0
# 3 = 0 0 1 1
# 4 = 0 1 0 0
# 5 = 0 1 0 1
# 6 = 0 1 1 0
# 7 = 0 1 1 1

# print(3 << 2)

# 0 1 1 0
# 0 0 1 1
# ---------
#   0 1 0 1

# x* (2**n)


# if else elif
# a = 10

# b = 10

# if a == b:
#     print("a is similler like b")
# else:
#     print('Not Found')


# a = int(input('Enter A Number :'))

# if a >= 0 and a <=100:
#     if a >= 80:
#         print("A+")
#     elif a >= 70:
#         print("A")
#     elif a >= 60:
#         print("A-")
#     elif a >= 50:
#         print("B")
#     elif a < 40:
#         print("Fail")
# else:
#     print('Invalid Number')

# Make a Calculator Using IF Else (Condition Only)



# While For

a = 0
# print(a <= 10)
# while a <= 10:
#     print(a)
#     if a == 5:        
#         break
#     a += 1 # a =  a + 1

# while a < 10:
#     a += 1
#     if a == 5:
#         continue
#     print(a)

# while True:
#     name = input('Enter Your Name :')
#     age  = input('Enter Your Age :')
#     subject = input('Enter Your Subject :')
#     print(f'Hello {name}, Your Age is {age}, Your Subject is {subject}')

#     is_continue = input('If You want to Continue Type Yes or No For Exit ').lower()

    # if is_continue == 'yes':
    #     pass
    # elif is_continue == 'no':
    #     break


# a = 'I Love Bangladesh'

# for i in a:
#     print(i)

# print(range(1,10))

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)

# while True:
#     number = int(input('Enter A Number :'))
#     for i in range(1,11):
#         print(f'{number} X {i} = {number*i}')
    
#     is_continue = input('If You want to Continue Type Yes or No For Exit ').lower()

#     if is_continue == 'yes':
#         pass
#     elif is_continue == 'no':
#         break

# a = 'America'

# print(f'I love {a}')

# a = 'I love Bangladesh'
# print(len(a))

# for i in range(17):
#     print(i,a[i])

# a = 'how are you'
# x = a.replace('o',"")
# print(x)

# List

# a = [34,'Bangladesh',12.34, True,None,34,34,34,34]
# a = 'I Love Bangladesh'
# print(a[1])
# print(a)
# a.append(45)
# a.insert(1,'India')
# x = a.index(None)
# print(a.count(34))
# print(x)
# a.pop(0)
# a.remove(True)
# a.clear()
# b = a.copy()
# b.reverse()
# print(b)

# a = [34,45,56]
# b = [57,58,59]

# a.extend(b)
# print(b)

# a = [34,2,6,8,23,12]

# a.sort()
# print(a)

# a = [34,2,6,8,23,12]

# for i in a:
#     print(i)

# x = []

# a = 'I Love Bangladesh'

# for i in range(len(a)):
#     if a[i] == 'a':
#         x.append(i)

# print(x)

# x = []

# x.append('Bangladesh')
# x.append('India')
# x.append('Pakisthan')
# x.append('Nepal')

# print(x)

# a = (34,45,56,67,'Bangladesh',45)

# print(a.index(34))
# print(a.count(45))
# x = list(a)
# x.append('India')
# a = tuple(x)
# print(a)
# print(x)
# y = []
# for i in a:
#     # print(type(i))
#    if isinstance(i, str):
#       y.append(i)
# print(y)

# for i in range(1,3):
#     for j in range(97,100):
#         print(f'{i}.{chr(j)}')

# a = (2,3,4,5,[67,68,69])
# a[4].append(70)
# print(a)

# a = {'name': 'Rahim','age':34}
# b = a.copy()
# print(a['age'])

# print(a.keys())
# print(a.values())
# b.update({'subject':'Python'})
# b.pop('age')
# b.popitem()
# b.clear()
# b.update({'name':'Karim'})
# x = b.get('age')
# print(x)

# x = b.items()
# print(x)

# a = {34,45,56,67,'Bangladesh',45}
# b = {2,3,'Bangladesh',45}

# print(type(a))
# a.add('India')
# b = a.copy()
# a.clear()
# a.discard('Bangladesh')
# a.pop()
# a.remove('Bangladesh')
# b = {2,4,5}
# a.update(b)
# x = a.intersection(b)
# x = a.difference(b)
# x = a.union(b)
# print(x)

# def rahim():
#     print('I Love Bangladesh')

# rahim()

# def rahim(a,b):
#     print(a + b)

# rahim(5,7)

# def rahim(a,b):
#     return a + b
#     # print(a + b)
# x = rahim(5,7)

# print(x+10)

# print(rahim(5,7)+ 10)


# def my_func(*a):
#     total = 0
#     for i in a:
#         total += i
#     return total

# x = my_func(34,56,12,34)

# print(x)

# x = []
# while True:
#     num = input('Enter A Number :')
#     if num == 'q':
#         break
#     else:
#         x.append(int(num))
#         print(x)

# print(my_func(*x))


# while True:
#     num = int(input('Enter A Number : '))
#     if num == 0:
#         break
#     else:
#         for i in range(1,11):
#             print(f'{num} X {i} = {num*i}')

# x = []
# while True:
#     num = int(input('Enter A Number : '))
#     if num == 0:
#         break
#     else:
#         x.append(num)

# print(x)
        
# rahim = lambda a,b: a + b

# print(rahim(5,7))
# def rahim(a):
#     return(a + 10)

# print(rahim(5))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))

# 5 * 4 * 3 * 2 * 1 

# a = 'Hello'

# def rahim(a):
#     if len(a) == 0:
#         return a
#     else:
#         return rahim(a[1:]) + a[0]

# print(rahim('Hello'))

# def countdown(a):
#     if a == 0:
#         print('Stop')
#     else:
#         print(a)
#         countdown(a-1)

# countdown(5)

# a = open('E:/Universal IT/Batch - 113/my_text_file.txt','a')
# a.write('I Love America.')
# a = open('E:/Universal IT/Batch - 113/my_text_file.txt','r')
# print(a.read())
# a.close()

# try:
#     a = int(input('Enter A Number :'))
#     for i in range(1,11):
#         print(f'{a} X {i} = {a * i}')
# except Exception as e:
#     print(e)
#     # print('Invalid Input!')

# b = 'I Love Bangladesh'
# print(b)
# print(len(b))
# print(b.upper())
# print(b.lower())

# try:
#     a = open('E:/Universal IT/Batch - 113/my_text_file.txt','w')
#     a.write('Bangladesh is our Brother land.')
#     try:
#         a = open('E:/Universal IT/Batch - 113/my_text_file.tx','a')
#         a.write('Bangladesh is our Sister land.')
#         a = open('E:/Universal IT/Batch - 113/my_text_file.txt','r')
#         print(a.read())
#     except:
#         print('Something went wrong.')
#     finally:
#         a.close()
# except Exception as e:
#     print(e)

# import main, my_module

# print(my_module.c)

# def myfun(x,y):
#     return x + y

# a = my_module.a
# b = my_module.b

# print(myfun(a,b))

# print(main.name)
# print(my_module.name)

# from datetime import datetime, timezone
# from zoneinfo import ZoneInfo

# a = datetime.datetime.now()
# print(a.strftime('%z'))
# utc_now = datetime.now(timezone.utc)
# x = datetime.now(ZoneInfo("America/Los_Angeles "))

# print(x)

# import os

# os.mkdir('New_113')
# os.remove('my_text_file.tx')
# x = os.getcwd()
# y = os.listdir(x)
# print(y)

# import turtle

# screen = turtle.Screen()
# screen.title('My Turtle')
# # screen.bgcolor('lightblue')

# my_turtle = turtle.Turtle()
# my_turtle.color('green')
# my_turtle.pensize(9)
# my_turtle.speed(3)

# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)

# for _ in range(5):
#     my_turtle.forward(100)
#     my_turtle.left(144)

# for _ in range(36):
#     for _ in range(2):
#         my_turtle.circle(100,60)
#         my_turtle.left(120)
#     my_turtle.left(10)

# my_turtle.hideturtle()

# turtle.done()

# from my_package import main,my_module

# print(my_module.name)

print('Hello')