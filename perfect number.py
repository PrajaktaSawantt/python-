# defining a function for perfect number
def perfect_number(n):
sum = 0
for x in range(1, n):
if n % x == 0:
sum += x
# returning the sum of the factor of the number
return sum
# taking the number as an input from the user
num =int(input("Enter the number : "))
# checking whether the number is perfectr number or not
if(perfect_number(num) == num):
print("Number is a perfect number")
else:
print("NUmber is not a perfect number")
