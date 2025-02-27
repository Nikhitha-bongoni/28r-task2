	# Print all numbers from 1 to 100 using a  for  loop. 
for i in range(1,101):
    print(i)

# Write a program to print the sum of the first  n  natural  numbers. (n*n+1/ 2) 
num=int(input("enter natural numbers:"))
sum=0
for i in range(1,num+1):
    print(i)
    sum +=i
print(sum)
# Print all even numbers between 1 and 50 using a  while  loop. 
i= 2
while i <= 50:
	print(i)
	i+= 2
# Write a program to display the multiplication table of a given  number. First 20 
n=int(input("enter the number:"))
for i in range(1,21):
	print(n,"*",i,"=",n*i)


# Reverse a number using a  while  loop. Also can we get the sum of all the digits.
   num=12473   
dig_sum=0
rev_num=0
while  num>0:
    rem=num%10
    dig_sum+=rem
    rev_num=rev_num*10+rem
    num=num//10
print(dig_sum)
print(rev_num)

#  Write a program to count the number of digits in a given  number using a  while  loop. 
num=int(input("enter a number:"))
count=0
if num==0:
	count=1
else:
	while num>0:
		num=num//10
		count+=1
print(count)
  

# Write a program that keeps asking the user to enter numbers  until they enter a negative number. Use a  while  loop. 
while True:
	n=int(input("enter a number:"))
	if n<0:
		break
	print(n)


# Medium Questions
# '''Print the first 10 terms of the Fibonacci series using a for loop.'''

n=10
a=0
b=1
for i in range(0,n+1):
    print(a)
    c=a+b
    a=b
    b=c


# '''Check if a given number is a prime number using a for
    #   loop.'''

n=int(input("Enter the number :"))
count=0
for i in range(2,n):
    if n%i==0:
        count+=1
if count==0:
    print(n, 'is prime')
else:
    print(n,'is not prime')


# '''Write a program to calculate the factorial of a number using a while loop.'''

n=int(input("Enter the number :"))
while n>0:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    break
print(fact)

# '''Implement a menu-driven program where the user can
    #   choose to:
    #       1. Find the square of a number.
    #       2. Find the cube of a number.
    #       3. Exit.'''

n=int(input('Enter a number :'))
if n==1:
    n=int(input('Enter a number :'))
    print(n**2)
elif n==2:
    n=int(input('Enter a number :'))
    print(n**3)
elif n==3:
    print('Exit')
else:
    print('enter number between 1 to 3')

# '''Implement a basic login system where the user has three attempts to enter the correct password using a loop.'''

attempts=3
password='123456'
while attempts>0:
    password=int(input('Enter a password'))
    if password == 123456:
        print('login sucessfull')
        break
    else:
        attempts-=1
        print(f'{attempts} attempts available')






    
    








