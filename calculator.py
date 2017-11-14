def add(x,y):
	return x+y

def sub(x,y):
	return x-y
	
def mul(x,y):
	return x*y
	
def div(x,y):
	return x/y

print("Select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice= input("Enter choice:(1/2/3/4):")
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
#print (type(choice) is int)
#print choice 
if choice == 1:
	#print num1
	#print(num1,"+",num2,"=")
	#res=add(num1,num2)
	#print res 
	print add(num1,num2)
elif choice == 2:
	print(num1,"-",num2,"=",sub(num1,num2))
elif choice == 3:
	print(num1,"*",num2,"=",mul(num1,num2))
elif choice == 4:
	print(num1,"/",num2,"=",div(num1,num2))

	
