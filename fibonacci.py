#! /bin/python3.8

# Python programm for counting Fibonacci sequence  Fn =  F(n-1) + F(n-2)
# n is number of terms in Fibonacci sequence
print ("Hi, this is python programm for counting Fibonacci sequence  Fn =  F(n-1) + F(n-2)")
n=int(input("Please enter the number of terms in Fibonacci sequence (n):"))
number_of_terms=n

# we are making new empty array
array=[]

# adding "0" to array, to show it in final print
array.append(0)

# F0 = a = 0 -> this is the first number of Fibonacci sequence
# F1 = b = 1 -> this is the second number of Fibonacci sequence

a=0
b=1

while n!=0:
    a=a+b
    b=a-b
    n=n-1
    # we are adding numbers to array
    array.append(a)

print("If number of terms =", number_of_terms, "-> Fibonacci sequence number equals to", a)

# print() -> empty row
print()
print("The whole sequence is:", array)
