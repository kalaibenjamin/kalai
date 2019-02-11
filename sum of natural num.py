number = int(input("Enter the value of n:"))
n = number
sum = 0
if number <= 0: 
   print("Enter a whole positive number") 
else: 
   while number > 0:
      sum = sum + number;
      number = number- 1; 
print("Sum of first", n,"natural numbers is:",sum)
