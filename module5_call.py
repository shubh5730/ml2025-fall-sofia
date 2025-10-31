"""
Main program that uses the NumberCollection class from module5_mod.py
"""

from module5_mod import NumberCollection

def main():
    # Ask user for N
    N = int(input("Enter a positive integer N: "))

    # Initialize the collection
    collection = NumberCollection(capacity=N)

    # Ask user to enter N numbers
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        collection.insert_number(num)

    # Ask for X
    X = int(input("Enter integer X: "))

    # Search for X
    result = collection.find_number(X)

    # Print result
    print(result)

if __name__ == "__main__":
    main()
