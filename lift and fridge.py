#Tavonga Mudzana
#22/09/14
#exercise 6.5

print("hello please enter the dimensions of the fridge and the lift")

fridge_length=float(input("please enter the length of the fridge: "))
fridge_width=float(input("please enter the width of the fridge: "))
fridge_depth=float(input("please enter the depth of the fridge: "))
fridge_area=(fridge_length*fridge_width)*fridge_depth
print("area for the fridge: {0}".format(fridge_area))
#this asks the user to input the dimensions of the fridge and prints the the area

lift_length=float(input("please enter the length of lift: "))
lift_width=float(input("please enter the width of the lift: "))
lift_depth=float(input("please enter the depth of the lift: "))
#this asks the user the dimensions of the lift 
lift_area=(lift_length*lift_width)*lift_depth

print("area for the lift: {0}".format(lift_area))
print("area for fridge: {0}".format(fridge_area))
#prints the area for the fridge and the lift
answer=fridge_area-lift_area

print("{0}-{1}".format(lift_area,fridge_area))
print("answer:{0}".format(answer))
#prints the 2 areas and then print the answers below


