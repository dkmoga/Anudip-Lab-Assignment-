
# 1.Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
# answer
x=int(input("Enter the number:"))

def checknumber(x):
    if x % 2 == 0:
     print(x,"Is Even Number")
    else:
      print(x, "Is Odd Number")

checknumber(x)     

# 2.Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
# answer
x=int(input("Enter the age:"))

def eligiblevoter(x):
    if x>=18:
     print("Person is allowed to vote")
    else:
      print( "Person is not allowed to vote")

eligiblevoter(x)

# 3.Write a Python program that determines if a given year is a leap year or not.
# answer
year_to_check = 2018
def is_leap_year(year):
	return any([(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)])


result_list = is_leap_year(year_to_check)
print(f"{year_to_check} is a leap year: {result_list}")


# 4.Create a Python program that checks if a user-given number is positive, negative, or zero.
# answer

def check(n):
	
	# if the number is positive
	if n > 0:
		print("Positive")
		
	# if the number is negative
	elif n < 0:
		print("Negative")
		
	# if the number is equal to
	# zero
	else:
		print("Equal to zero")
		
#example
check(5)
check(0)
check(-5)


# 5.Write a Python program that determines the largest of three numbers entered by the user.
# answer
# Python program to find the largest 
# number among the three numbers 

def maximum(a, b, c): 

    if (a >= b) and (a >= c): 
        largest = a 

    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
        
    return largest 


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
print(maximum(a, b, c)) 
