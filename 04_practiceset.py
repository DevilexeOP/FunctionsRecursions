# Write a program using function to find the greatest of 3 numbers
def max(num1, num2, num3):
    if(num1 > num2):
        if(num1 > num3):
            return num1
        else:
            return num3
    else:
        if(num2 > num3):
            return num2
        else:
            return num3
x = max(33, 868, 3134)
print("The value of the max is\n" + str(x))

# Write a python program using function to convert celsius to ferhanite
def far(cel):
    return(cel*(9/5)) + 32
c = 45
f = far(c)
print("Fahrenite temp is ", str(f))

# How do u prevent a python print()function to print a new line at the end
print("Hi", end=" ")
print("hello", end=" ")

# Write a recursive function to calculate the sum of first n natural numbers
n = int((input("Enter the number\n")))
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
x = sum(n)
print(x)

''' 
***
**
* n=3
'''
n = 6
for i in range(6):
    print("*" * (n-i))  # Prints * n-i times (eg)6-5=5 times

# write a program to convert inch in cms
inch_value = int(input('Enter the value in inch: '))
cm_value = 2.54 * inch_value

print('{}″ = {}cm'.format(inch_value, cm_value))
def inch_to_cm(inch):
    return inch * 2.54
inch_value = int(input('Enter value in inch:'))
print('{}" == {}cm'.format(inch_value, inch_to_cm(inch_value)))

# Write a python function to remove the given word from a string and strip at the same time
def remove_split(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()
this = "   OK is OK  "
n = remove_split(this,"Ok")
print(n)

# Write a program to print tthe multiplication table of a given number
n = int(input("Enter the number\n"))
def multiply(n):
    return(f"{n}x{i}={n*i}")
for i in range(1,11):
    print(multiply(n))