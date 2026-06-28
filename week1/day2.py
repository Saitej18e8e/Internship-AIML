# # # # age=20; nationality="Indian"

# # # # if(age>=18 and nationality=="Indian"):
# # # #      print("Allowed for Driving Liences")
# # # # else:
# # # #      print("Not allowed")


# # # mark=int(input("Enter marks"));
# # # if mark >=0  and mark <= 100:
# # #     if(mark<40):
# # #         print("Student is Failed")

# # #     elif(mark >40 and mark<60):
# # #         print("pass c")

# # #     elif(mark>60 and mark<75):
# # #         print("second class B")

# # #     else:
# # #         print("First class A")

# # # else:
# # #     print("invalid")

# # # even odd


# # # a=int(input("Enter a number to validated:"))


# # # if(a%2==0):
# # #     print("number is Even")
# # # else:
# # #     print("number is Odd ")


# # # largest number

# # # a=int(input("Enter a number a:"))
# # # b=int(input("Enter a number b:"))

# # # if(a>b):
# # #     print("The number a is largest")
# # # else:
# # #     print("The number b is largest")


# # # login 



# # # a=input("username:")
# # # b=input("password:")

# # # if(a=="admin" and b=="admin@123"):
# # #     print("logged in successfully")

# # # else:
# # #     print("incorrect credentials")


# # # divisibilty by 5

# # # a=int(input("enter a number to be check"))

# # # if(a%5==0):
# # #     print("number is divisible by 5")
# # # else:
# # #     print("number isnt divisible by 5")


# # # # leap year

# # # a=int(input("Enter the year:"))

# # # if(a%4==0) and (a%100!=0):
# # #     print("year is leap ")
# # # else:
# # #     print("year isnt leap ")


# # # 6 pizza type
# # choice=int(input("Enter pizza type(1 or 2)"))
# # qty=int(input("Enter quantity:"))

# # if choice ==1:
# #     price=200
# #     print("veg pizza")
# # elif choice==2:
# #     price=500
# #     print("Nonveg pizza")
# # else:
# #     print("invalid pizza type")
# #     exit()

# # totalbill=price*qty

# # if qty>5:
# #     discount=totalbill*0.10
# # else:
# #     discount=0

# # finalbill=totalbill-discount

# # print("Total bill=",totalbill)
# # print("Discount=",discount)
# # print("Final bill=",finalbill)

# #  8. Movie Ticket pricing by age 

# age = int(input("Enter your age: "))

# if age < 12:
#     price = 100
# elif age <= 59:
#     price = 200
# else:
#     price = 150

# print("Ticket Price = ", price)

# 10 food delivery app

order = float(input("Enter Order Amount: "))
member = input("Are you a member? (yes/no): ")

if member == "yes" and order > 1000:
    discount = order * 0.20

elif member == "yes" and order > 500:
    discount = order * 0.10

elif member == "no" and order > 2000:
    discount = order * 0.05

else:
    discount = 0

final_amount = order - discount

print("Order Amount =", order)
print("Discount =", discount)
print("Final Amount =", final_amount)