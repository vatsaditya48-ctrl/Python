#A simple calculator in python IDLE (NON BODMAS) for chapter functions 
def divide(a,b,c):
        return(a/b/c)
def multiply(a,b,c):
        return(a*b*c)
def sub(a,b,c):
        return(a-b-c)
def add(a,b,c):
    return(a+b+c) #Defining the words add and multiply and giving what they would return
while True:

    choice= input("What Do You Want Me To Perform? (For multiplication type 'multiply' for division type 'div' for addition type 'add' and for subtraction type 'sub'") #Asking what to perform weather to add or multiply

    a= int(input("Enter The First Number:")) #getting inputs for calculations
    b= int(input("Enter the second numer:"))
    c= int(input("Enter The Third Number:"))    

    if choice== "multiply":
        result= multiply(a,b,c)
        print(f"The multiply of the numbers provided are:",result)

    elif choice== "add":
        result2=add(a,b,c)
        print(f"The addition of the numbers provided are:",result2)

    if choice== "sub":
            result3= sub(a,b,c)
            print(f"The Sub of the numbers provided are:",result3)

    if choice== "div":
            result4= divide(a,b,c)
            print(f"The division of the numbers provided are:",result4)#Results of the choice with respect to calcus


    again= input("Do you want to run again? (yes/no):") #Giving choice of loop or exit or termination of program

    if again=="no":
            print("Terminating program (╥﹏╥)")
            break
