import numpy as np

class KNNRegressor:
    #Simple k-NN regression model using NumPy arrays

    def __init__(self):
        self.X = np.array([], dtype=float)
        self.Y = np.array([], dtype=float)

    def insert_point(self, x: float, y: float):
        #Insert a new (x, y) point into the dataset
        self.X = np.append(self.X, x)
        self.Y = np.append(self.Y, y)

    def predict(self, x_input: float, k: int):
        #Perform k-NN regression: predict Y for given X
        n = len(self.X)
        if k > n:
            return f"Error: k ({k}) cannot be greater than N ({n})"

        # Compute Euclidean distances
        distances = np.abs(self.X - x_input)

        # Get indices of k nearest neighbors
        nearest_indices = np.argsort(distances)[:k]

        # Compute mean Y value of those k neighbors
        predicted_y = np.mean(self.Y[nearest_indices])

        return predicted_y


def main():

    #Reading N (positive integer)
    N = int(input("Enter N (number of data points): "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    #Reading k (positive integer)
    k = int(input("Enter k (number of neighbors): "))
    if k <= 0:
        print("Error: k must be a positive integer.")
        return

    # Initialize model
    model = KNNRegressor()

    #Reading N points
    for i in range(N):
        x = float(input(f"Enter x{i + 1}: "))
        y = float(input(f"Enter y{i + 1}: "))
        model.insert_point(x, y)

    #Reading input X for prediction
    X_input = float(input("Enter X for prediction: "))

    #Predict Y using k-NN Regression
    result = model.predict(X_input, k)

    #Print result or error
    print("Predicted Y:" if isinstance(result, float) else "Result:", result)


if __name__ == "__main__":
    main()
