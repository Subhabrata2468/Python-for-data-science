'''
Write the python program for k-NN model implemented on iris dataset and print accuracy of the
same.
'''
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Step 2: Split the dataset into training and testing sets (70-30 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Train the k-NN model
k = 3  # You can choose different values for k
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Step 4: Make predictions on the test set
y_pred = knn.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

# Step 6: Print the accuracy
print(f"Accuracy of k-NN model with k={k}: {accuracy:.2f}")

'''
output

Accuracy of k-NN model with k=3: 0.98


'''

'''
    Import necessary libraries:
        load_iris to load the Iris dataset.
        train_test_split to split the dataset into training and testing sets.
        KNeighborsClassifier to create and train the k-NN model.
        accuracy_score to evaluate the model's accuracy.

    Load the Iris dataset:
        load_iris() loads the Iris dataset into a dictionary-like object.
        X contains the features (sepal length, sepal width, petal length, petal width).
        y contains the target labels (species of Iris).

    Split the dataset:
        train_test_split(X, y, test_size=0.3, random_state=42) splits the data into 70% training and 30% testing sets.

    Train the k-NN model:
        KNeighborsClassifier(n_neighbors=k) initializes the k-NN classifier with k neighbors.
        knn.fit(X_train, y_train) trains the k-NN model using the training data.

    Make predictions:
        knn.predict(X_test) makes predictions on the test data.

    Evaluate the model:
        accuracy_score(y_test, y_pred) calculates the accuracy of the model by comparing the true labels (y_test) with the predicted labels (y_pred).

    Print the accuracy:
        The accuracy of the k-NN model is printed, showing the proportion of correct predictions.
'''