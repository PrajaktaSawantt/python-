# taking the lower and upper limit for displaying the armstrong number
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
# checking the number from 1 to 5000 and displaying the armstrong number
print("All the natural number between 1 to 5000 : ")
for num in range(lower,upper + 1):
sum = 0
temp = num
while temp > 0:
digit = temp % 10
sum += digit ** 3
temp //= 10
if num == sum:
print(num) 
