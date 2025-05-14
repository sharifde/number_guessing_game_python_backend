print("Hello, World!")  
if 5 > 2 : 
    print("print 5 is greater then 2")
    print("second  print")

# Verible in python   
x = 5

y = "Hello world"

print(type(x) , "" ,type(y))

# int float ,str   veriable are case sensitvie

# Python is no command for declaring the verible

# Global veriable in python

var_awesome = " awesome"

def  complment_fun():

    var_awesome = "Fantastic"
    print("python is" ,var_awesome)

    #Create a global veriable inside the the function and use it outside the project

    global my_global 
    my_global = " this is a global veriable  and i used out side the function"



complment_fun()

print(my_global)