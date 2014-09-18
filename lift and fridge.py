#Tavonga Mudzana
#....
#exercise 6.5

print("hello please enter the dimensions of the fridge and the lift")

length1=float(input("please enter the length of the fridge: "))
width1=float(input("please enter the width of the fridge: "))
depth1=float(input("please enter the depth of the fridge: "))
area1=(length1*length1)*depth1
print("area for the fridge: {0}".format(area1))
#this asks the user to input the dimensions of the fridge
length2=float(input("please enter the length of lift: "))
width2=float(input("please enter the width of the lift: "))
depth2=float(input("please enter the depth of the lift: "))

area2=(length2*length2)*depth2
print("area for the lift {0}".format(area2))

print(area1)
print(area2)

answer=area2-area1

print("{0}-{1}".format(area2,area1))
print("answer:{0}".format(answer))



