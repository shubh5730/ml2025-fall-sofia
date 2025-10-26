# module4.py

#User Input : Asking to positive integer N
N = int(input("Enter a positive integer N: "))

# Read N numbers and ask user again to provide numbers from 1 to N
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Ask the user for random X number
X = int(input("Enter integer X: "))

# Check for if X is among the entered numbers or not
if X in numbers:
    # Output the index (1-based)
    print(numbers.index(X) + 1)
else:
    # Output -1 if not found
    print(-1)
