from module6_knn_mod import KNNRegressor


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
