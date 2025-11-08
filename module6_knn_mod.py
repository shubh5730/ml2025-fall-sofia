import numpy as np


class KNNRegressor:
    """Simple k-NN Regression model using NumPy arrays."""

    def __init__(self):
        """Initialize empty arrays for X and Y."""
        self.X = np.array([], dtype=float)
        self.Y = np.array([], dtype=float)

    def insert_point(self, x: float, y: float):
        """Insert a new (x, y) point into the dataset."""
        self.X = np.append(self.X, x)
        self.Y = np.append(self.Y, y)

    def predict(self, x_input: float, k: int):
        """
        Perform k-NN regression: predict Y for given X.
        Returns:
            - Mean Y value of k nearest neighbors if k <= N
            - Error message if k > N
        """
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
