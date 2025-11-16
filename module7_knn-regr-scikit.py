#!/usr/bin/env python3
#Scikit-learn intro

import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def main():
    # Read N
    N = int(input("Enter a positive integer N: "))
    if N <= 0:
        print("Error: N must be positive.")
        return

    # Read k
    k = int(input("Enter a positive integer k: "))
    if k <= 0:
        print("Error: k must be positive.")
        return

    # Read N (x, y) points
    print(f"Enter {N} points, each with x then y:")
    data = np.zeros((N, 2), dtype=float)

    for i in range(N):
        x_val = float(input(f"Enter x for point {i+1}: "))
        y_val = float(input(f"Enter y for point {i+1}: "))
        data[i] = [x_val, y_val]

    # Separate into X_train and y_train
    X_train = data[:, 0].reshape(-1, 1)
    y_train = data[:, 1]

    # Ask for query point X
    X_query = float(input("Enter the value of X for prediction: "))
    X_query_arr = np.array([[X_query]])

    # Check if k <= N
    if k > N:
        print("Error: k cannot be greater than N.")
        return

    # KNN regression using scikit-learn
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_query_arr)[0]

    # Variance of labels
    label_variance = np.var(y_train)

    print(f"\nPredicted Y for X = {X_query}: {y_pred}")
    print(f"Variance of training labels (y-values): {label_variance}")


if __name__ == "__main__":
    main()
