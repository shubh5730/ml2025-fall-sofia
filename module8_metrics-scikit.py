import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Ask user for number of samples
    N = int(input("Enter a positive integer N: "))

    # Initialization
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    # Read N (x, y)
    print("\nEnter the data points. Each point has:")
    print("X = ground truth label (0 or 1)")
    print("Y = predicted label   (0 or 1)")
    
    for i in range(N):
        x_val = int(input(f"\nEnter X (ground truth) for point {i+1}: "))
        y_val = int(input(f"Enter Y (prediction) for point {i+1}: "))
        X[i] = x_val
        Y[i] = y_val

    #Precision and recall calculation using scikit-learn
    precision = precision_score(X, Y, zero_division=0)
    recall = recall_score(X, Y, zero_division=0)

    # Output
    print("\n--- RESULTS ---")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")


if __name__ == "__main__":
    main()
