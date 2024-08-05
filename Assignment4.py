# 1.     Function without Parameters:
# answer
#function without parameter means that no argument is pass within the brackets along with functionname
def my_function():   #my_function() have no parameters
  print("Hello from a function")

my_function()

# 2.      Function with Parameter:
# answer
#function with parameters means some argument is pass along with functionname
def my_function(fname): #my_function have a fname argument in their parameter
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# 3.      Function with Default Parameter:
# answer
#default value in function are used for such an argument if no value is passed to it and if value passed than argument is overriden
def showinfo( name, city = "Hyderabad" ): #city is a default value 
   print ("Name:", name)
   print ("City:", city)
   return

showinfo(name = "Ansh", city = "Delhi")
showinfo(name = "Shrey")

# 4.      Function with Return Keyword:
# answer
def add(a, b):

    # returning sum of a and b
    return a + b

# calling function
res = add(2, 3)
print("Result of add function is {}".format(res))

# 5.      Recursion:
# answer
#Recursion is a process in which a function calls itself directly or indirectly. 

# a) WAP to print factorial value of a given number using recursion
# answer
def factorial(n): 
     
    if (n==1 or n==0):
         
        return 1
     
    else:
         
        return (n * factorial(n - 1)) 
 
#example 
num = 5; 
print("number : ",num)
print("Factorial : ",factorial(num))


#  b) WAP to display Fibonacci series up to 10 iteration using recursion.
# answer
def recursive_fibonacci(n):
    if n <= 1:
	    return n
    else:
	    return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

# check if the number of terms is valid
if n_terms <= 0:
 print("Invalid input !")
else:
 print("Fibonacci series:")
for i in range(n_terms):
	      print(recursive_fibonacci(i))
