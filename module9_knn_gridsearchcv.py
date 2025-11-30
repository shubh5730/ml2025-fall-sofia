import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Read Training Set

N = int(input("Enter N (number of training samples): "))

train_x = []
train_y = []

print("\nEnter training pairs (x then y):")
for i in range(N):
    x = float(input(f"Train x[{i+1}]: "))
    y = int(input(f"Train y[{i+1}]: "))
    train_x.append(x)
    train_y.append(y)

train_x = np.array(train_x).reshape(-1, 1)
train_y = np.array(train_y)

# Read Test Set

M = int(input("\nEnter M (number of test samples): "))

test_x = []
test_y = []

print("\nEnter test pairs (x then y):")
for i in range(M):
    x = float(input(f"Test x[{i+1}]: "))
    y = int(input(f"Test y[{i+1}]: "))
    test_x.append(x)
    test_y.append(y)

test_x = np.array(test_x).reshape(-1, 1)
test_y = np.array(test_y)
 
# Best k
max_k = min(10, N)  # Assumption k <= number of training samples
best_k = None
best_acc = -1

for k in range(1, max_k + 1):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(train_x, train_y)

    preds = model.predict(test_x)
    acc = accuracy_score(test_y, preds)

    if acc > best_acc:
        best_acc = acc
        best_k = k


#Result

print(f"Best k: {best_k}")
print(f"Test Accuracy: {best_acc:.4f}")
