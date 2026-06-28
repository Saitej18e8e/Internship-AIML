# function

# def additionof2(n1,n2):
#     print(n1+n2)

# additionof2(5,6)


# create function for CalculateBill price and quantity

# def CalculateBill(price,quantity):
#     return price*quantity

# billamt=CalculateBill(1000,2)
# print("for 2 product whose price is 1000 :",billamt)

# def logincheck(username,password):
#     if(username== 'saitej' and password== 'Saitej@67'):
#         print("login successfull")
    
#     else:
#         print("Incorrect username or password")

# logincheck("saitej","Saitej@67") #function calling

    
# def largest(a,b,c):
#     if(a>b and a>c):
#         print("largest is",a)
#     elif(a>b and a<c):
#         print("largest is",c)
#     else:
#         print("largest is",b)

# largest(10,66,49)

# def largest(a, b, c):
#     if a > b and a > c:
#         return ( a)
#     elif b > a and b > c:
#         return ( b)
#     else:
#         return ( c)

# print(largest(10, 66, 49))   #return is better than print cause we can call it again or use it ahead


# def discount(a):
#     if(a>10000):
#         return a- a*0.40
#     elif(a>5000):
#         return a- a*0.20
#     else:
#         return a
    

# print(discount(12000))
# print(discount(7000))
# print(discount(3000))
    

# def getoffer(recharge,month):
#     if(recharge>7000 and month == 12 ):
#         return "congrast u got Free Netflix"   
#     elif(recharge>1000 and month == 3):
#         return "congrast u got free Extra 5GB " 
#     else:
#         return"No offer 4 u :)"   
    
# print(getoffer(10000,12))



#--------File handling---------


# file =open("data.txt","w")
# file.write("HEllo b91")
# file.close()

# file1=open("data.txt","r")
# content = file1.read()
# print(content)
# file1.close()

# file2= open("data.txt","a")
# file2.write("\nThis is last line")
# file2.close()

# with open("data.txt","r") as file3:
#     print(file3.read())

# note=input("Enter note:")
# with open("myNotes.txt","a")as file4:
#     file4.write(note "\n")