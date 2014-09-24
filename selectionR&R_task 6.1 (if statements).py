#Tavonga Mudzana
#24/09/14
#selection homework :task 5.1 (if statements)
age=int(input("please enter your age: "))
if age>=18:
        print("you are allowed to vote")
else:#prints the text below if the criteria is not met
        print("you are not allowed to vote")
        
retire_age=65-age

#subtracts the data entered from 65 to work out how many years until they can retire

print("age until you can retire: {0}years".format(retire_age))
        
        
        

