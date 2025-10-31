
class NumberCollection:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.numbers = []

    def insert_number(self, num: int):
        self.numbers.append(num)

    def find_number(self, x: int) -> int:
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1


def main():
    # Ask for N
    N = int(input("Enter a positive integer N: "))

    # Create collection
    collection = NumberCollection(capacity=N)

    # Read N numbers
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        collection.insert_number(num)

    # Ask for X
    X = int(input("Enter integer X: "))

    # Search and print result
    print(collection.find_number(X))


if __name__ == "__main__":
    main()
