# # # ***
# # # ***
# # # ***
# # # for i in range(3):
# # #     line=''
# # #     for j in range(3):
# # #         line += '*'
# # #     print(line)

# # *
# # **
# # ***
 
# for i in range(1,4):
#     # print("* "*i)    #can be only used in py

# #1.create a program for sum of numbers

# num=1234567
# sum=0

# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10
# print("sum of digits=",sum)

#2. Restorent Order System 
# Input Number of orders 
# Loop should ask : Food Name and price 
# Display total bill

# order=int(input("Enter the number of orders:"))

# totalbill=0

# for i in range(1,order+1):
#     food=input("Enter food name:")
#     price=float(input("Enter price:"))
#     totalbill=totalbill+price
# print("Total Bill:",totalbill)

# #3. ATM Retry System 
# Allow user maximum 3 attempts.
# Correct PIN:   1234 
# Display: Access Granded OR Card Blocked

# pin= 1234

# for i in range(3):
#     userpin=int(input("Enter your pin:"))
#     if userpin==1234:
#         print("access granted")
#         break
# else:
#      print("Card Block ")

# 5. a. Count digits in given number 
#    b. Reverse a given number

num=int(input("enter a num="))
temp=num
count=0
while temp>0:
    count=count+1
    temp=temp//10
print("length of num",count)

reverse= 0
temp=num
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10
print("reverse",reverse)