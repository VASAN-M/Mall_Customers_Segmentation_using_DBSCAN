# Mall Customers Segmentation using DBSCAN

This project applies the DBSCAN (Density-Based Spatial Clustering of
Applications with Noise) algorithm to segment mall customers based on
their annual income and spending behavior. DBSCAN is particularly useful
for identifying clusters of arbitrary shape and detecting outliers.

---

## Dataset
- File: `Mall_Customers.csv`
- Features used for clustering:
  - `Annual_Income_(k$)`
  - `Spending_Score`
- Additional columns:
  - `CustomerID`
  - `Genre`
  - `Age`

---

## Workflow

### 1. Data Exploration
- Loaded the dataset using pandas
- Inspected:
  - Dataset structure and data types
  - Statistical summary of numerical features
  - Dataset shape and column integrity

---

### 2. Data Preprocessing
- Encoded categorical feature:
  - `Genre`: Male → 0, Female → 1
- Selected relevant numerical features for clustering
- No target variable is required as DBSCAN is an unsupervised algorithm

---

### 3. Feature Selection
For clustering, the following features were selected:
- `Annual_Income_(k$)`
- `Spending_Score`

These features capture customer purchasing power and spending behavior.

---

### 4. DBSCAN Clustering
- Applied DBSCAN with parameters:
  - `eps = 9`
  - `min_samples = 5`
  - Distance metric: Euclidean
- Identified dense regions as clusters
- Automatically detected noise points (label `-1`)

---

### 5. Visualization
- Visualized clusters using a scatter plot
- Different colors represent different clusters
- Noise points are shown distinctly as outliers

---

## Libraries Used
- pandas
- numpy
- scikit-learn
- matplotlib

---

## How to Run

1. Install dependencies:
```bash
pip install pandas numpy scikit-learn matplotlib
