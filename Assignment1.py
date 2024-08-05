# Q.1 print helloworld
#answer

print("Hello world")


# Q.2 describe local variable and global variable code
#answer

#global variable 
x="Global variable"

def f():
	
	# local variable
	s = "local variable"
	print(s)
	#local variable runs perfectly within the block
	print(x)
	#it also run perfectly due to x is a global variable
f()
print(x)

print(s)
#it cause error because s is the local variable it can be access only within the block



# Q.3 Write a code that describe Indentation error
#answer

for i in range(1,11):
	print(i)

for i in range(1,11):
print(i) #it will cause indentation error                 

# Q.4 write a code that describe local and global variable with same name
#answer

#global variable 
s=12
def f():
	#local variable
	s=16
	print("Inside Function:", s)

f()
print("Outside Function:",s)

# Q.5 Write a code for string, int and float input.

studentclass=int(input("Enter the class:")) #integer input
studentmarks=float(input("Enter the marks:")) #float input
studentname=input("Enter your name:") #string input

print("The name is:",studentname)
print("The class is:",studentclass)
print("The marks is:",studentmarks)