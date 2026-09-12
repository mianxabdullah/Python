def avg():
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    avg=(a+b)/2
    print("The Average Of Two Numbers Is: ",avg)
    print(f"The Average Of Two Numbers Is: {avg}")

def avg1(a,b):
    avg=(a+b)/2
    print("The Average Of Two Numbers Is: ",avg)
    print(f"The Average Of Two Numbers Is: {avg}")

def avg2(a,b):
    avg=(a+b)/2
    return avg
    

avg()  #call in main
print("Call with Arguments: ")
n=12
m=66
avg1(n,m)

print("Calling Return function: ")
ans=avg2(n,m)
print(f"The Average Of Two Numbers Is: {ans}")

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

print(f"Factorial of 5 is: {factorial(5)}")