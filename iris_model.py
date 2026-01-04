# 1 Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# 2 Load Dataset
df = sns.load_dataset('iris')
print(df.head())

# 3 Data Exploration
print(df.describe())
print("\nMissing Values:\n", df.isnull().sum())

# 4 Visualization - Pairplot (1st)  ||   show all diagram in one frame
sns.pairplot(df, hue="species")
plt.show()

# Visualization - Heatmap (FIXED) (2nd)
plt.figure(figsize=(6,4))
sns.heatmap(df.drop("species", axis=1).corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 5 Prepare Data for Training
X = df.drop("species", axis=1)
y = df["species"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize Data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 6 Model Training (KNN)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 7 Model Evaluation
y_pred = model.predict(X_test)

# Accuracy Score
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%\n")

# Classification Report
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# 8 Save Model + Scaler
joblib.dump(model, "iris_model.pkl")
joblib.dump(scaler, "iris_scaler.pkl")
print("Model Saved Successfully ")
print("Scaler Saved Successfully ")

# testing
sample = [[5.9, 3.0, 5.1, 1.8]]
sample_scaled = scaler.transform(sample)
print("\nSample Prediction:", model.predict(sample_scaled)[0])

