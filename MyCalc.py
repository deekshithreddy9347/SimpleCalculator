#simple calculator with Basic arithematic operations
#performs operations like Addition,subtraction,multiplication,division etc...
print("Simple calculator with Basic Arithematic operations")
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mull(num1,num2):
    return num1*num2

def div(num1,num2):
    if (num2==0):
        print("Cannot divide by zero!")
    else:
        return num1/num2


while True:
    num1=int(input("Enter First number:"))#inputing two numbers to perform arthematic operations
    num2=int(input("Enter Second number:"))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    number=int(input("enter operation number:"))
    if(number==1):
        result=add(num1,num2)
    elif(number==2):
        result=sub(num1,num2)
    elif(number==3):
        result=mull(num1,num2)
    elif(number==4):
        result=div(num1,num2)
    else:
        print("Invalid Operation")
        break
    print("The Result of two numbers are:",result)
    
    
    
       



















 
 
 
 
 
 
 
 
 
 
 
 
 
 